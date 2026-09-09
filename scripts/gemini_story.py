"""Gera roteiro estruturado usando Gemini.
Exige GEMINI_API_KEY e sempre injeta o manifesto canônico do personagem.
"""
import os
from pathlib import Path
from google import genai

ROOT = Path(__file__).parents[1]
key = os.environ.get('GEMINI_API_KEY')
if not key:
    raise SystemExit('Defina GEMINI_API_KEY.')

client = genai.Client(api_key=key)
canon = (ROOT/'config/character_nenito.json').read_text(encoding='utf-8')
prompt = f'''Você escreve para NenitoClub.
Respeite rigorosamente este canon:\n{canon}\n
Crie um roteiro infantil de 25 segundos, simples, positivo, em PT-BR.
Retorne JSON com 4 cenas contendo id, start, end, characters, action, motion_id, narration, camera e scene_asset.
Não invente roupas, acessórios ou características permanentes.'''
resp = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
print(resp.text)
