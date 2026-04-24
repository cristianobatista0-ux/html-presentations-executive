# Intake — antes de gerar qualquer deck

Use este roteiro quando qualquer **gatilho** abaixo aparecer no chat. O objetivo é **não** gerar `deck.json`, HTML, PDF ou PPTX até coletar dados mínimos e confirmar narrativa.

## Gatilhos (acionam este fluxo)

- `modo apr:` ou `modo apresentação:`
- `nova apresentação`, `novo deck`, `novo pitch`
- `reunião semanal`, `reunião de`, `comitê`, `board`, `QBR`
- `deck executivo`, `apresentação executiva`, `update gerencial`
- Pedido explícito de `.html`, `.pdf` ou `.pptx` de slides

## Regras para o agente

1. **Uma pergunta por vez** — não envie questionário de 7 itens de uma vez.
2. **Não** escreva `deck.json` nem rode `render_html.py` / `export_pdf.py` / `generate_pptx.py` antes das **7 respostas**.
3. Ao terminar as 7, resuma **BLUF** (1 frase) + **SCQA** (4 frases: S, C, Q, A) e peça **confirmação** do usuário.
4. Só após confirmação: montar `deck.json`, gerar **HTML** (padrão); **PDF** se for distribuir/arquivar fora do live; **PPTX** só se o usuário pedir edição no PowerPoint.
5. Se o usuário usar marca: ler [brand/README.md](brand/README.md) e `brand/brand.json` (se existir); presets em [STYLE_PRESETS.md](STYLE_PRESETS.md).

## As 7 perguntas (ordem fixa)

**1. Audiência** — Quem está na sala? (board, C-level, diretoria, VPs, squad interno, cliente, investidor, outro)

**2. Decisão buscada** — O que precisa sair da reunião? (aprovação / budget / mudança de estratégia / alinhamento informativo)

**3. Duração** — Quanto tempo fala? (10 / 30 / 60 min). Regra: ~1 slide a cada 2–3 minutos; não estourar.

**4. BLUF** — Em **uma frase**, qual é a mensagem central (verbo forte + número se couber)?

**5. Dados** — Os números vêm de onde? (usuário anexa / cola / pede para o agente buscar com fontes explícitas)

**6. Preset visual** — Qual estilo HTML? Padrão `swiss_modern`; alternativas `bold_signal`, `dark_botanical`, `paper_ink`; ou sugerir `python scripts/preview_styles.py` para comparar 3 previews.

**7. Marca oficial** — Usar `brand/brand.json` + pastas `brand/logos/` e `brand/images/`? (sim → `brand_path` ou objeto `brand` no JSON; não → `brand_mode`: `off` e só preset)

## Depois do intake

- Action titles + `kicker` por slide (ver [narrative.md](narrative.md)).
- Caminhos de imagem relativos ao arquivo `deck.json`.
- QA: viewports no HTML (ver [STYLE_PRESETS.md](STYLE_PRESETS.md)); PPTX opcional com pipeline da [SKILL.md](SKILL.md).
