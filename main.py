
from pathlib import Path
import sys


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

    print("Ambiente inicial configurado!")


if __name__ == "__main__":
    main()
