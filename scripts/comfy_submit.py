import os, json, requests
from pathlib import Path
ROOT = Path(__file__).parents[1]
url = os.environ.get('COMFYUI_URL','http://127.0.0.1:8188')
wf = ROOT/'workflows/comfyui/wan22_animate_move.json'
if not wf.exists():
    raise SystemExit('Workflow Wan2.2 ainda não instalado/validado.')
workflow = json.loads(wf.read_text(encoding='utf-8'))
r = requests.post(f'{url}/prompt', json={'prompt':workflow}, timeout=30)
r.raise_for_status()
print(r.json())
