# Política do repositório público

Este repositório é público para código, automação, schemas, workflows e documentação técnica genérica.

## Nunca versionar aqui
- chaves API, tokens ou arquivos `.env`
- MASTERs canônicos dos personagens
- documentos confidenciais de origem/inspiração
- dados pessoais
- músicas/áudios comerciais ainda não publicados
- arquivos de Drive usados como fonte patrimonial

## Pode versionar
- código Python
- workflows GitHub Actions
- workflows ComfyUI sem segredos
- schemas JSON
- manifests técnicos sem conteúdo privado
- testes sintéticos
- documentação do pipeline

## Fontes de verdade
- Google Drive: assets e documentos canônicos/patrimoniais
- GitHub: código, automação, versionamento e CI

O pipeline deve buscar ou receber os MASTERs localmente no momento de renderização, sem commitá-los no repositório público.
