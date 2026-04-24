# Identidade da marca (uso no trabalho)

Esta pasta segue o modelo **híbrido**: a **estrutura** e os **READMEs** vão para o Git; arquivos sensíveis (`brand.json`, logos reais, fotos, PDFs de referência) ficam **só na sua máquina** (ignorados pelo `.gitignore` na raiz do repo).

Se ainda não houver guia oficial, use o pacote de cores sugerido em [ds-reference-superapp-fintech-br.md](../ds-reference-superapp-fintech-br.md) só como **rascunho**; substitua pelos hex corporativos assim que o marketing aprovar.

## O que fazer no Mac do trabalho

1. Copie `brand.json.example` para **`brand.json`** (mesma pasta).
2. Preencha os hex do guia de marca (sem `#`) e, se quiser, `logo_path` apontando para `logos/logo.svg` ou `logos/logo.png`.
3. Coloque o logo em `logos/`, fotos aprovadas em `images/`, e 2–3 decks que o time admira em `reference-decks/` (PDF ou PPTX).

## Como o agente usa isso

- Ao gerar um deck com marca: no `deck.json` use `"brand_path": "../brand.json"` se o JSON estiver em `brand/examples/` ou `scripts/`; ajuste o caminho relativo à **pasta do arquivo `deck.json`**.
- Ou copie o objeto `brand` inteiro do `brand.json` para a raiz do deck (sobrescreve o arquivo).

Ver também [SETUP-TRABALHO.md](../SETUP-TRABALHO.md).
