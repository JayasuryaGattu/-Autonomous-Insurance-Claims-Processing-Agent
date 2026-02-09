import pdfplumber
from pathlib import Path

def load_document(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        return _load_pdf(path)
    elif path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError("Unsupported file format")

def _load_pdf(path: Path) -> str:
    text = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)
