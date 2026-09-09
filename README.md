# NenitoClub — Animation Pilot

Pipeline experimental automation-first para validar um piloto de 20–30 segundos antes de escalar para vídeos de 3–4 minutos.

## Princípios
- MASTER oficial obrigatório para personagens humanos.
- Geração aberta por prompt não pode produzir asset humano canônico.
- WIP não vira APPROVED automaticamente.
- GitHub = código, workflows e versionamento.
- Google Drive = fonte patrimonial/canônica.
- ComfyUI = execução visual local.
- Gemini = roteiro/JSON.
- FFmpeg/librosa = montagem e sincronização.

## Meta de escala
1. Piloto 20–30 s.
2. Primeiro vídeo 3–4 min.
3. 2 vídeos/semana.
4. 3–4 vídeos/semana.
5. Meta: 1 vídeo/dia.

## Pipeline
tema → Gemini → episode.json → canon gate → áudio → timing → motion → ComfyUI/Wan → composição → QC → export

## Status
LAB / WIP.
