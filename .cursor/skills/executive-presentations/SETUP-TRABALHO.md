# Setup no Mac do trabalho

Leve a skill pelo **Git** (repositório **privado** recomendado se houver paleta ou materiais internos).

## 1. No Mac de casa

```bash
cd "/caminho/Skill Apresentacoes"
git status
git add .
git commit -m "skill executive-presentations"
git remote add origin <url-do-repo-privado>
git push -u origin main
```

## 2. No Mac do trabalho

```bash
git clone <url-do-repo-privado> ~/Programacao/Skill-Apresentacoes
cd ~/Programacao/Skill-Apresentacoes/.cursor/skills/executive-presentations
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

- **PDF:** use `scripts/export_pdf.py` — precisa do **Google Chrome** instalado ou `pip install playwright && playwright install chromium`.

## 3. Preencher a marca (não vai no Git)

1. Copie `brand/brand.json.example` → `brand/brand.json` e preencha com o guia oficial da empresa.
2. Copie logos para `brand/logos/` (ex.: `logo.svg`).
3. Fotos aprovadas em `brand/images/`.
4. PDFs/PPTX de referência em `brand/reference-decks/`.

Detalhes: [brand/README.md](brand/README.md).

## 4. Skill global no Cursor (opcional)

Para ter a skill em **todos** os projetos:

```bash
cp -R ~/Programacao/Skill-Apresentacoes/.cursor/skills/executive-presentations ~/.cursor/skills/
```

(Ajuste o caminho de origem para onde você clonou o repo.)

## 5. Teste rápido

```bash
cd ~/.cursor/skills/executive-presentations   # ou o clone do repo
source .venv/bin/activate
python scripts/render_html.py brand/examples/board_expansao.json /tmp/deck-teste.html
open /tmp/deck-teste.html
```

Se abrir com slides navegáveis (setas / scroll), o ambiente está OK.
