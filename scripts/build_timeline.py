import json, sys
from pathlib import Path

p = Path(sys.argv[1])
episode = json.loads(p.read_text(encoding='utf-8'))
timeline = {'episode_id':episode['episode_id'],'duration_s':episode['duration_s'],'tracks':{'video':[],'audio':[]}}
for s in episode['scenes']:
    timeline['tracks']['video'].append({
        'scene':s['id'],'start':s['start'],'end':s['end'],
        'characters':s['characters'],'motion':s.get('motion_id'),
        'background':s.get('scene_asset'),'camera':s.get('camera')
    })
    if s.get('narration'):
        timeline['tracks']['audio'].append({'scene':s['id'],'start':s['start'],'text':s['narration']})
out = p.parents[1]/'outputs'/f"{episode['episode_id']}_timeline.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(timeline,ensure_ascii=False,indent=2),encoding='utf-8')
print(out)
