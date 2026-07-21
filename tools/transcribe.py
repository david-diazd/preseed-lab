#!/usr/bin/env python3
"""Transcribe audio files locally using faster-whisper.

Uso:
    python tools/transcribe.py inputs/audio/reunion.m4a
    python tools/transcribe.py inputs/audio/                  # carpeta entera
    python tools/transcribe.py inputs/audio/ --model medium --lang es
    python tools/transcribe.py inputs/audio/ --force         # re-transcribir aunque exista el .md
"""

import argparse
import sys
from pathlib import Path

from faster_whisper import WhisperModel

AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".mp4", ".ogg", ".flac", ".webm", ".aac", ".opus"}


def format_ts(seconds: float) -> str:
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def find_audio_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob("*") if p.suffix.lower() in AUDIO_EXTS)


def transcribe(path: Path, model: WhisperModel, out_dir: Path, language: str | None) -> None:
    print(f"Transcribiendo: {path.name} ...")
    segments, info = model.transcribe(str(path), language=language, vad_filter=True)

    lines = []
    for i, seg in enumerate(segments, 1):
        lines.append(f"[{format_ts(seg.start)}] {seg.text.strip()}")
        if i % 20 == 0:
            print(f"  ... {i} segmentos ({format_ts(seg.end)})")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{path.stem}.md"
    out_path.write_text(
        f"# Transcripción: {path.name}\n\n"
        f"Idioma detectado: {info.language} (confianza {info.language_probability:.2f})\n\n"
        + "\n".join(lines)
        + "\n",
        encoding="utf-8",
    )
    print(f"  -> Guardado en {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe audio con faster-whisper")
    parser.add_argument("input", help="Archivo de audio o carpeta con audios")
    parser.add_argument(
        "--model",
        default="small",
        choices=["tiny", "base", "small", "medium", "large-v3"],
        help="Tamaño del modelo (default: small; medium/large-v3 = mas preciso pero mas lento)",
    )
    parser.add_argument(
        "--lang",
        default=None,
        help="Forzar idioma (ej. es, en, auto). Por defecto autodetecta.",
    )
    parser.add_argument(
        "--out",
        default="outputs/transcripts",
        help="Carpeta de salida (default: outputs/transcripts)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-transcribir aunque ya exista el .md de salida",
    )
    args = parser.parse_args()

    language = None if args.lang in (None, "auto") else args.lang

    input_path = Path(args.input)
    if not input_path.exists():
        sys.exit(f"No existe: {input_path}")

    files = find_audio_files(input_path)
    if not files:
        sys.exit(f"No se encontraron audios en: {input_path}")

    out_dir = Path(args.out)

    if not args.force:
        pending = [f for f in files if not (out_dir / f"{f.stem}.md").exists()]
        skipped = len(files) - len(pending)
        if skipped:
            print(f"Omitiendo {skipped} archivo(s) ya transcrito(s). Usa --force para re-transcribir.")
        files = pending
        if not files:
            sys.exit("Nada que hacer.")

    print(f"Cargando modelo '{args.model}' (esto tarda mas la primera vez, se descarga)...")
    model = WhisperModel(args.model, device="cpu", compute_type="int8")

    ok, fail = 0, 0
    for f in files:
        try:
            transcribe(f, model, out_dir, language)
            ok += 1
        except Exception as e:
            print(f"  !! Error transcribiendo {f.name}: {e}", file=sys.stderr)
            fail += 1

    print(f"\nListo. {ok} ok, {fail} con error. Salida en {out_dir}/")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
