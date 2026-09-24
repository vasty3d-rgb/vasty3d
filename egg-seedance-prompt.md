# Промт для ролика easter egg (Seedance 2.5)

Прикрепить референс персонажа в полный рост как `@image1` (тот, что на белом фоне).
Результат положить в `assets/video/egg.mp4` — команды пережатия в `README.md`.

Один непрерывный дубль ~11 секунд, 16:9, фон абсолютно чёрный (чтобы ролик бесшовно
сел на чёрный оверлей сайта). Динозаврик описан визуально как пиксельный спрайт,
без упоминания бренда.

```text
SCENE CONTEXT
A stylized chibi-proportioned boy drops out of darkness into a pool of light on an unseen floor, walks straight toward the camera, greets the viewer with a wave, then a small pixel-art tyrannosaurus charges in from frame left, startles him, and both bolt out of frame right, leaving the empty lit floor behind. Void environment, no walls, no horizon, no props.

ACTIVE REFERENCES
@image1: a stylized chibi-proportioned boy, roughly 1.2 m tall, oversized head relative to a small torso, spiky bright white hair, ornate chrome-silver wraparound sunglasses with pierced scrollwork frames and solid black lenses, a plain black crewneck sweatshirt with dropped shoulders, wide-leg black cargo trousers breaking over the shoe, chunky black sneakers with white midsoles. Skin is smooth matte, with a faint closed-mouth smile. 100% matches the reference. @image1 defines one unique person; exactly one physical instance of @image1 exists in the scene.

LOCATION MAP
Pure black void. A single soft elliptical pool of light, about 3 m across, sits on an unseen matte floor in the lower third of frame, slightly right of center. Fine dust drifts through the light column. Background, midground walls and horizon are absent and stay absolutely black. Camera sits on the floor side of the pool, 4 m back, lens height 0.6 m. Character movement path runs from the pool center straight toward the camera, then hard to frame right. The tyrannosaurus path runs in a straight line from frame left to frame right across the near edge of the pool.

FIRST FRAME / BLOCKING
Empty asymmetrical composition: the lit pool occupies the lower-right third, the upper-left two thirds are solid black negative space. No character present. Dust particles already drifting downward through the light.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
Full-body framing throughout, 47 degrees FOV for the entire take, no drift mid-segment.

CAMERA
Static locked-off camera at 0.6 m lens height, slight low angle looking up at the character. The camera does not pan, tilt, dolly or zoom. Focus is pre-set on the pool center and holds as the character approaches; he stays acceptably sharp from 4 m to 1.6 m. Highlights roll off softly, blacks stay deep and unlifted.

ACTION
0.0s to 0.6s — Empty lit pool, dust drifting.
0.6s to 1.5s — @image1 drops into frame from above at speed, feet first, and lands in the pool center in a deep crouch; a thin ring of dust blows outward from the contact point and his white hair flattens then rebounds.
1.5s to 2.3s — He rises, steadies his balance, and pushes his sunglasses up the bridge of his nose with one index finger.
2.3s to 4.2s — He walks toward the camera at about 3 km/h, five unhurried steps, growing from full-body wide to full-body close where he fills roughly 80 percent of frame height, and stops at 1.6 m from the lens.
4.2s to 5.8s — He raises his right hand to shoulder height and waves twice, side to side, wrist loose; his smile widens slightly. This is a deliberate direct address to the viewer, so his eyes meet the lens for this beat only.
5.8s to 6.6s — A small pixel-art tyrannosaurus enters at speed from frame left, crossing the near edge of the pool at about 14 km/h.
6.6s to 7.4s — He snaps his head to camera-left toward the approaching creature; his shoulders lift, his torso pulls back, his heels shift backward and his waving hand freezes mid-air.
7.4s to 9.6s — He spins right and sprints out of frame right at about 16 km/h, arms pumping; the tyrannosaurus follows the same line and exits frame right one beat behind him.
9.6s to 11.0s — Empty lit pool again, dust unsettled and slowly falling, black void on all sides.

PERFORMANCE
On landing, the oversized head carries visible inertia and bobbles once before the neck settles. During the walk, his eyeline stays level on the lens housing area but reads as scanning the dark room, not as contact, until the wave. On the wave, the smile reaches the cheeks before the hand fully lifts and his head tilts a few degrees toward his raised hand. On the scare, the trigger is the creature entering his peripheral vision: eyes snap left behind the dark lenses, the head leads and the shoulders follow a fraction later, the jaw drops slightly open, one shallow sharp inhale lifts the chest, the raised hand stalls then drops, and the weight transfers to the back foot before he commits to the sprint. Recovery is immediate flight, not a held pose.

PHYSICS
Chibi proportions carry real mass: the fall accelerates under gravity, the landing compresses knees and ankles with the floor absorbing the impact, and the dust ring expands outward low and thin before settling. The wide cargo trousers swing with delay and drag behind each leg, the sweatshirt hem lifts on the sprint. The sprint shows credible heel-to-toe contact, vertical oscillation and arm counter-swing at chibi limb length. The tyrannosaurus is a flat two-dimensional pixel sprite moving through three-dimensional space: it stays perfectly perpendicular to the camera, alternates between exactly two leg positions in a fast cycle, and does not rotate, deform or gain volume. It casts no light and receives none.

LIGHTING
A single soft top-front source hangs 4 m above and slightly right of the pool center, pointing down, creating the elliptical pool and a short contact shadow directly under the character. A narrow cool rim from high behind separates his white hair and shoulders from the black void. Key-to-fill ratio is wide, roughly 8 to 1, so the void reads as true black with no ambient bounce. The chrome sunglasses frames catch the top light as hard specular glints. White balance fixed at 5600K. Haze density 15 percent inside the light column only.

WARDROBE
Black crewneck sweatshirt, matte cotton, dropped shoulders, slightly oversized. Wide-leg black cargo trousers, heavy fabric, stacking over the shoe. Chunky black sneakers with white midsoles. All garments stay clean and identical from first frame to last.

AUDIO
SFX only. A short descending air rush during the fall, one soft low thud with a dry dust scatter on landing, cotton fabric rustle as he rises, a single fingertip tap on the sunglasses frame, five soft rubber sneaker contacts on a hard matte floor during the walk, cloth movement on the wave. The creature arrives with a thin two-tone electronic blip followed by dry rapid pixel-quantized footfalls panning left to right. One sharp inhale on the scare, then fast scuffing sneaker sprints trailing off to frame right, the blipping footfalls trailing after. The final 1.4 seconds hold near-silence with a faint high room hiss and settling dust. No music, no score, no tonal pads, no dialogue.

STYLE
Photoreal rendering of a stylized character: subsurface-soft skin, individually resolved hair strands, physically accurate chrome on the sunglasses frames, real cloth simulation. The tyrannosaurus stays deliberately flat pixel art against that realism, hard-edged and unfiltered. Fine natural film grain, no chromatic aberration, no lens flare.

OUTPUT SETTINGS
16:9 aspect ratio. Spherical lens behavior, no anamorphic squeeze. Real-time speed throughout.

POSITIVE LOCKS
@image1 keeps identical face, hair, sunglasses, wardrobe and 1.2 m height through the entire take, with one head, one torso, two arms and two legs.
Exactly one physical instance of @image1 and exactly one tyrannosaurus exist in the shot.
The background stays pure black on all sides for the full duration, with the lit floor pool as the only visible surface.
The tyrannosaurus remains flat dark-grey low-resolution pixel art, roughly 0.9 m tall with its back at the character's chest height, and never becomes realistic, volumetric or textured.
The tyrannosaurus enters from frame left and both characters exit frame right; screen direction never reverses.
Lens-facing eye contact occurs only during the 4.2s to 5.8s wave; every other gaze points into the dark room or toward the creature at frame left.
The capture camera remains outside the rendered world and casts no shadow into the light pool.
The camera stays locked off at 47 degrees for the whole take.
All contact points, weight shifts and momentum stay physically coherent for a 1.2 m chibi body.
The final frame is the empty lit pool with settling dust and no characters.
```

## Если 11 секунд не влезает в один прогон

Резать по паузам, они для этого и стоят:
- **дубль 1** — с 0.0с по 5.8с (падение, подход, взмах), последний кадр придержать;
- **дубль 2** — с 5.8с по 11.0с (динозаврик, испуг, побег).

Во втором дубле обязательно повторить весь блок `ACTIVE REFERENCES` и `LIGHTING` —
Seedance не помнит предыдущую генерацию. Склеить в любом редакторе, стык на взмахе.
