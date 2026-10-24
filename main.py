
from pathlib import Path
from math import hypot
import sys
import pymupdf


def check_directories():
    project_path = Path(__file__).resolve().parent

    data_path = project_path / "data"

    data_path.mkdir(parents=True, exist_ok=True)

    print("Diretório data disponível!")



def main():
    project_path = Path(__file__).resolve().parent

    print("=== RAG Assistant ===")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Diretório: {project_path}")

    check_directories()

    pdf_path = project_path / "data" / "teste.pdf"

    extracted_pages = extract_text_from_pdf(pdf_path)
    chunks = create_chunks_from_pages(extracted_pages, chunk_size=50, overlap=10)

    for chunk in chunks:
        print(
            f"Arquivo: {chunk['file']} | Página: {chunk['page']} "
            f"| Trecho: {chunk['chunk_number']}"
        )
        print(chunk["text"])

    print("\nExemplo didático com vetores fictícios:")
    question_vector = [1, 0]
    for vector in ([0.8, 0.2], [0.2, 0.8]):
        score = cosine_similarity(question_vector, vector)
        print(f"Similaridade com {vector}: {score:.3f}")

def extract_text_from_pdf(pdf_path):
    pages = []

    with pymupdf.open(pdf_path) as document:
        for page_number, page in enumerate(document, start=1):
            pages.append({
                "file": pdf_path.name,
                "page": page_number,
                "text": page.get_text(),
            })

    return pages

def split_text_into_chunks(text, chunk_size, overlap=0):
    if chunk_size <= 0:
        raise ValueError("chunk_size deve ser maior que zero.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap deve ser maior ou igual a zero e menor que chunk_size.")

    step = chunk_size - overlap
    chunks = []

    for start in range(0, len(text), step):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        if end >= len(text):
            break

    return chunks

def create_chunks_from_pages(pages, chunk_size, overlap=0):
    if chunk_size <= 0:
        raise ValueError("chunk_size deve ser maior que zero.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap deve ser maior ou igual a zero e menor que chunk_size.")

    chunks = []

    for page in pages:
        if not page["text"].strip():
            continue

        page_chunks = split_text_into_chunks(page["text"], chunk_size, overlap)

        for chunk_number, text in enumerate(page_chunks, start=1):
            chunks.append({
                "file": page["file"],
                "page": page["page"],
                "chunk_number": chunk_number,
                "text": text,
            })

    return chunks

def cosine_similarity(vector_a, vector_b):
    """Compara a direção de dois vetores numéricos finitos e não nulos."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Os vetores devem ter a mesma dimensão.")
    if not vector_a:
        raise ValueError("Os vetores não podem ser vazios.")

    magnitude_a = hypot(*vector_a)
    magnitude_b = hypot(*vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("A similaridade não é definida para vetores nulos.")

    return sum(
        (a / magnitude_a) * (b / magnitude_b)
        for a, b in zip(vector_a, vector_b)
    )


if __name__ == "__main__":
    main()
