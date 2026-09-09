import json
from pathlib import Path
ROOT = Path(__file__).parents[1]
char = json.loads((ROOT/'config/character_nenito.json').read_text(encoding='utf-8'))

def validate(character_id, master_path):
    if character_id == 'nenito' and not master_path:
        raise SystemExit('BLOCKED: Nenito exige MASTER explícito.')
    if character_id == 'nenito' and char['visual_lock']['lanyard'] is False:
        print('QC: rejeitar qualquer output com cordão/crachá no Nenito.')

validate('nenito','assets/masters/NC_PERSONAGEM_NENITO_MASTER_v1.0.png')
print('CANON GATE OK')
