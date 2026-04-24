# Exemplos — um por layout

Exemplos concretos de slides executivos bem executados. Use como referência para o campo `layout` no `deck.json`.

**Novos (visual editorial):** `chapter` (capítulo + gancho + foto), `scqa_story` (quatro cartões S/C/Q/A), `hero_split` (número gigante + bullets + foto). Ver deck completo [`brand/examples/board_expansao.json`](brand/examples/board_expansao.json).

### HTML + preset + marca (raiz do `deck.json`)

O mesmo `deck.json` alimenta `render_html.py` e (opcional) `generate_pptx.py`. Para o HTML, defina **preset** e **brand_mode**:

```json
{
  "title": "Reunião semanal — Inadimplência",
  "profile": "corporate",
  "preset": "swiss_modern",
  "brand_mode": "strict",
  "brand": {
    "primary": "0B3D5C",
    "primary_dark": "051F30",
    "accent": "E8941E",
    "surface": "F2F6FA",
    "text_dark": "14232E",
    "muted": "5A6B78",
    "on_dark": "FFFFFF"
  },
  "slides": []
}
```

Geração: `python scripts/render_html.py brand/examples/board_expansao.json /caminho/absoluto/saida.html` (caminho **absoluto** no `.html` facilita resolver `image_path` relativos ao JSON). PDF: `python scripts/export_pdf.py saida.html saida.pdf`.

---

## `title` (capa)

```
[FUNDO NAVY #1E2761, full-bleed]

                EXPANSÃO FULFILLMENT SUL
                (44pt Georgia Bold, ice blue #CADCFC)

            Recomendação de capex R$ 18M — Board Apr/2026
                (18pt Calibri Regular, white 85% opacity)


[Canto inferior esquerdo: logo em white]        [Canto inferior direito: "23 Abr 2026 · CONFIDENTIAL" — 9pt muted]
```

**deck.json:**

```json
{
  "layout": "title",
  "title": "Expansão Fulfillment Sul",
  "subtitle": "Recomendação de capex R$ 18M — Board Apr/2026",
  "date": "23 Abr 2026",
  "confidential": true
}
```

---

## `executive_summary` (BLUF + 3 bullets)

```
[FUNDO OFF-WHITE]

Recomendamos R$ 18M de capex para abrir CD em Curitiba —
payback 22 meses, +R$ 52M GMV em 3 anos
(36pt Georgia Bold, navy)

  ●  Demanda do Sul cresceu 48% YoY; SLA caiu para 72%
  ●  CD próprio reduz frete em 31% e eleva NPS em 14pt (benchmark interno Norte)
  ●  Janela ótima: terreno 18% abaixo da média; concorrente X entra no Sul em 2027

                    (14pt Calibri, bullets em cor acento, texto em navy 90%)


[Borda esquerda 4pt em cor acento ao longo dos 3 bullets — motivo visual repetido]

Fonte: BI interno, jan-dez/2025; research de mercado contratado.          [9pt muted, rodapé esquerdo]
```

**deck.json:**

```json
{
  "layout": "executive_summary",
  "action_title": "Recomendamos R$ 18M de capex para abrir CD em Curitiba — payback 22 meses, +R$ 52M GMV em 3 anos",
  "bullets": [
    "Demanda do Sul cresceu 48% YoY; SLA caiu para 72%",
    "CD próprio reduz frete em 31% e eleva NPS em 14pt (benchmark interno Norte)",
    "Janela ótima: terreno 18% abaixo da média; concorrente X entra no Sul em 2027"
  ],
  "source": "BI interno jan-dez/2025; research de mercado contratado"
}
```

---

## `kpi_callout` (3 números gigantes)

```
[FUNDO OFF-WHITE]

Três indicadores sustentam a tese
(32pt Georgia Bold)


     +48%               22 meses              +R$ 52M
     (72pt navy)        (72pt navy)           (72pt coral — acento)

  Crescimento         Payback               GMV incremental
   de demanda          esperado             em 3 anos (base)
  2025 vs 2024
   (11pt muted)       (11pt muted)          (11pt muted)


Fonte: BI interno; modelo financeiro v2.3.   [9pt rodapé]
```

**deck.json:**

```json
{
  "layout": "kpi_callout",
  "action_title": "Três indicadores sustentam a tese",
  "kpis": [
    {"value": "+48%", "label": "Crescimento de demanda\n2025 vs 2024"},
    {"value": "22 meses", "label": "Payback esperado"},
    {"value": "+R$ 52M", "label": "GMV incremental\nem 3 anos (base)", "highlight": true}
  ],
  "source": "BI interno; modelo financeiro v2.3"
}
```

---

## `two_column` (texto + visual)

```
[FUNDO OFF-WHITE]

CD próprio reduz frete em 31% e elimina dependência operacional
(32pt Georgia Bold)


┌─ Esquerda (texto) ─────────────┐    ┌─ Direita (gráfico) ──────────┐
│                                │    │                              │
│  ●  Frete 3PL: R$ 12,40/pedido │    │    [Barras:                  │
│     → CD próprio: R$ 8,55      │    │      3PL     ████████ R$12,40│
│     (-31%)                     │    │      Próprio ██████ R$8,55]  │
│                                │    │                              │
│  ●  SLA sobe de 72% para 96%   │    │   Destaque: barra "Próprio"  │
│     (target interno 94%)       │    │   em cor acento              │
│                                │    │                              │
│  ●  Dependência técnica do 3PL │    │                              │
│     cai de 100% para 20%       │    │                              │
│     (picos de sazonalidade)    │    │                              │
│                                │    │                              │
└────────────────────────────────┘    └──────────────────────────────┘

Fonte: contrato 3PL 2025; modelo financeiro CD v2.3.       [9pt]
```

**deck.json:**

```json
{
  "layout": "two_column",
  "action_title": "CD próprio reduz frete em 31% e elimina dependência operacional",
  "left_bullets": [
    "Frete 3PL R$ 12,40/pedido → CD próprio R$ 8,55 (-31%)",
    "SLA sobe de 72% para 96% (target interno 94%)",
    "Dependência técnica do 3PL cai de 100% para 20%"
  ],
  "right_visual": {
    "type": "bar",
    "data": [{"label": "3PL", "value": 12.40}, {"label": "Próprio", "value": 8.55, "highlight": true}],
    "unit": "R$/pedido"
  },
  "source": "contrato 3PL 2025; modelo financeiro CD v2.3"
}
```

---

## `chart` (gráfico protagonista)

```
[FUNDO OFF-WHITE]

Demanda cresceu 48% mas SLA despencou — gap operacional em 2025
(32pt Georgia Bold)


    [Gráfico ocupa 75% da área útil, duplo eixo:
     - Barras (eixo esquerdo): demanda trimestral em mil pedidos
     - Linha (eixo direito): SLA % por trimestre

     Anotação: "SLA < meta" em balão sobre Q3 e Q4 2025
     Linha tracejada horizontal em 94% marca a meta interna]

    ──────────────────────────────────────────────────
    Q1'24  Q2'24  Q3'24  Q4'24  Q1'25  Q2'25  Q3'25  Q4'25


Fonte: BI interno, pedidos Sul, jan/2024-dez/2025. Meta SLA = 94%.  [9pt]
```

**deck.json:**

```json
{
  "layout": "chart",
  "action_title": "Demanda cresceu 48% mas SLA despencou — gap operacional em 2025",
  "chart": {
    "type": "combo",
    "x": ["Q1'24","Q2'24","Q3'24","Q4'24","Q1'25","Q2'25","Q3'25","Q4'25"],
    "bars": {"label": "Pedidos (mil)", "values": [42, 48, 51, 62, 68, 74, 82, 92]},
    "line": {"label": "SLA (%)", "values": [96, 95, 94, 92, 88, 82, 76, 72]},
    "annotations": [{"at": "Q3'25", "text": "SLA < meta"}],
    "target_line": {"axis": "line", "value": 94, "label": "Meta"}
  },
  "source": "BI interno, pedidos Sul, jan/2024-dez/2025. Meta SLA = 94%"
}
```

---

## `comparison` (duas ou três alternativas)

```
[FUNDO OFF-WHITE]

CD próprio supera 3PL em 4 das 5 dimensões — único trade-off é capex inicial
(32pt Georgia Bold)


┌─────────────────┬────────────────┬─────────────────────────┐
│                 │   3PL (atual)  │   CD próprio ★ RECOMEND.│   ← header, "recomendado" em acento
├─────────────────┼────────────────┼─────────────────────────┤
│ Custo/pedido    │   R$ 12,40     │   R$ 8,55 (-31%)        │
│ SLA             │   72% atual    │   96% projetado         │
│ NPS             │   64           │   78 (benchmark Norte)  │
│ Controle        │   Baixo        │   Alto                  │
│ Capex inicial   │   R$ 0         │   R$ 18M                │   ← único red, honestidade
└─────────────────┴────────────────┴─────────────────────────┘

Fonte: contrato 3PL atual; modelo CD v2.3; benchmark CD Norte 2024-25.   [9pt]
```

**deck.json:**

```json
{
  "layout": "comparison",
  "action_title": "CD próprio supera 3PL em 4 das 5 dimensões — único trade-off é capex inicial",
  "columns": [
    {"name": "3PL (atual)"},
    {"name": "CD próprio", "recommended": true}
  ],
  "rows": [
    {"dimension": "Custo/pedido", "values": ["R$ 12,40", "R$ 8,55 (-31%)"]},
    {"dimension": "SLA", "values": ["72% atual", "96% projetado"]},
    {"dimension": "NPS", "values": ["64", "78 (benchmark Norte)"]},
    {"dimension": "Controle", "values": ["Baixo", "Alto"]},
    {"dimension": "Capex inicial", "values": ["R$ 0", "R$ 18M"]}
  ]
}
```

---

## `timeline`

```
[FUNDO OFF-WHITE]

Em 9 meses operamos; em 22 pagamos
(32pt Georgia Bold)


Hoje              +3m              +9m                +15m              +22m
 ●━━━━━━━━━━━━━━━━━○━━━━━━━━━━━━━━━━━●━━━━━━━━━━━━━━━━━○━━━━━━━━━━━━━━━━━★
Decisão      Terreno + obra       Operação        Ramp-up completo   Break-even
 Board        fechados             inicia           (capacidade
                                                    nominal)

 (●=ocorrido/aprovado, ○=marco de projeto, ★=financeiro)
```

**deck.json:**

```json
{
  "layout": "timeline",
  "action_title": "Em 9 meses operamos; em 22 pagamos",
  "milestones": [
    {"when": "Hoje", "label": "Decisão Board", "type": "decision"},
    {"when": "+3m", "label": "Terreno + obra fechados", "type": "project"},
    {"when": "+9m", "label": "Operação inicia", "type": "go-live"},
    {"when": "+15m", "label": "Ramp-up completo", "type": "project"},
    {"when": "+22m", "label": "Break-even", "type": "financial", "highlight": true}
  ]
}
```

---

## `image_right` (foto + texto)

```
[FUNDO OFF-WHITE]

┌────────────────────────┬──────────────────────────────┐
│                        │                              │
│  Janela fecha em 2027  │                              │
│  quando concorrente X  │    [FOTO OU ILUSTRAÇÃO       │
│  entra no Sul          │     half-bleed, 45% largura  │
│  (28pt Georgia Bold)   │     B&W com tint navy]       │
│                        │                              │
│  ●  X anunciou obra    │                              │
│     no Paraná em       │                              │
│     Fev/2026           │                              │
│                        │                              │
│  ●  Decisão em Abr vs  │                              │
│     Jul significa -6m  │                              │
│     de vantagem        │                              │
│                        │                              │
│  ●  Custo de esperar:  │                              │
│     R$ 7M em GMV       │                              │
│     perdido            │                              │
│                        │                              │
└────────────────────────┴──────────────────────────────┘
```

**deck.json:**

```json
{
  "layout": "image_right",
  "action_title": "Janela fecha em 2027 quando concorrente X entra no Sul",
  "bullets": [
    "X anunciou obra no Paraná em Fev/2026",
    "Decisão em Abr vs Jul significa -6m de vantagem",
    "Custo de esperar: R$ 7M em GMV perdido"
  ],
  "image_path": "assets/concorrente_map.jpg"
}
```

---

## `closing` (the ask)

```
[FUNDO NAVY, sanduíche fecha dark como capa]

                        APROVAÇÃO DO BOARD
            destrava compra do terreno em 30 dias
                  (36pt Georgia Bold, ice blue)


          Próximos 3 passos
          (14pt white, 70% opacity)

          1.  Aprovar capex R$ 18M       —  Board        —  Hoje
          2.  Fechar compra do terreno   —  CFO + Legal  —  30 dias
          3.  Iniciar obras              —  COO          —  60 dias

          (12pt white regular; 3 colunas: ação | dono | prazo)


          Próxima revisão: Board Jul/2026    [9pt muted]
```

**deck.json:**

```json
{
  "layout": "closing",
  "action_title": "Aprovação do Board destrava compra do terreno em 30 dias",
  "next_steps": [
    {"action": "Aprovar capex R$ 18M", "owner": "Board", "due": "Hoje"},
    {"action": "Fechar compra do terreno", "owner": "CFO + Legal", "due": "30 dias"},
    {"action": "Iniciar obras", "owner": "COO", "due": "60 dias"}
  ],
  "next_review": "Board Jul/2026"
}
```

---

## Deck Completo de Referência (ghost deck)

Para a tese de expansão Fulfillment Sul, o deck completo ficaria em **10 slides**:

1. `title` — capa
2. `executive_summary` — BLUF + 3 bullets (o slide mais importante do deck)
3. `two_column` — SCQA (texto à esquerda, gráfico de contexto à direita)
4. `kpi_callout` — 3 números âncora
5. `chart` — Demanda vs SLA (argumento 1)
6. `comparison` — 3PL vs CD (argumento 2)
7. `chart` — Cenários financeiros (argumento 3)
8. `timeline` — Jornada 22 meses
9. `image_right` — Janela competitiva
10. `closing` — The ask
