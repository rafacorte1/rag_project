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
Embeddings ainda não foram implementados.

## 24/10/2026 — Chunking com sobreposição

- `split_text_into_chunks(text, chunk_size, overlap=0)` divide por caracteres,
  com avanço de `chunk_size - overlap`. Para quando um trecho alcança o fim
  do texto, evitando um trecho extra contendo apenas caracteres já incluídos.
- Valores inteiros devem respeitar `chunk_size > 0` e
  `0 <= overlap < chunk_size`; violações geram `ValueError`.
  A checagem explícita dos tipos dos argumentos ainda não foi implementada.
- `create_chunks_from_pages()` preserva arquivo e página e adiciona
  `chunk_number`, reiniciado em 1 em cada página. Ignora páginas vazias
  ou contendo apenas espaços. A sobreposição não atravessa páginas.
- `main()` exibe os chunks de `data/teste.pdf` usando tamanho 50 e overlap 10.
  Esses valores são didáticos, não parâmetros calibrados para recuperação.
- Testes por asserções validaram texto vazio, texto curto, divisão exata,
  sobreposição zero, sobreposição próxima ao tamanho e parâmetros inválidos.
- Fluxo completo validado com `data/validacao_paginas.pdf`, tamanho 30 e
  overlap 10: duas páginas com dois chunks cada e terceira página sem chunks.
  Foram conferidos metadados, numeração, limite de tamanho, os dez caracteres
  compartilhados e reconstrução exata do texto de cada página.

A divisão por caracteres pode cortar palavras e frases. Sobreposição não
elimina essa limitação. As validações foram executadas no terminal; ainda
não há uma suíte de testes persistida no projeto.

## 24/10/2026 — Similaridade de cosseno (exercício didático)

- Implementada `cosine_similarity(vector_a, vector_b)` com a biblioteca
  padrão: `math.hypot` calcula os comprimentos, e a soma dos produtos dos
  componentes normalizados calcula a similaridade.
- A função pressupõe componentes numéricos finitos. Rejeita vetores vazios,
  dimensões diferentes e vetores nulos com `ValueError`.
- `main()` demonstra vetores fictícios: `[1, 0]` comparado com `[0.8, 0.2]`
  resulta em aproximadamente 0,970; com `[0.2, 0.8]`, aproximadamente 0,243.
- Asserções validaram esses resultados, simetria, mesma direção (1),
  perpendicularidade (0), direções opostas (-1) e entradas inválidas.
- Execução completa de `main.py` e nova validação do fluxo PDF → chunks
  com sobreposição concluídas com sucesso.

Próxima sessão: apresentar opções para gerar embeddings reais, discutir
custos e uso de dados antes de escolher ou utilizar uma API. Nenhuma API
foi chamada, e os vetores fictícios não foram associados aos chunks.
