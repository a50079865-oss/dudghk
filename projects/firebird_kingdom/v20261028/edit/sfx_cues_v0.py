"""SFX cue sheet v0: one bed per scene + spot effects per clip. No music."""
import json
tl = {c['idx']: c for c in json.load(open('edit/timeline_v0.json'))['clips']}

# scene beds (loop under the whole scene)
beds = {
 'S01': 'desolate wind over a burned plain, faint crackle of dying embers, distant crows, no music',
 'S02': 'burned village square ambience: low wind, crackling fires, shuffling refugee footsteps on ash, murmurs without words, a distant crying baby, no music',
 'S03': 'quiet close room tone, soft ember hiss, cloth rustle, no music',
 'S04': 'ruined stone chapel interior: hollow wind through a broken roof, single candle flame flutter, slow drips, creaking charred beams, no music',
 'S05': 'muffled memory: low dull wind, distant crowd murmur filtered and slowed, faint creak of rope, no music',
 'S06': 'tense chapel interior: armor creak and chainmail shifts, heavy boots on stone, wind through the doorway, embers ticking, no music',
 'S07': 'roaring fire, crackling burning timber, falling sparks, smoke rush, no music',
 'S08': 'sudden total silence: near-silent air tone with an extremely faint high shimmer, no music',
 'S09': 'high moor wind, distant smoke crackle far below, cloak fabric flapping, no music',
}
# spot effects: idx -> list of (offset_s, description)
spots = {
 1: [(0.5, 'gust of wind carrying ash')], 2: [(1.0, 'crows ruffling feathers, a single caw'), (2.5, 'horse snort in distance')],
 3: [(1.5, 'deep low groan of thick ice shifting under pressure')], 4: [(1.0, 'faint metallic hum of a cracked bronze bell trembling, ash trickling')],
 5: [(1.0, 'tiny ember sizzle on metal')], 6: [(0.5, 'fire roar reflected, crow eye blink')], 7: [(0.5, 'footsteps crunching in ash fading away')],
 8: [(0.3, 'linen bandage pulled taut, fabric stretch')], 9: [(0.5, 'crowd footsteps passing, cloth bandage wrapping')],
 10: [(1.0, 'bandage pressed, a wounded man groans softly')], 11: [(0.5, 'ash falling softly, her breath out through the nose')],
 12: [(0.5, 'hands on a shawl, cloth rustle')], 13: [(0.8, 'knuckles tightening, skin and fabric creak')],
 14: [(0.5, 'wind rising, footsteps receding')], 15: [(0.3, 'fibers snapping')], 16: [(0.5, 'leather sheath, handle grip')],
 17: [(0.5, 'blade turning, faint metallic ring')], 18: [(0.0, 'candle wick crackle')], 19: [(0.5, 'wax drip tick on bronze')],
 20: [(0.5, 'metal gauntlet settling on stone')], 21: [(1.0, 'footsteps on stone and ash entering, soldier stirring on a wooden pew')],
 22: [(0.5, 'soldier sharp breath'), (3.5, 'blade drawn back'), (5.0, 'leather pouch rummaged, empty'),
      (8.5, 'braid grabbed, hair tension'), (9.5, 'knife sawing through thick hair, strand snapping'), (11.5, 'cut braid falls free'),
      (13.0, 'tying knot pulled tight, soldier gasps')],
 25: [(0.5, 'small footsteps stop in the doorway')], 26: [(0.5, 'candle flicker, breath')], 27: [(0.5, 'heartbeat-like low pulse, very subtle')],
 28: [(0.3, 'rope fibers twisting, creak')], 29: [(0.2, 'rope creak swinging in wind')], 30: [(0.2, 'crowd jostle, a mother gasp without words')],
 31: [(0.2, 'many feet moving, then stillness')], 32: [(0.3, 'iron-shod hoof slamming on stone, ash burst')], 33: [(0.2, 'heavy war banner snapping in wind')],
 34: [(0.3, 'distant rhythmic hoofbeats making dust tremble on wood')], 35: [(0.5, 'heavy boots and armor entering a doorway')],
 36: [(0.5, 'knife raised, child whimper breath')], 37: [(0.5, 'sword tip scraping stone')], 38: [(0.5, 'armor creak, tense breath')],
 39: [(0.5, 'leather gauntlet on cloth, stitches tugged')], 40: [(0.5, 'grip tightening on a sword hilt, leather creak')],
 41: [(0.5, 'quiet exhale')], 42: [(0.5, 'fabric scrap crumpled in a fist')], 43: [(0.5, 'sword pushed back into scabbard, steel slide and click')],
 44: [(0.3, 'ember pulsing crackle in a charred beam')], 45: [(0.3, 'wool coat rustle')],
 46: [(0.2, 'burning roof beam cracking and crashing down, sparks exploding')], 47: [(0.3, 'cloak whipped around, embers swirling, falling debris')],
 48: [(0.2, 'sharp intake of breath, fire roar close')], 49: [(0.0, 'all sound sucked away into silence')], 50: [(0.5, 'single soft flame stillness tone')],
 51: [(0.5, 'suspended silence')], 52: [(0.3, 'soft airy whoosh of ash rising')], 53: [(0.5, 'vast low wing-beat rumble behind clouds, very distant')],
 54: [(0.5, 'distant church bells starting to ring by themselves, overlapping')], 55: [(0.5, 'feather drifting, faint warm crackle')],
 56: [(0.3, 'ember touching skin, soft glowing hum, no burn')], 57: [(0.5, 'sword slowly lowered, steel whisper')],
 58: [(0.3, 'feather filament glowing hum')], 59: [(0.3, 'smoke column rumble')], 60: [(0.3, 'boots on wind-flattened grass')],
 61: [(0.5, 'cloak flapping in high wind')], 62: [(0.3, 'breath inside a hood')],
}
cues = []
for idx, c in tl.items():
    for off, desc in spots.get(idx, []):
        cues.append({'idx': idx, 'slot': c['slot'], 'scene': c['scene'], 't': round(c['start'] + off, 2), 'sfx': desc})
scene_span = {}
for c in tl.values():
    # bridge cuts (S01→S02) pre-lap the next scene's bed
    s = scene_span.setdefault(c['scene'].split('→')[-1], [c['start'], c['end']]); s[0] = min(s[0], c['start']); s[1] = max(s[1], c['end'])
bed_list = [{'scene': k, 'start': round(v[0], 2), 'end': round(v[1], 2), 'sfx': beds[k]} for k, v in sorted(scene_span.items())]
json.dump({'version': 'v0', 'rule': 'SFX only, no BGM, no voices', 'beds': bed_list, 'spots': cues},
          open('edit/sfx_cues_v0.json', 'w'), ensure_ascii=False, indent=1)
print(len(bed_list), 'beds', len(cues), 'spots')
for b in bed_list: print(b['scene'], b['start'], b['end'])
