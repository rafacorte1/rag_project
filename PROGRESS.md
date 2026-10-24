# Progresso do RAG Assistant

## 24/10/2026 — Extração básica de PDFs

- Ambiente virtual com Python 3.14.6 e importação de PyMuPDF validada.
- `extract_text_from_pdf(pdf_path)` retorna uma lista de registros com
  `file`, `page` (numeração a partir de 1) e `text`.
- `main()` lê `data/teste.pdf` e exibe o texto com arquivo e página.
- Execução de `.venv/bin/python main.py` concluída com sucesso.
- Criado localmente `data/validacao_paginas.pdf`, com duas páginas de texto
  e uma terceira em branco. Validação por asserções confirmou:
  - três registros, com páginas 1, 2 e 3;
  - nome do arquivo preservado em todos os registros;
  - texto das duas primeiras páginas igual ao conteúdo inserido;
  - página em branco preservada com texto vazio (`""`).
- PDFs de teste permanecem locais: `data/` está no `.gitignore`.

A leitura de páginas em branco não realiza OCR. PDFs inválidos, arquivos
ausentes e documentos digitalizados ainda não possuem tratamento específico.
Chunking e embeddings ainda não foram implementados.
