#!/usr/bin/env python3
"""Fetch YouTube transcripts to markdown.

Uso:
    python tools/yt-transcript.py https://youtu.be/dQw4w9WgXcQ
    python tools/yt-transcript.py dQw4w9WgXcQ
    python tools/yt-transcript.py urls.txt                 # fichero con una URL/ID por línea
    python tools/yt-transcript.py urls.txt --lang es        # preferir idioma
    python tools/yt-transcript.py urls.txt --force          # re-descargar

Dependencia: youtube-transcript-api  (pip install youtube-transcript-api)
"""

import argparse
import re
import sys
from pathlib import Path

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|embed/|shorts/)([A-Za-z0-9_-]{11})")


def parse_video_id(token: str) -> str | None:
    token = token.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", token):
        return token
    m = VIDEO_ID_RE.search(token)
    return m.group(1) if m else None


def read_tokens(input_path: Path) -> list[str]:
    if input_path.is_file() and input_path.suffix.lower() == ".txt":
        return [
            line.strip()
            for line in input_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
    return [str(input_path)]


def format_ts(seconds: float) -> str:
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def out_path_for(video_id: str, out_dir: Path) -> Path:
    return out_dir / f"yt_{video_id}.md"


def fetch_one(token: str, out_dir: Path, lang: str | None) -> None:
    video_id = parse_video_id(token)
    if not video_id:
        raise ValueError(f"No se pudo extraer video ID de: {token}")

    api = YouTubeTranscriptApi()
    if lang:
        try:
            t = api.fetch(video_id, languages=[lang])
            lang_used = t.language_code
        except NoTranscriptFound:
            t = api.fetch(video_id)
            lang_used = t.language_code
    else:
        t = api.fetch(video_id)
        lang_used = t.language_code

    print(f"Descargando: {video_id} ({lang_used}, {len(t)} segmentos) ...")

    lines = [
        f"# YouTube: {video_id}",
        f"URL: https://youtu.be/{video_id}",
        f"Idioma: {lang_used}",
        f"Auto-generado: {'sí' if t.is_generated else 'no'}\n",
    ]
    for snippet in t:
        lines.append(f"[{format_ts(snippet.start)}] {snippet.text.strip()}")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_path_for(video_id, out_dir)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  -> Guardado en {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Descarga transcripciones de YouTube")
    parser.add_argument("input", help="URL, video ID, o fichero .txt con uno por línea")
    parser.add_argument(
        "--lang",
        default=None,
        help="Preferir idioma (ej. es, en). Si no existe, cae al default del video.",
    )
    parser.add_argument(
        "--out",
        default="outputs/transcripts",
        help="Carpeta de salida (default: outputs/transcripts)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-descargar aunque ya exista el .md de salida",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        sys.exit(f"No existe: {input_path}")

    tokens = read_tokens(input_path)
    if not tokens:
        sys.exit("No se encontraron URLs/videos.")

    out_dir = Path(args.out)

    if not args.force:
        pending = []
        for t in tokens:
            vid = parse_video_id(t)
            if vid and out_path_for(vid, out_dir).exists():
                continue
            pending.append(t)
        skipped = len(tokens) - len(pending)
        if skipped:
            print(f"Omitiendo {skipped} video(s) ya descargado(s). Usa --force para re-descargar.")
        tokens = pending
        if not tokens:
            sys.exit("Nada que hacer.")

    ok, fail = 0, 0
    for t in tokens:
        try:
            fetch_one(t, out_dir, args.lang)
            ok += 1
        except (VideoUnavailable, TranscriptsDisabled, NoTranscriptFound) as e:
            print(f"  !! {t}: {type(e).__name__}: {e}", file=sys.stderr)
            fail += 1
        except Exception as e:
            print(f"  !! Error procesando {t}: {e}", file=sys.stderr)
            fail += 1

    print(f"\nListo. {ok} ok, {fail} con error. Salida en {out_dir}/")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
