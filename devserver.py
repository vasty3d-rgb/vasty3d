"""
Локальный дев-сервер для тестирования сайта.

Помимо обычной раздачи файлов умеет:
- Accept-Ranges: bytes — без этого Chrome помечает <video> как непеределываемое
  (seekable=[0,0]); чисто ограничение встроенного http.server, на реальном
  хостинге (nginx, Vercel, GitHub Pages и т.д.) заголовок отправляется сам.
- POST /__api/save   — сохраняет HTML-страницу на диск (для панели редактирования).
- POST /__api/upload — принимает загруженный файл (картинку/видео) и кладёт
  его в assets/uploads/.

Оба API-эндпоинта работают ТОЛЬКО с localhost (127.0.0.1/::1) — сервер слушает
все интерфейсы (для доступа с телефона в локальной сети), но запись на диск
разрешена только с этой же машины.
"""
import sys
import os
import re
import json
import time
import secrets
import hmac
import mimetypes
import urllib.parse
from http.cookies import SimpleCookie
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(ROOT, 'assets', 'uploads')
BACKUP_DIR = os.path.join(ROOT, 'backups')

# какие HTML-файлы разрешено перезаписывать через /__api/save
SAVEABLE_FILES = {'index.html', '404.html'}

SAFE_NAME_RE = re.compile(r'[^A-Za-z0-9._-]+')

# доступ к /admin с не-localhost адресов защищён этим логином/паролем;
# на хостинге можно переопределить через переменные окружения ADMIN_USER/ADMIN_PASS
ADMIN_USER = os.environ.get('ADMIN_USER', 'vasty')
ADMIN_PASS = os.environ.get('ADMIN_PASS', '16022002')
SESSION_COOKIE = 'sa_session'
SESSIONS = set()  # валидные токены сессий (в памяти, сбрасываются при рестарте сервера)


def is_local(handler):
    return handler.client_address[0] in ('127.0.0.1', '::1')


def get_session_token(handler):
    cookie_header = handler.headers.get('Cookie')
    if not cookie_header:
        return None
    cookie = SimpleCookie()
    try:
        cookie.load(cookie_header)
    except Exception:
        return None
    morsel = cookie.get(SESSION_COOKIE)
    return morsel.value if morsel else None


def is_authed(handler):
    # с localhost (собственная машина) панель работает без логина — как раньше
    if is_local(handler):
        return True
    token = get_session_token(handler)
    return bool(token) and token in SESSIONS


class RangeAwareHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        super().end_headers()

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ('/admin', '/admin/'):
            self.path = '/index.html'
        elif self.path == '/__api/me':
            return self._json(200, {'authed': is_authed(self)})
        return super().do_GET()

    def do_POST(self):
        if self.path == '/__api/login':
            return self._handle_login()
        if self.path == '/__api/logout':
            return self._handle_logout()
        if self.path == '/__api/save':
            return self._handle_save()
        if self.path == '/__api/upload':
            return self._handle_upload()
        self._json(404, {'error': 'not found'})

    def _handle_login(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length)
            data = json.loads(raw.decode('utf-8'))
            user = str(data.get('user', ''))
            pw = str(data.get('pass', ''))
            ok = hmac.compare_digest(user, ADMIN_USER) and hmac.compare_digest(pw, ADMIN_PASS)
            if not ok:
                return self._json(401, {'error': 'неверный логин или пароль'})
            token = secrets.token_hex(32)
            SESSIONS.add(token)
            body = json.dumps({'ok': True}, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Set-Cookie', f'{SESSION_COOKIE}={token}; Path=/; HttpOnly; SameSite=Lax; Max-Age=2592000')
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            self._json(500, {'error': str(e)})

    def _handle_logout(self):
        token = get_session_token(self)
        SESSIONS.discard(token)
        body = json.dumps({'ok': True}, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Set-Cookie', f'{SESSION_COOKIE}=; Path=/; HttpOnly; Max-Age=0')
        self.end_headers()
        self.wfile.write(body)

    def _handle_save(self):
        if not is_authed(self):
            return self._json(403, {'error': 'нет доступа — войдите в /admin'})
        try:
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length)
            data = json.loads(raw.decode('utf-8'))
            filename = data.get('file', 'index.html')
            html = data.get('html', '')
            if filename not in SAVEABLE_FILES:
                return self._json(400, {'error': f'файл {filename} нельзя сохранять'})
            if not html or '<html' not in html[:2000].lower():
                return self._json(400, {'error': 'пустой или некорректный HTML'})

            target = os.path.join(ROOT, filename)
            os.makedirs(BACKUP_DIR, exist_ok=True)
            if os.path.exists(target):
                stamp = time.strftime('%Y%m%d-%H%M%S')
                backup_path = os.path.join(BACKUP_DIR, f'{filename}.{stamp}.bak')
                with open(target, 'r', encoding='utf-8') as f_old:
                    old_content = f_old.read()
                with open(backup_path, 'w', encoding='utf-8') as f_bak:
                    f_bak.write(old_content)

            with open(target, 'w', encoding='utf-8', newline='\n') as f:
                f.write(html)

            self._json(200, {'ok': True, 'file': filename, 'backup': True})
        except Exception as e:
            self._json(500, {'error': str(e)})

    def _handle_upload(self):
        if not is_authed(self):
            return self._json(403, {'error': 'нет доступа — войдите в /admin'})
        try:
            length = int(self.headers.get('Content-Length', 0))
            if length <= 0 or length > 60 * 1024 * 1024:
                return self._json(400, {'error': 'файл пустой или больше 60МБ'})
            raw = self.rfile.read(length)

            orig_name = self.headers.get('X-Filename', 'file')
            try:
                orig_name = urllib.parse.unquote(orig_name)
            except Exception:
                pass
            orig_name = os.path.basename(orig_name)
            base, ext = os.path.splitext(orig_name)
            base = SAFE_NAME_RE.sub('-', base).strip('-') or 'file'
            ext = SAFE_NAME_RE.sub('', ext)
            stamp = time.strftime('%Y%m%d-%H%M%S')
            final_name = f'{base}-{stamp}{ext}'

            os.makedirs(UPLOAD_DIR, exist_ok=True)
            with open(os.path.join(UPLOAD_DIR, final_name), 'wb') as f:
                f.write(raw)

            url = f'assets/uploads/{final_name}'
            self._json(200, {'ok': True, 'url': url})
        except Exception as e:
            self._json(500, {'error': str(e)})


if __name__ == '__main__':
    # облачные хостинги (Render, Railway и т.п.) передают порт через $PORT —
    # аргумент командной строки остаётся приоритетным для локального запуска
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = int(os.environ.get('PORT', 5599))
    print(f'Сервер слушает порт {port}  (Ctrl+C — остановить)')
    ThreadingHTTPServer(('0.0.0.0', port), RangeAwareHandler).serve_forever()
