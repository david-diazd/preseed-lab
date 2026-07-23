#!/usr/bin/env python3
"""Extract text from PDF files to markdown.

Uso:
    python tools/pdf2md.py inputs/pitch.pdf
    python tools/pdf2md.py inputs/pdfs/                 # carpeta entera
    python tools/pdf2md.py inputs/pdfs/ --force         # re-procesar aunque exista el .md

Dependencia: pdfplumber  (pip install pdfplumber)
"""

import argparse
import sys
from pathlib import Path

import pdfplumber

PDF_EXTS = {".pdf"}


def find_pdfs(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob("*") if p.suffix.lower() in PDF_EXTS)


def table_to_markdown(table: list[list[str | None]]) -> str:
    rows = []
    for i, row in enumerate(table):
        cells = [(c or "").strip().replace("\n", " ").replace("|", "\\|") for c in row]
        rows.append("| " + " | ".join(cells) + " |")
        if i == 0:
            rows.append("| " + " | ".join("---" for _ in cells) + " |")
    return "\n".join(rows)


def extract_page(page) -> str:
    parts: list[str] = []
    text = page.extract_text()
    if text and text.strip():
        parts.append(text.strip())
    for table in page.extract_tables():
        if table:
            parts.append(table_to_markdown(table))
    return "\n\n".join(parts)


def convert(path: Path, out_dir: Path) -> None:
    print(f"Extrayendo: {path.name} ...")
    sections: list[str] = [f"# Extracción PDF: {path.name}\n"]
    with pdfplumber.open(path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            content = extract_page(page)
            sections.append(f"## Página {i}/{total}\n\n{content}\n")
            if i % 10 == 0:
                print(f"  ... {i}/{total} páginas")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{path.stem}.md"
    out_path.write_text("\n".join(sections), encoding="utf-8")
    print(f"  -> Guardado en {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrae texto de PDFs a markdown")
    parser.add_argument("input", help="Archivo PDF o carpeta con PDFs")
    parser.add_argument(
        "--out",
        default="outputs/pdfs",
        help="Carpeta de salida (default: outputs/pdfs)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-procesar aunque ya exista el .md de salida",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        sys.exit(f"No existe: {input_path}")

    files = find_pdfs(input_path)
    if not files:
        sys.exit(f"No se encontraron PDFs en: {input_path}")

    out_dir = Path(args.out)

    if not args.force:
        pending = [f for f in files if not (out_dir / f"{f.stem}.md").exists()]
        skipped = len(files) - len(pending)
        if skipped:
            print(f"Omitiendo {skipped} archivo(s) ya procesado(s). Usa --force para re-procesar.")
        files = pending
        if not files:
            sys.exit("Nada que hacer.")

    ok, fail = 0, 0
    for f in files:
        try:
            convert(f, out_dir)
            ok += 1
        except Exception as e:
            print(f"  !! Error procesando {f.name}: {e}", file=sys.stderr)
            fail += 1

    print(f"\nListo. {ok} ok, {fail} con error. Salida en {out_dir}/")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
