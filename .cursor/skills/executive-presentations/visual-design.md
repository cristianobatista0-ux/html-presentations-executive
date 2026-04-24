# Visual Design

Baseado na skill oficial Anthropic `pptx` e em princípios de design editorial e editorial-executivo. Aplique **depois** de fechar o ghost deck (ver [narrative.md](narrative.md)).

---

## 0. HTML primeiro — presets e brand mode

O **caminho recomendado** para harmonia visual é o render web (`scripts/render_html.py`): tipografia Google por **preset**, layout responsivo com `clamp()`, um slide = uma viewport.

- **Catálogo e regras:** [STYLE_PRESETS.md](STYLE_PRESETS.md) (viewport obrigatório, densidade, mood → preset, lista de stubs).
- **No `deck.json` (raiz):**
  - `"preset"`: `swiss_modern` | `bold_signal` | `dark_botanical` | `paper_ink` | … (stubs redirecionam).
  - `"brand_mode"`: `strict` (padrão se existir `brand`) aplica **cores** do guia sobre o preset e mantém **fontes do preset**; `accent_only` só troca o acento; `off` ignora marca no HTML.
- **QA HTML:** testar nos tamanhos **1920×1080**, **1280×720**, **768×1024**, **375×667**, **667×375** — sem scroll dentro do slide, contraste e imagens contidas.
- **DS inspiracional anônimo (super-app fintech BR):** [ds-reference-superapp-fintech-br.md](ds-reference-superapp-fintech-br.md) — papéis de cor e layout **sem** nome de marca; use até chegar o guia oficial.

O `.pptx` continua documentado abaixo para quando o entregável for obrigatoriamente PowerPoint.

---

## 1. Identidade da marca no `generate_pptx.py` (e no mesmo `deck.json` do HTML)

Para levar o deck ao trabalho com **paleta oficial**, use no JSON raiz:

- **`brand`**: objeto com hex **sem `#`** — `primary`, `primary_dark`, `secondary`, `accent`, `surface`, `text_dark`, `muted`, `on_dark`, opcionalmente `header_font`, `body_font`, `logo_path`.
- **`brand_path`**: caminho para um `brand.json` (mesmo schema) — útil para um arquivo único compartilhado pelo time.

Exemplo completo: [scripts/brand.example.json](scripts/brand.example.json).

**Imagens:** em cada slide, `image_path` relativo à **pasta do `deck.json`** (o script expande antes de renderizar). Para URL pública, use `image_url` + flag `--fetch-images` (baixa para cache temporário).

**Layouts “editoriais”** (evitam cara de template padrão):

| Layout | Efeito visual |
|--------|----------------|
| `title` | Painel `primary_dark` à esquerda + faixa `accent` + foto hero à direita |
| `chapter` | Capítulo numerado gigante + gancho + foto / colagem |
| `scqa_story` | Quatro cartões arredondados (S, C, Q, A) sobre `surface` |
| `hero_split` | Número-destaque + bullets à esquerda; foto full-height à direita |
| Demais | Faixa superior `primary_dark` + `kicker` em caixa alta + `action_title` |

Se não houver arquivo de imagem, o gerador desenha uma **colagem geométrica (*bento*)** nas cores da marca — ainda conta como elemento visual, mas **foto real** quase sempre vence.

---

## 2. Antes de Começar — Decisões de Identidade

Feche estas 4 decisões de uma vez, no começo, e **não mude no meio do deck**:

1. **Paleta content-informed** (seção 2)
2. **Dominância** (uma cor 60-70%, outra 20-30%, acento 5-10%)
3. **Sanduíche claro/escuro** (capa e fecho escuros, miolo claro) OU **dark premium** no deck todo
4. **Motivo visual único** repetido em todo o deck (um e apenas um — ver seção 5)

---

## 3. Paletas (content-informed)

Nunca use "azul corporativo padrão". Escolha uma paleta que **combine com o tema** do deck. Lista testada (hex):

| Nome | Primária (60-70%) | Secundária (20-30%) | Acento (5-10%) | Indicada para |
|---|---|---|---|---|
| **Midnight Executive** | `#1E2761` navy | `#CADCFC` ice | `#FFFFFF` white | Board, C-level, conselho |
| **Charcoal Minimal** | `#36454F` charcoal | `#F2F2F2` off-white | `#212121` black | Resultados financeiros, sobriedade |
| **Forest & Moss** | `#2C5F2D` forest | `#97BC62` moss | `#F5F5F5` cream | ESG, sustentabilidade, agro |
| **Warm Terracotta** | `#B85042` terracotta | `#E7E8D1` sand | `#A7BEAE` sage | Consumer, varejo, marca |
| **Ocean Gradient** | `#065A82` deep blue | `#1C7293` teal | `#21295C` midnight | Tech enterprise, fintech |
| **Coral Energy** | `#F96167` coral | `#F9E795` gold | `#2F3C7E` navy | Startup, pitch, energia |
| **Berry & Cream** | `#6D2E46` berry | `#A26769` dusty rose | `#ECE2D0` cream | Beauty, lifestyle, hospitality |
| **Teal Trust** | `#028090` teal | `#00A896` seafoam | `#02C39A` mint | Healthtech, bem-estar |
| **Cherry Bold** | `#990011` cherry | `#FCF6F5` off-white | `#2F3C7E` navy | Urgência, crise, turnaround |
| **Sage Calm** | `#84B59F` sage | `#69A297` eucalyptus | `#50808E` slate | Wellness, educação |

Regra de teste: se ao trocar sua paleta por outra o deck continua "funcionando", você escolheu cores genéricas demais. Torne-as específicas ao tema.

---

## 4. Tipografia

### Pairings recomendados

Escolha um header com personalidade + um body neutro:

| Header | Body | Mood |
|---|---|---|
| **Georgia** | Calibri | Editorial executivo |
| **Cambria** | Calibri | Tradicional sóbrio |
| **Arial Black** | Arial | Bold, startup |
| **Trebuchet MS** | Calibri | Moderno amigável |
| **Impact** | Arial | Pitch agressivo |
| **Palatino** | Garamond | Clássico premium |
| **Consolas** | Calibri | Tech, data |
| **Inter** (se disponível) | Inter | Neutro moderno |
| **Playfair Display** (se disponível) | Inter | Luxo editorial |

Evite Arial + Arial. Evite Times New Roman. Evite Comic Sans (óbvio).

### Escala tipográfica (pt)

| Elemento | Tamanho | Peso |
|---|---|---|
| Slide title (action title) | 28-36 | Bold |
| Seção / header interno | 20-24 | Bold |
| Corpo / bullets | 14-16 | Regular |
| Caption / fonte | 9-10 | Regular muted |
| **Número destaque (KPI)** | **60-72** | Bold |
| Label de KPI | 10-12 | Regular muted |

Contraste mínimo entre título e corpo: **2x** de diferença (36 vs 16 funciona, 28 vs 24 não).

### Quebras e comprimento

- Action title idealmente em 1-2 linhas, máximo 16 palavras.
- Bullets: 1 linha. Se passar, reescreva ou vire gráfico.
- Corpo sem hifenização; alinhamento à esquerda (centralizar só em títulos e callouts).

---

## 5. Layouts (templates de slide)

Estes 9 layouts são suficientes para 95% dos decks executivos. O `scripts/generate_pptx.py` implementa todos.

### 4.1 `title` (capa)

- Fundo cor primária (dark).
- Título em 44-54pt, font header, cor acento.
- Subtítulo em 16-20pt muted.
- Logo no canto; data discreta no rodapé.

### 4.2 `executive_summary`

- Action title no topo (28-36pt).
- 3 bullets fortes (14-16pt) — idealmente paralelos sintaticamente (todos começam com verbo).
- Espaço em branco generoso à direita OU ícone vertical de motivo visual.

### 4.3 `kpi_callout`

- Action title no topo.
- 3 colunas com números gigantes (60-72pt) + label (10-12pt muted).
- Fonte de dados no rodapé.

### 4.4 `two_column`

- Action title no topo.
- Esquerda: texto (bullets curtos ou parágrafo de 2-3 linhas).
- Direita: chart, imagem, ou gráfico simples.

### 4.5 `chart`

- Action title deve comunicar a **conclusão do gráfico**, não o nome dele.
- Gráfico ocupa 70-80% da área útil.
- 1 destaque no gráfico (barra em cor acento, linha anotada com callout).
- Fonte obrigatória em 9-10pt.

### 4.6 `image_right`

- Imagem/ilustração ocupa ~45% à direita (half-bleed ok).
- Texto à esquerda: action title + 2-3 bullets OU parágrafo curto.

### 4.7 `comparison`

- Duas (ou três) colunas comparando alternativas.
- Header de cada coluna com nome + label ("Recomendado" em cor acento).
- Dimensões em linhas; check/x ou números por célula.

### 4.8 `timeline`

- Linha horizontal com 4-6 marcos.
- Cada marco: mês/ano + label curto + ícone pequeno.
- Cor acento no marco "hoje" ou "decisão".

### 4.9 `closing`

- Repete o BLUF como Ask no topo.
- 3 próximos passos (owner + data).
- Ou uma "decision slide" com checkbox visual de aprovação.

---

## 6. Motivo Visual Único

**Comprometa-se com UM elemento distintivo** e repita em todo slide:

- Ícones dentro de círculos coloridos do tamanho constante (ex.: ⌀ 40pt)
- Frames arredondados para imagens (radius constante)
- Borda espessa em um único lado dos cards (ex.: 4pt na borda esquerda na cor acento)
- Número do slide em canto fixo com tipografia marcante
- Linha horizontal fina entre header e conteúdo (sob o action title — EVITE, vira vício de IA)
  ↑ Se usar linha, use só 1 vez como divisor de capítulo, nunca sob cada título.

**Regra:** escolha UM. Dois motivos = zero motivo.

---

## 7. Data Viz — Gráficos em Decks Executivos

Regras condensadas (adaptado de Tufte, Few, Storytelling with Data):

- **1 mensagem por gráfico.** O action title é essa mensagem.
- **Destaque em cor acento** apenas na barra/linha/ponto que importa; o resto em cinza/muted.
- **Remova grid, bordas, fundo, 3D, sombras.** Menos tinta, mais dado.
- **Label direto no gráfico** em vez de legenda separada (quando 1-3 séries).
- **Eixo Y começa em 0** para gráficos de barras; pode não começar em linhas se a variação for sutil (mas avise no título).
- **Anotação com flecha** para apontar o insight no próprio chart.
- **Use % e unidades explícitas** em cada número.
- **Fonte**: `Fonte: [nome do sistema], [período]. n=[tamanho amostra se aplicável].`

Tipos e quando usar:

| Tipo | Quando usar |
|---|---|
| Barras horizontais | Ranking de categorias |
| Barras verticais | Evolução temporal com poucos períodos |
| Linhas | Evolução temporal com muitos períodos |
| Área empilhada | Composição que soma 100% ao longo do tempo |
| Dot plot / lollipop | Comparação de poucos pontos (evita barras 3D) |
| Waterfall | Decomposição de variação (útil em P&L) |
| Slope chart | Before/After em duas dimensões |

**Evite**: pizza com mais de 3 fatias, donut decorativo, 3D, gauge, "radar" de skills.

---

## 8. Ícones e Ilustrações

- **Lucide, Feather, Phosphor, Heroicons** — sempre um destes, nunca misturar.
- Tamanho padrão no deck todo (24, 32 ou 40pt; escolha UM).
- Mesma grossura de traço.
- Cor do ícone = cor acento OU cor do texto ao lado (nunca 2 cores dentro do mesmo ícone).
- **Nunca emojis** em deck executivo corporativo (pode em pitch de startup, com parcimônia).

Ilustrações: prefira fotos de alta qualidade B&W com um tint da paleta, ou ilustrações vetoriais minimalistas. Evite clip art do PowerPoint a todo custo.

---

## 9. Spacing (o detalhe que separa profi de amador)

- **Margens mínimas do slide**: 0.5" (~1.27cm) em todos os lados.
- **Gap entre blocos**: escolha 0.3" OU 0.5" — use consistente.
- **Padding interno de cards**: 0.2"-0.3".
- **Nunca** deixe um bloco a menos de 0.5" da margem.
- **Baseline grid**: alinhe topos de blocos horizontalmente entre slides consecutivos (sensação de ordem).

Respire. **Espaço em branco é um elemento de design**, não desperdício.

---

## 10. QA Visual Obrigatório

**Assuma que há problemas.** Se encontrou zero no primeiro passe, não olhou direito.

### 9.1 Conteúdo

```bash
python -m markitdown output.pptx
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|placeholder|tbd|todo|\[.*\]"
```

Checks:
- [ ] Nenhum placeholder sobrou
- [ ] Action titles em todos os slides não-capa
- [ ] Todo número tem fonte
- [ ] Nomes próprios e siglas corretos

### 9.2 Visual — Render e inspeção

```bash
# Converter PPTX → PDF → imagens (1 por slide)
soffice --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

Gera `slide-01.jpg`, `slide-02.jpg`, ...

Para cada slide, inspecione procurando:

- [ ] **Overlap**: texto sobre shape, linha sobre palavra, cards se tocando
- [ ] **Overflow**: texto cortado, cabendo por pouco, ou estourando caixa
- [ ] **Margem insuficiente**: qualquer elemento a < 0.5" da borda
- [ ] **Gaps desiguais**: 0.5" num lugar, 0.2" em outro
- [ ] **Contraste baixo**: texto cinza sobre creme, ícone escuro sobre fundo escuro
- [ ] **Linha decorativa sob título** (remova — vício de IA)
- [ ] **Layout repetido** 3+ slides seguidos iguais
- [ ] **Rodapé colidindo** com conteúdo
- [ ] **Fonte inconsistente** (uma família só, 2 no máximo)
- [ ] **Paleta drift** (cor fora da paleta escolhida)
- [ ] **KPI sem fonte** de dados

### 9.3 Loop de verificação

1. Gera → Converte → Inspeciona
2. **Lista issues** (se encontrou zero, olhe de novo)
3. Corrige
4. Re-renderiza e **re-inspeciona os slides afetados** — um fix muitas vezes cria outro problema
5. Repete até um passe completo sem issues

**Não declare pronto** sem pelo menos um ciclo completo fix-and-verify.

### 9.4 Dica forte: use subagent para inspeção

Mesmo com 2-3 slides, peça a um subagente para inspecionar as imagens. Você (o modelo que gerou) já "vê o que esperava", não o que está lá. Subagente tem olhos frescos.

Prompt sugerido:

```
Inspecione visualmente estes slides. ASSUMA QUE HÁ PROBLEMAS — encontre-os.

Procure por:
- Elementos sobrepostos
- Texto cortado nas bordas
- Contraste baixo
- Margens < 0.5"
- Gaps desiguais
- Títulos que não são action titles
- Linhas decorativas sob títulos
- Cores fora da paleta [lista a paleta]

Para cada slide, liste issues mesmo pequenos.

Imagens:
1. /path/slide-01.jpg (esperado: capa deck X)
2. /path/slide-02.jpg (esperado: executive summary com 3 bullets)
...

Reporte TODOS os issues encontrados.
```

---

## 11. Dependências

Para renderização e QA:

```bash
# Python
pip install python-pptx Pillow
pip install "markitdown[pptx]"

# Sistema (macOS)
brew install --cask libreoffice
brew install poppler

# Sistema (Linux)
sudo apt install libreoffice poppler-utils
```
