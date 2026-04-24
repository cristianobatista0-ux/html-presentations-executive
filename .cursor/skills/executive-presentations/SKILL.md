---
name: executive-presentations
description: Creates executive-grade slide decks as self-contained HTML (viewport-fit, presets, optional brand palette) with optional PDF export and optional PowerPoint (.pptx). Strong narrative (Minto Pyramid, SCQA, action titles, BLUF) and intentional visual design. Use whenever the user asks for an executive presentation, board deck, pitch, HTML slides, PDF handout, or mentions apresentação executiva, deck, slides, PPT, PPTX, board, QBR — or wants to improve an existing .pptx storyline.
---

# Executive Presentations

**Caminho principal:** HTML self-contained (`render_html.py`) com tipografia web, presets visuais e `brand`/`brand_mode` — depois **PDF** para distribuição (`export_pdf.py`). **Opcional:** `.pptx` via `generate_pptx.py` quando o time precisa editar no PowerPoint.

Inspirada na skill Anthropic `pptx`, na filosofia viewport-first da skill `frontend-slides` (SkillsMP), e em Minto / SCQA / action titles / BLUF.

## Non-negotiables (HTML, alinhados a frontend-slides)

1. **Zero dependência em runtime:** um arquivo `.html` com CSS/JS inline; fontes via Google Fonts no `<head>`.
2. **Viewport fit:** cada slide = `100vh` / `100dvh`, sem scroll interno; conteúdo demais vira outro slide.
3. **Show, don't tell:** indeciso no estilo? Rode `preview_styles.py` ou peça 3 previews antes do deck final.
4. **Design distintivo:** presets (`swiss_modern`, `bold_signal`, …) em [STYLE_PRESETS.md](STYLE_PRESETS.md) — evitar “template genérico”.
5. **Produção:** navegação teclado/toque/scroll, `prefers-reduced-motion`, contraste legível.

## Quando Usar

- Criar deck do zero (board, C-level, QBR, pitch, reunião semanal)
- Entregar **HTML** para apresentar no navegador + **PDF** para quem só lê arquivo
- Revisar narrativa de um `.pptx` existente (storyline) ou gerar `.pptx` quando necessário

## Passo zero — Intake obrigatório

Qualquer **gatilho** de apresentação (ver [intake.md](intake.md)) dispara o roteiro de entrevista: **sete perguntas, uma por vez**. Não gerar `deck.json`, HTML, PDF ou PPTX antes de completar as respostas e o usuário confirmar **BLUF + SCQA**. Detalhes e lista de gatilhos: [intake.md](intake.md).

## Quick Reference

| Tarefa | Leia / comando |
|---|---|
| Intake (perguntas antes de gerar) | [intake.md](intake.md) |
| Setup no outro Mac / trabalho | [SETUP-TRABALHO.md](SETUP-TRABALHO.md) |
| Estruturar a narrativa antes de desenhar | [narrative.md](narrative.md) |
| Presets, viewport, densidade, brand mode | [STYLE_PRESETS.md](STYLE_PRESETS.md) + [visual-design.md](visual-design.md) |
| DS inspiracional (sem nome de marca) | [ds-reference-superapp-fintech-br.md](ds-reference-superapp-fintech-br.md) |
| Perfil (corporate / startup / consulting) | [profiles.md](profiles.md) |
| Exemplos de `deck.json` | [examples.md](examples.md) |
| **Gerar HTML** | `python scripts/render_html.py deck.json output.html` |
| **Gerar PDF** | `python scripts/export_pdf.py output.html output.pdf` |
| 3 previews de estilo (uma página cada) | `python scripts/preview_styles.py` → `.preview/` |
| Gerar .pptx (opcional) | `python scripts/generate_pptx.py deck.json output.pptx` |
| Paleta oficial (trabalho) | Pasta [brand/](brand/) + `brand.json` local (ver `brand.json.example`); no deck: `brand` / `brand_path` + `brand_mode` + `preset` — ver [scripts/brand.example.json](scripts/brand.example.json) |
| Foto remota (PPTX) | `image_url` + `--fetch-images` no `generate_pptx.py` |

---

## Identidade visual (trabalho / marca)

O gerador aceita **paleta corporativa** no JSON raiz — use no trabalho para aderir ao guia de marca:

```json
"brand": {
  "primary": "0B3D5C",
  "primary_dark": "051F30",
  "secondary": "DDE8F0",
  "accent": "E8941E",
  "surface": "F2F6FA",
  "text_dark": "14232E",
  "muted": "5A6B78",
  "on_dark": "FFFFFF",
  "header_font": "Calibri Light",
  "body_font": "Calibri",
  "logo_path": "../../assets/logo.png"
}
```

Alternativa: `"brand_path": "brand.json"` com o mesmo conteúdo (útil para vários decks). Caminhos de `logo_path` e `image_path` nos slides são **relativos à pasta do arquivo `deck.json`**.

---

## História + imagem (obrigatório para deck “de verdade”)

Antes do `deck.json`, escreva em 6 linhas:

1. **Audiência e decisão** da reunião.
2. **BLUF** (uma frase).
3. **SCQA** em quatro frases (situação, complicação, pergunta, resposta).
4. **O que cada slide prova** — um slide = uma prova.
5. **Imagem ou visual** por slide: foto licenciada, gráfico, ícone consistente, ou colagem geométrica (o script gera *bento* se não houver foto).
6. **Onde a paleta da marca entra** (primária, acento, superfície).

O agente **não** deve entregar sequência só de bullets sem arco SCQA, nem comparar números de bases diferentes sem nota metodológica.

---

## Princípio #0 — Narrativa antes de Design

**Nunca comece pelo design.** Um deck executivo bonito com história ruim é descartado; um deck simples com história forte vende.

Fluxo obrigatório:

1. **Definir a mensagem central em UMA frase** (BLUF — Bottom Line Up Front). Se não cabe em uma frase, ainda não está claro.
2. **Estruturar em Pirâmide de Minto**: 1 ideia governante → 3 argumentos de apoio → evidências.
3. **Escrever os action titles de cada slide ANTES de qualquer visual.**
   Um action title é uma frase completa que comunica a conclusão, não o tópico.
   - ❌ "Receita por região"
   - ✅ "Latam cresceu 32% e já responde por 41% da receita — maior motor de crescimento em 2025"
4. **Só então** decidir layout, paleta, tipografia, elementos visuais.

Detalhes completos em [narrative.md](narrative.md).

---

## Workflow Executivo (Checklist)

Copie e acompanhe o progresso:

```
Deck Progress:
- [ ] 0. Intake completo (sete perguntas em intake.md) + confirmação BLUF + SCQA
- [ ] 1. Entrevistar requisitos (audiência, decisão buscada, duração)
- [ ] 2. Escrever BLUF em 1 frase
- [ ] 3. Montar Pyramid + SCQA da abertura (layout `scqa_story`)
- [ ] 4. Redigir action titles + `kicker` de TODOS os slides
- [ ] 5. Escolher `preset` + `profile`; se houver marca, `brand` + `brand_mode` (ver STYLE_PRESETS.md)
- [ ] 6. Garantir foto ou gráfico por slide (`image_path`, `chart`, …)
- [ ] 7. Escrever deck.json
- [ ] 8. Gerar HTML (`render_html.py`) — caminho principal
- [ ] 9. QA HTML (viewports 1920×1080 … 375×667) + export PDF se necessário (`export_pdf.py`)
- [ ] 10. Opcional: gerar .pptx (`generate_pptx.py`) + QA PPTX (markitdown + imagens)
- [ ] 11. Iterar até um passe completo sem issues
```

### Passo 1 — Entrevista de requisitos

Antes de qualquer linha, confirme com o usuário (ou infira e valide):

- **Audiência**: board, C-level, diretoria, VPs, investidores, squad, cliente?
- **Decisão buscada**: aprovação, alocação de budget, mudança de estratégia, update informativo?
- **Duração**: 10 min / 30 min / 60 min → isso define número de slides (regra prática: 1 slide por 2-3 min, nunca mais).
- **Restrições**: identidade visual da empresa, formato do evento, idioma.
- **Perfil**: consultoria, startup ou corporativo (ver [profiles.md](profiles.md)).

Se qualquer item estiver indefinido, **pergunte antes de gerar**.

### Passo 2 — BLUF

Escreva a mensagem em **uma única frase declarativa com verbo forte e número**. Essa frase vai no slide 1 ou 2 (executive summary) e é o fio condutor de tudo.

Exemplos:

- "Recomendamos R$ 18M em capex para expandir Fulfillment na região Sul — payback de 22 meses e +R$ 52M de GMV incremental em 3 anos."
- "Reduzimos churn em 34% no Q3; propomos escalar o programa de CS proativo para toda a base enterprise em 2026."

### Passo 3-4 — Pyramid + Action Titles

Ver [narrative.md](narrative.md) para o método completo.

### Passo 5-7 — Design

Ver [profiles.md](profiles.md) para escolher o perfil e [visual-design.md](visual-design.md) para aplicar paleta, tipografia, layouts e motivo visual.

### Passo 8 — deck.json

Descreva o deck em JSON estruturado antes de gerar. O script lê este arquivo.

**Estrutura mínima** (HTML + opcional PPTX; use `preset` e `brand_mode` para o render web):

```json
{
  "title": "Expansão Fulfillment Sul — Board Deck",
  "profile": "corporate",
  "preset": "swiss_modern",
  "brand_mode": "strict",
  "palette": "midnight_executive",
  "author": "Cristiano Batista",
  "date": "2026-04-23",
  "slides": [
    {
      "layout": "title",
      "title": "Expansão Fulfillment Sul",
      "subtitle": "Recomendação de capex R$ 18M — Board Apr/2026"
    },
    {
      "layout": "executive_summary",
      "action_title": "Recomendamos R$ 18M de capex para abrir CD em Curitiba — payback 22 meses, +R$ 52M GMV em 3 anos",
      "bullets": [
        "Demanda do Sul cresceu 48% em 2025, mas SLA caiu para 72%",
        "CD próprio reduz frete em 31% e NPS sobe 14pt (benchmark interno Norte)",
        "Janela ótima: terreno disponível a R$ 2.100/m², 18% abaixo da média"
      ]
    },
    {
      "layout": "kpi_callout",
      "action_title": "Três indicadores sustentam a tese",
      "kpis": [
        {"value": "22 meses", "label": "Payback esperado"},
        {"value": "+R$ 52M", "label": "GMV incremental (3 anos)"},
        {"value": "31%", "label": "Redução de frete"}
      ]
    }
  ]
}
```

Layouts suportados pelo script:

| Layout | Uso |
|--------|-----|
| `title` | Capa com painel escuro + **foto hero** à direita |
| `chapter` | Capítulo (“01”) + gancho de uma linha + foto |
| `scqa_story` | **SCQA em 4 cartões** — ancora a história antes dos dados |
| `hero_split` | Insight + **número gigante** + bullets + foto |
| `executive_summary` | BLUF em bullets + **foto** à direita |
| `kpi_callout` | Faixa escura + **3 cards** de KPI |
| `two_column`, `chart`, `comparison`, `timeline`, `image_right`, `closing` | Corpo analítico (gráficos, tabela, linha do tempo, fechamento com foto opcional) |

Campos úteis em qualquer slide de conteúdo: `kicker` (rótulo narrativo em caixa alta na faixa), `action_title`, `image_path` ou `image_url`, `source`.

Ver [examples.md](examples.md) e o deck de referência `brand/examples/board_expansao.json`.

### Passo 9 — Geração

```bash
cd .cursor/skills/executive-presentations
python -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt

# Principal: HTML (caminho absoluto no .html ajuda caminhos de imagem)
python scripts/render_html.py path/to/deck.json path/to/output.html

# PDF para distribuição (requer Chrome/Chromium ou Playwright)
python scripts/export_pdf.py path/to/output.html path/to/output.pdf

# Opcional: PowerPoint
python scripts/generate_pptx.py path/to/deck.json output.pptx
```

### Passo 10-11 — QA (obrigatório)

**Assuma que há problemas.** Se na primeira inspeção você não encontrou nada, não olhou direito.

**HTML:** abrir o `.html` no navegador e validar **1920×1080**, **1280×720**, **768×1024**, **375×667**, **667×375** — sem barra de rolagem dentro do slide, textos legíveis, imagens não estourando.

**Conteúdo (PPTX, se gerado):**

```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|placeholder|tbd|todo"
```

**Visual PPTX:** converter para imagens (`soffice` + `pdftoppm`) como em [visual-design.md](visual-design.md) — overlap, overflow, contraste, títulos sem action, linhas finas decorativas sob títulos.

Corrija → re-renderize → re-inspecione. **Nunca declare pronto sem ao menos um ciclo completo de fix-and-verify.**

---

## Princípios Executivos Não-Negociáveis

Inspirados na skill oficial Anthropic `pptx` e no consulting playbook:

1. **Uma ideia por slide.** Se precisar de "e", provavelmente são dois slides.
2. **Action titles em TODOS os slides** (exceto capa e divisores). Sem exceção.
3. **Fonte de dados em todo gráfico/número.** `Fonte: ...` em 9-10pt muted.
4. **Cada slide precisa de um elemento visual** — ícone, chart, imagem, shape. Deck só-texto é descartável.
5. **Paleta content-informed**: se ao trocar as cores por outra apresentação o deck ainda "funciona", as cores são genéricas demais.
6. **Dominância, não igualdade**: uma cor domina 60-70%, outra 20-30%, acento em 5-10%.
7. **Número-destaque em 60-72pt**, label em 10-12pt muted abaixo.
8. **Respiro**: margens mínimas de 0.5"; 0.3-0.5" entre blocos; nunca preencha cada polegada.
9. **Sem bullets longos**: se uma linha passa de ~12 palavras, reescreva ou vire chart.
10. **NUNCA use linhas finas decorativas sob títulos** — é a marca registrada de slides gerados por IA.

---

## Avoid (Vícios Comuns de Deck Corporativo)

- ❌ Slide de agenda com 7 tópicos idênticos — vire um visual de capítulos
- ❌ "Sobre nós" no slide 3 num deck para quem já te conhece
- ❌ Títulos tópico-formais ("Resultados", "Mercado", "Time") em vez de action titles
- ❌ Tabelas gigantes copiadas do Excel — extraia o insight, mostre gráfico
- ❌ Clipart e ícones genéricos do PowerPoint — use Lucide/Feather/Phosphor ou pictogramas próprios
- ❌ Gradiente azul padrão do PowerPoint
- ❌ Rodapé com logo + página + data + título do deck ocupando 8% da altura em todo slide
- ❌ Bullets aninhados em 3 níveis — quebra hierarquia visual

---

## Arquivos de Referência

- [intake.md](intake.md) — gatilhos e entrevista antes de gerar
- [SETUP-TRABALHO.md](SETUP-TRABALHO.md) — clone, venv, marca no Mac do trabalho
- [narrative.md](narrative.md) — método de estruturação (Minto, SCQA, action titles)
- [STYLE_PRESETS.md](STYLE_PRESETS.md) — presets, viewport, densidade, brand mode
- [visual-design.md](visual-design.md) — paletas, tipografia, layouts, QA visual
- [profiles.md](profiles.md) — perfis corporate/startup/consulting
- [examples.md](examples.md) — slides de referência por layout
- [brand/README.md](brand/README.md) — logos, imagens, `brand.json`, exemplos JSON
- [ds-reference-superapp-fintech-br.md](ds-reference-superapp-fintech-br.md) — DS inspiracional anônimo (cores + layout)
- [scripts/render_html.py](scripts/render_html.py) — gerador HTML
- [scripts/export_pdf.py](scripts/export_pdf.py) — export PDF
- [scripts/preview_styles.py](scripts/preview_styles.py) — previews de preset
- [scripts/generate_pptx.py](scripts/generate_pptx.py) — gerador python-pptx (opcional)
- [scripts/requirements.txt](scripts/requirements.txt) — dependências Python
