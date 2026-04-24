# Skill `frontend-design` (Cursor)

Este repositório contém **apenas** a skill [**`frontend-design`**](.cursor/skills/frontend-design/SKILL.md) (direção estética, UI, anti–“AI slop”). No Cursor, use **`@frontend-design`** ou priorize esta skill no projeto.

## Marca da empresa (guia)

A skill define **Purpose / Tone / Constraints / Differentiation** e boas práticas de UI; **não** substitui o manual de marca. Coloque identidade e tokens **fora** de `.cursor/skills/` (a skill pode ser atualizada por sync).

| Artefato | Função |
|----------|--------|
| [`brand/brand-brief.md`](brand/brand-brief.md) | Posicionamento, voz, uso de logo, o que evitar (template editável). |
| [`brand/tokens.json.example`](brand/tokens.json.example) | Modelo de cores, fontes, raios — copie para `brand/tokens.json` (local) e mapeie em `:root` no front. |
| `brand/logos/` | SVG/PNG oficiais (não versionar ativos confidenciais se a política exigir outro repositório). |
| [`.gitignore`](.gitignore) | `brand/tokens.json` e `brand/tokens.local.json` podem ficar fora do Git; use o `.example` como base. |

Regra opcional: [`.cursor/rules/brand.mdc`](.cursor/rules/brand.mdc) — lembrar a IA a ler `brand/` ao estilizar UI.

## Atualizar a skill via CLI

A `frontend-design` costuma vir de catálogos como [`vercel-labs/skills`](https://github.com/vercel-labs/skills) / Anthropic. Exemplos:

```bash
npx --package=skills -- skills list
npx --package=skills -- skills update frontend-design
```

> Se o CLI instalar em `.agents/skills/`, **mova** para [`.cursor/skills/`](.cursor/skills/) para manter a convenção deste repositório.

## Lock de skills

[`skills-lock.json`](skills-lock.json) documenta a skill fixada para a CLI de skills do projeto.

## Link

[`.cursor/skills/frontend-design/SKILL.md`](.cursor/skills/frontend-design/SKILL.md)
