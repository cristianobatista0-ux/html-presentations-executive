# Narrativa Executiva

Método de estruturação ANTES de qualquer design. Aplique na ordem: BLUF → Pyramid → SCQA → Action Titles → Ghost Deck.

---

## 1. BLUF — Bottom Line Up Front

Uma frase. Começa com verbo de decisão. Contém número.

**Template:**

> [Recomendamos / Propomos / Concluímos] [ação específica] — [número-âncora] e [benefício quantificado em horizonte de tempo].

**Bons:**

- "Recomendamos encerrar a operação de B2C na Europa — economiza R$ 14M/ano e libera o time para dobrar B2B em 2026."
- "Propomos elevar o preço da camada Pro em 18% — +R$ 9M ARR com churn projetado de apenas 2.1pp."

**Ruins:**

- "Vamos discutir a estratégia europeia" (não é decisão)
- "Os resultados foram positivos" (sem número, sem ação)

O BLUF é o slide 1 do corpo (após a capa) e reaparece no slide de fechamento.

---

## 2. Pirâmide de Minto

Toda apresentação executiva tem **uma ideia governante** sustentada por **3 (raramente 4) argumentos**, cada um com evidências.

```
              [IDEIA GOVERNANTE = BLUF]
                        |
       ┌────────────────┼────────────────┐
  [Argumento 1]    [Argumento 2]    [Argumento 3]
     |                |                |
  evid/dado        evid/dado        evid/dado
  evid/dado        evid/dado        evid/dado
```

Regras:

- Os argumentos devem ser **MECE**: Mutuamente Exclusivos, Coletivamente Exaustivos.
- Cada argumento vira **1 slide** (às vezes 2) no corpo.
- Ordenar argumentos por **força decrescente** ou por **sequência lógica** (causa → efeito → ação).

**Exemplo — tese de expansão Sul:**

Governante: *"Recomendamos R$ 18M capex para abrir CD em Curitiba"*

1. Demanda existe e está mal atendida *(crescimento 48%, SLA caiu p/ 72%)*
2. Economia operacional sustenta o payback *(frete -31%, NPS +14pt — benchmark Norte)*
3. Janela é agora *(terreno 18% abaixo da média; concorrente entra em 2027)*

---

## 3. SCQA — abertura que prende atenção

Use nos primeiros 2-3 slides (após capa) para contextualizar a decisão:

- **S**ituation — onde estamos hoje (fato conhecido e aceito)
- **C**omplication — o que mudou ou está em risco
- **Q**uestion — a pergunta implícita que força a reunião
- **A**nswer — o BLUF

**Exemplo (1 slide por linha, ou todos em um):**

- **S**: Fulfillment Sul hoje é 100% 3PL, atende 18% do GMV.
- **C**: Demanda cresceu 48% YoY mas SLA caiu de 94% para 72% — NPS despencou 21pt.
- **Q**: Seguimos com 3PL ou verticalizamos?
- **A**: Verticalizamos. R$ 18M capex. Payback 22 meses.

Depois disso vêm os argumentos da Pyramid.

---

## 4. Action Titles

**Regra de ouro:** o título de cada slide é uma **frase completa** que comunica a **conclusão** daquele slide.

Se o leitor ler **só os títulos**, ele deve conseguir reconstruir a história inteira.

### Diagnóstico rápido

Antes de ir para o design, leia apenas os títulos em sequência. Pergunta-teste:

> "Alguém que leu só os títulos sairia com a mesma conclusão do BLUF?"

Se não, reescreva os títulos.

### Exemplos comparados

| Tópico (❌ evite) | Action title (✅ faça) |
|---|---|
| "Receita por região" | "Latam já representa 41% da receita — motor de crescimento em 2025" |
| "Análise de churn" | "Churn caiu 34% após CS proativo — resultado replicável em enterprise" |
| "Cenários financeiros" | "Cenário base entrega R$ 52M em 3 anos; cenário conservador ainda paga o capex" |
| "Concorrência" | "Concorrente X entra no Sul em 2027 — janela fecha em 9 meses" |
| "Próximos passos" | "Aprovação do board destrava compra do terreno em 30 dias" |

### Anatomia do action title

- **Verbo forte** (cresceu, caiu, dobrou, concentra, responde, supera)
- **Sujeito específico** (Latam, enterprise, Sul, não "o negócio")
- **Número** (sempre que possível)
- **Consequência** (por isso importa)

Se couber em ~12-16 palavras, melhor. Se passar de 20, quebre em duas linhas ou reescreva.

---

## 5. Ghost Deck (wireframe textual)

Antes de gerar o `.pptx`, monte o ghost deck em Markdown ou texto. É o rascunho sem design.

```
01. [CAPA] Expansão Fulfillment Sul — Board Apr/2026

02. [SUMMARY] Recomendamos R$ 18M capex para CD em Curitiba — payback 22m, +R$ 52M GMV em 3 anos
    • Demanda do Sul cresceu 48% YoY; SLA caiu p/ 72%
    • CD próprio: frete -31%, NPS +14pt (benchmark Norte)
    • Janela ótima: terreno 18% abaixo da média; concorrente entra em 2027

03. [SCQA] Hoje 3PL atende 18% do GMV — e a equação quebrou em 2025

04. [KPI CALLOUT] Três números sustentam a tese
    48% crescimento demanda | -31% frete | 22 meses payback

05. [CHART] Demanda cresceu 48% mas SLA despencou — gap operacional em 2025
    (gráfico duplo-eixo: demanda + SLA por trimestre)

06. [COMPARISON] CD próprio supera 3PL em 4 das 5 dimensões
    (3PL | CD próprio: custo, SLA, NPS, controle, capex)

07. [TIMELINE] Em 9 meses operamos; em 22 pagamos
    (milestones: terreno → obra → ramp → break-even)

08. [CHART] Cenário base: +R$ 52M GMV; conservador ainda paga o capex
    (3 cenários lado a lado)

09. [IMAGE_RIGHT] Janela fecha em 2027 quando concorrente X entra no Sul

10. [CLOSING] Aprovação do board destrava compra do terreno em 30 dias
    Próximos passos + ask explícito
```

Validação do ghost deck:

- [ ] Todo título (exceto capa) é action title?
- [ ] Lendo só os títulos, a história fecha?
- [ ] Cada slide entrega UMA ideia?
- [ ] O ask/decisão está explícito no final?
- [ ] Número de slides compatível com a duração? (regra: 1 slide por 2-3 min)

Só depois que o ghost deck passa nesse check, vá para [visual-design.md](visual-design.md).

---

## 6. Padrões de Fechamento

O último slide **nunca** é "Obrigado" ou "Dúvidas?". Use uma destas variações:

- **The Ask**: repete o BLUF como decisão solicitada + próximos 3 passos com dono e data.
- **Decision Matrix**: opções → recomendada destacada → trade-offs.
- **Commitment**: o que o proponente se compromete a entregar se aprovado.

---

## 7. Variações por Tipo de Deck

| Tipo | Estrutura recomendada |
|---|---|
| **Board / C-level** | BLUF → SCQA curto → 3 argumentos → cenários financeiros → ask |
| **Investor / Pitch** | Problema → Solução → Mercado → Tração → Modelo → Time → Ask |
| **QBR** | Compromissos anteriores → Resultados vs. plano → 3 learnings → Plano próximo Q |
| **Steering / Projeto** | Status (RAG) → Riscos → Decisões pendentes → Próximo checkpoint |
| **Estratégia anual** | Onde estamos → Aonde vamos → Como chegamos → Primeiros 90 dias |

Detalhes por perfil em [profiles.md](profiles.md).
