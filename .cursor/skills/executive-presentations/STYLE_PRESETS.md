# Style Presets — executive-presentations (HTML)

Referência visual alinhada à filosofia da skill [`frontend-slides`](https://skillsmp.com/pt/skills/affaan-m-everything-claude-code-agents-skills-frontend-slides-skill-md) (viewport-fit, densidade, presets distintos). O motor HTML usa `scripts/style_presets.py`.

## Viewport fit (não negociável)

Cada slide = **exatamente uma altura de viewport**. Conteúdo demais = **dividir em mais slides**. Sem scroll interno no slide.

### Limites de densidade

| Tipo de slide | Máximo |
|----------------|--------|
| Título | 1 heading + 1 subtítulo + tagline opcional |
| Conteúdo | 1 heading + 4–6 bullets ou 2 parágrafos curtos |
| Grade de cards | 6 cards |
| Citação | 1 quote + atribuição |
| Imagem | 1 imagem, idealmente &lt; 60vh |

### Bloco CSS base obrigatório

O gerador `render_html.py` injeta variantes deste bloco em todo deck. Não remova: `100vh`/`100dvh`, `overflow: hidden` em `.slide`, tipografia com `clamp()`.

```css
html, body { height: 100%; margin: 0; overflow-x: hidden; }
html { scroll-snap-type: y mandatory; scroll-behavior: smooth; }
.slide {
  width: 100vw; height: 100vh; height: 100dvh;
  overflow: hidden; scroll-snap-align: start;
  display: flex; flex-direction: column; position: relative;
}
.slide-content {
  flex: 1; display: flex; flex-direction: column; justify-content: center;
  max-height: 100%; overflow: hidden;
  padding: var(--slide-padding);
}
```

## Mood → preset (mapeamento sugerido)

| Sensação | Presets fortes |
|-----------|------------------|
| Impresso / confiante | `bold_signal`, `swiss_modern` |
| Energizado | `bold_signal` (stub: `creative_voltage`, `neon_cyber`) |
| Calmo / focado | `swiss_modern`, `paper_ink` |
| Inspirado / premium | `dark_botanical` |

## Catálogo de presets

### Implementados (Python)

| ID | Nome | Uso |
|----|------|-----|
| `swiss_modern` | Swiss Modern | Corporativo, dados, grid suíço |
| `bold_signal` | Bold Signal | Pitch, alto contraste, fundo escuro |
| `dark_botanical` | Dark Botanical | Premium, narrativa, atmosfera |
| `paper_ink` | Paper & Ink | Editorial, ensaio, manifesto |

### Stubs (alias temporário)

Até implementação completa no `style_presets.py`, estes IDs **resolvem** para um preset próximo:

| ID stub | Redireciona para |
|---------|-------------------|
| `electric_studio` | `swiss_modern` |
| `creative_voltage` | `bold_signal` |
| `notebook_tabs` | `paper_ink` |
| `pastel_geometry` | `paper_ink` |
| `split_pastel` | `paper_ink` |
| `vintage_editorial` | `paper_ink` |
| `neon_cyber` | `bold_signal` |
| `terminal_green` | `swiss_modern` |

(Preset completo = tipografia + paleta + assinatura CSS próprias.)

## Brand mode (`deck.json`)

Campos opcionais na raiz do deck:

```json
"preset": "swiss_modern",
"brand_mode": "strict"
```

- **`strict`** (padrão se existir `brand` ou `brand_path`): aplica **cores** do guia (`primary`, `primary_dark`, `accent`, `surface`, `text_dark`, `muted`, `on_dark`) sobre o preset; **mantém fontes do preset** (tipografia é o diferencial visual).
- **`accent_only`**: só substitui o acento pela cor `accent` da marca.
- **`off`**: ignora marca; usa só o preset.

Hex no JSON **sem** `#` (compatível com o gerador PPTX).

## Checklist de viewport (QA)

- [ ] Cada `.slide` com `height: 100vh`, `100dvh`, `overflow: hidden`
- [ ] Tipografia e espaçamento com `clamp()`
- [ ] Imagens com `max-height` em `vh`
- [ ] Testar: 1920×1080, 1280×720, 768×1024, 375×667, 667×375

## Anti-patterns

- Gradiente roxo “startup genérico” sem identidade
- Paredes de bullet
- `-clamp(...)` negado no CSS (use `calc(-1 * clamp(...))`)

## Ritual “show, don’t tell”

Para quem ainda não escolheu estilo: rode `python scripts/preview_styles.py` — gera 3 HTML de **uma página** em `.preview/` para comparar presets antes do deck completo.
