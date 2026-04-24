# DS de referência — banco digital (BR, anônimo)

Referência **inspiracional** para alinhar paleta, hierarquia e ritmo visual a um padrão comum de produtos financeiros digitais no Brasil (super-app, conta digital, blog institucional). Uso interno na skill.

**Regras:** não nomear instituições, concorrentes ou marcas de terceiros em materiais finais do usuário. Este arquivo descreve apenas **papéis de cor**, **layout** e **tipografia** genéricos. Quando existir guia corporativo oficial, ele **substitui** tudo abaixo.

---

## Papéis de cor (hex sem `#`, prontos para `brand.json`)

Valores escolhidos para contraste legível em títulos escuros sobre fundo claro e CTA laranja visível sem “estourar” em projeção.

| Papel | Hex sugerido | Uso |
|--------|----------------|-----|
| `primary` | `1A1A1A` | Texto principal, ícones fortes, números |
| `primary_dark` | `0D0D0D` | Faixas de cabeçalho, hero escuro opcional |
| `accent` | `FF7A00` | CTA, destaque em gráficos, kicker em marca clara |
| `secondary` | `E8F5E9` | Faixas suaves, “sucesso” / contexto positivo (verde muito claro) |
| `surface` | `F7F7F5` | Fundo de slide / cartão |
| `text_dark` | `1A1A1A` | Corpo (igual primary ou levemente mais suave) |
| `muted` | `6B7280` | Legendas, fonte, meta |
| `on_dark` | `FFFFFF` | Texto sobre `primary_dark` |

**Segundo destaque (opcional):** para badges “ok”, selos ou série secundária em gráfico, use verde médio **`22C55E`** como cor de ilustração — no `brand.json` atual não há campo dedicado; use `secondary` com tom verde (como acima) ou trate no copy/visual como cor de ícone pontual sem alterar o schema.

---

## Formato e layout (padrões de UI)

- **Hero:** headline curta (uma ideia), subtítulo explicativo, um bloco visual forte (imagem ou número). No deck: layouts `title`, `chapter`, `hero_split`.
- **Cartões:** cantos arredondados, sombra leve, bastante respiro; conteúdo em camadas (título > corpo > meta). No deck: `scqa_story`, `kpi_callout`, partes de `two_column`.
- **Grade de benefícios:** 3 colunas ou lista curta com ícone/acento. No deck: `kpi_callout`, bullets com `▸` já usados nos templates.
- **Editorial tipo blog:** data + categoria + título; no deck: `kicker`, `source`, action titles como manchete.

---

## Tipografia (direção)

- **Display / títulos:** sans geométrica ou humanista condensada (personalidade “app”: confiante, legível em tamanho grande). Proxies no ecossistema web: famílias próximas a **Archivo**, **Plus Jakarta Sans**, **Manrope** — já alinhadas aos presets da skill (`swiss_modern`, etc.).
- **Corpo:** sans neutra de alta legibilidade (**Nunito Sans**, **Source Sans 3**, ou stack sans neutra do guia corporativo).
- **Escala:** manter `clamp()` e limites de densidade em [STYLE_PRESETS.md](STYLE_PRESETS.md).

---

## Mapeamento papel DS → `brand.json` / preset HTML

| Papel DS | Campo `brand.json` | Notas |
|-----------|-------------------|--------|
| Texto principal / números | `primary`, `text_dark` | Podem ser o mesmo tom |
| Faixa superior escura | `primary_dark` | Slide `theme-band` |
| CTA / destaque | `accent` | KPIs, gráficos, kicker |
| Fundo suave / cartão | `surface`, `secondary` | `secondary` com viés verde opcional |
| Legendas | `muted` | `source`, labels |
| Texto em faixa escura | `on_dark` | Contraste sobre `primary_dark` |

**Preset HTML sugerido:** `swiss_modern` para fundo claro + acento laranja forte; `bold_signal` se o deck for majoritariamente escuro e quiser o mesmo laranja como energia. Sempre `brand_mode: "strict"` quando preencher `brand` com esta paleta.

**Gatilho no chat:** se o usuário pedir “estilo super-app BR” ou equivalente, o agente: lê este arquivo → propõe o bloco `brand` acima (ou grava em `brand/brand.json`) → segue [intake.md](intake.md) antes de gerar arquivos.

---

## Checklist rápido

- [ ] Uma cor domina o fundo (claro); laranja só onde precisa de ação ou destaque.
- [ ] Verde só em **apoio** (sucesso, contexto positivo), não competir com o laranja.
- [ ] Action titles curtos, estilo manchete; `source` em todo dado.
