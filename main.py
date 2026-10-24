
from pathlib import Path
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

    for page in extracted_pages:
        print(f"Arquivo: {page['file']} | Página: {page['page']}")
        print(page["text"])

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



if __name__ == "__main__":
    main()
