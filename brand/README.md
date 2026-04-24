# Marca (projeto)

Pasta **na raiz** do repositório — não dentro de [`.cursor/skills/frontend-design`](../.cursor/skills/frontend-design/SKILL.md), para não misturar a skill genérica (atualizável) com a identidade da sua empresa.

## O que colocar aqui

1. **[`brand-brief.md`](brand-brief.md)** — texto curto: posicionamento, voz, público, regras de logo (mínimo de área, claro/escuro, o que proibir).
2. **[`tokens.json.example`](tokens.json.example)** — modelo de design tokens. Copie para `tokens.json` e ajuste (o arquivo `tokens.json` está no [`.gitignore`](../.gitignore) se não quiser publicar a paleta).
3. **`logos/`** — arquivos oficiais; só o `.gitkeep` e este README entram no Git; substitua localmente ou ajuste o [`.gitignore`](../.gitignore) se a política for versionar SVGS.

Sobrescritas locais (opcional): crie `tokens.local.json` com o mesmo esquema parcial; no front, mescle depois de carregar `tokens.json`.

## Uso com IA

Nos pedidos de UI, referencie `@brand/brand-brief` e, se existir, `@brand/tokens.json` (cópia local), para alinhar cores e tipografia à marca.
