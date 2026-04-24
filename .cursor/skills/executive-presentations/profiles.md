# Perfis Executivos

Cada deck tem um tom. Escolha um perfil **uma vez** e mantenha consistente.

O campo `profile` no `deck.json` aciona defaults do script (paleta + tipografia + layouts padrão).

---

## 1. `corporate` — Board, Conselho, C-Level, Diretoria

**Quando usar:** board meeting, steering corporativo, conselho, apresentação a diretoria tradicional, resultado trimestral, request de capex, turnaround.

**Audiência espera:** sobriedade, precisão, riscos explicitados, fontes, números ancorados.

**Defaults:**

- **Paleta**: `midnight_executive` (navy + ice + white) ou `charcoal_minimal`
- **Tipografia**: Georgia (header) + Calibri (body) OU Cambria + Calibri
- **Estrutura**: BLUF → SCQA → 3 argumentos → cenários (base/conservador/otimista) → riscos → ask
- **Número de slides**: 8-14 (decks mais curtos = mais poder)
- **Densidade**: média. Action titles fortes; 3 bullets por slide no máximo.
- **Motivo visual**: número de slide discreto no canto + borda esquerda 3pt na cor acento em cards
- **Imagens**: fotos B&W com tint navy, ou ícones Phosphor light em círculos navy ⌀ 40pt

**Tons e palavras:**

- Preferir: "Recomendamos", "Propomos", "Concluímos", "Payback", "Risco materializado", "Evidência", "Baseline"
- Evitar: "Incrível", "Revolucionário", "Disruptivo", "Game-changer", "Next-level"

**Template de ask (slide final):**

```
ASK (1 linha, verbo forte)
├── Decisão solicitada: [aprovar capex R$ 18M / autorizar início / ...]
├── Próximos 3 passos:
│   1. [ação] — [dono] — [data]
│   2. ...
└── Próxima revisão: [checkpoint e data]
```

---

## 2. `startup` — Pitch, Investidores, Demo Day, All-Hands

**Quando usar:** pitch deck para VC, demo day, seed/Series A/B, all-hands da empresa, keynote em evento, lançamento.

**Audiência espera:** energia, visão grande, tração provada, time forte, clareza de modelo.

**Defaults:**

- **Paleta**: `coral_energy`, `ocean_gradient` ou paleta customizada da marca
- **Tipografia**: Inter Bold ou Arial Black (header) + Inter (body); ou Playfair Display + Inter
- **Estrutura** (Sequoia-style, 10-12 slides):
  1. **Purpose** — uma frase de missão
  2. **Problem** — dor real, quantificada
  3. **Solution** — como você resolve (com demo/screenshot)
  4. **Why now** — janela de mercado
  5. **Market size** — TAM/SAM/SOM com fonte
  6. **Product** — diferencial técnico
  7. **Business model** — como ganha dinheiro
  8. **Traction** — números que já existem (MRR, clientes, crescimento)
  9. **Competition** — matriz 2x2 ou tabela
  10. **Team** — por que este time
  11. **Financials / Plan** — 18 meses à frente
  12. **The ask** — $ + what for + milestones
- **Densidade**: baixa. Um número gigante, uma ideia, uma imagem.
- **Motivo visual**: full-bleed images + números gigantes 80-120pt em slides de tração

**Tons e palavras:**

- Permitido: "Dobramos", "10x", "Primeiro a", "Único", "Tração" (se tiver tração real)
- Evitar ainda: jargão vazio ("leveraging synergies", "world-class", "best-in-class")
- **Números honestos**. Investidor detecta infla em 3s.

**Slide de tração — template:**

```
[Action title: "Dobramos MRR em 4 meses com CAC de 1/3 do setor"]

[Número gigante 120pt: $42k MRR]   [Gráfico de crescimento à direita]
[Label: +127% MoM média]

[3 KPIs secundários em linha: Clientes | CAC | Payback]

Fonte: Stripe, jan-abr/2026.
```

---

## 3. `consulting` — McKinsey / BCG / Bain style

**Quando usar:** entrega a cliente de consultoria, steering de projeto de transformação, ghost deck de diagnóstico, síntese de workstream.

**Audiência espera:** estrutura MECE impecável, Minto Pyramid explícita, disciplina de exhibits, zero desperdício.

**Defaults:**

- **Paleta**: `charcoal_minimal` (charcoal + off-white + black accent) ou firm-branded
- **Tipografia**: Arial (header + body, pesos diferentes) OU Georgia + Arial
- **Estrutura**: Executive Summary de **1 página** (Minto completo) → deep-dive por argumento → appendix (fontes e metodologia)
- **Densidade**: alta. Exhibits densos são aceitos quando o action title extrai a conclusão.
- **Motivo visual**: numeração rigorosa de exhibits ("Exhibit 1 of 18") no canto inferior; fonte obrigatória em cada slide.

**Regras não-negociáveis consulting-style:**

1. **Action title na primeira pessoa do plural** ou na 3ª impessoal: "Reduzimos custo em 23%" / "Custo cai 23% com o redesenho do processo"
2. **Todo exhibit tem:**
   - Action title (topo)
   - Exhibit label + número (canto superior esquerdo, pequeno)
   - Fonte (rodapé direito, 9pt muted)
   - Nota metodológica se aplicável (rodapé esquerdo, 8-9pt)
3. **MECE**: argumentos e sub-argumentos são mutuamente exclusivos e coletivamente exaustivos. Declare isso no slide de estrutura.
4. **Sem "coisas bonitinhas"**. Nenhum ícone decorativo que não comunique informação. Nenhum gradient desnecessário.
5. **Appendix numerado**: A.1, A.2, A.3 — acessível mas não no flow principal.

**Template de sumário executivo (1 slide tudo):**

```
[Action title da recomendação — 1 linha]

Situation:     [1 frase contexto]
Complication:  [1 frase o que mudou]
Question:      [1 pergunta]
Answer:        [BLUF]

Três razões sustentam a recomendação:
  1. [argumento 1 — 1 linha + métrica]
  2. [argumento 2 — 1 linha + métrica]
  3. [argumento 3 — 1 linha + métrica]

Próximos passos: [3 passos one-liner]
```

Esse slide deve **caber em 1 página** legível a 3 metros. Se não cabe, o pensamento ainda não está pronto.

---

## 4. Matriz de Escolha Rápida

| Situação | Perfil |
|---|---|
| "Preciso apresentar para o board semana que vem" | `corporate` |
| "Quero pitch para investidores" | `startup` |
| "Deck de diagnóstico para o cliente" | `consulting` |
| "QBR da área" | `corporate` (mais leve) |
| "Demo day em 3 min" | `startup` |
| "All-hands da empresa" | `startup` |
| "Resultado trimestral financeiro" | `corporate` |
| "Entrega final de projeto de transformação" | `consulting` |
| "Comitê de investimentos" | `corporate` |
| "Keynote em evento" | `startup` |

---

## 5. Mistura é OK, mas declare

Decks híbridos acontecem (ex.: startup apresentando resultados ao próprio board). Nesse caso escolha **o perfil do leitor**, não do apresentador. Board de startup → `corporate`. Conselho de startup → `corporate`. Pitch para próximo round → `startup`.

Se verdadeiramente híbrido, escolha **um perfil** para identidade visual e **aplique rigor de narrativa do outro**. Ex.: visual `startup` + estrutura `consulting` = pitch deck com SCQA explícito.
