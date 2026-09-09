import json, sys
from pathlib import Path
from jsonschema import validate

episode_path = Path(sys.argv[1])
root = episode_path.parents[1]
schema = json.loads((root/'schemas/episode.schema.json').read_text(encoding='utf-8'))
episode = json.loads(episode_path.read_text(encoding='utf-8'))
validate(instance=episode, schema=schema)
for s in episode['scenes']:
    assert s['end'] > s['start'], f"{s['id']}: end <= start"
    assert s['end'] <= episode['duration_s'], f"{s['id']}: excede duração"
    if 'nenito' in s['characters']:
        assert s.get('motion_id'), f"{s['id']}: motion_id obrigatório"
print('OK:', episode['episode_id'])
