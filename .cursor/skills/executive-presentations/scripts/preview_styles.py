#!/usr/bin/env python3
"""
preview_styles.py — gera 3 HTML de uma página cada (ritual show-don't-tell) para escolher preset.

Saída: ../.preview/preview_<preset>.html (relativo à pasta scripts/)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from render_html import render_deck  # noqa: E402

PREVIEW_PRESETS = ["swiss_modern", "bold_signal", "dark_botanical"]


def main() -> None:
    skill_root = _SCRIPT_DIR.parent
    out_dir = skill_root / ".preview"
    out_dir.mkdir(parents=True, exist_ok=True)

    for preset in PREVIEW_PRESETS:
        mini: dict = {
            "title": f"Preview — {preset}",
            "preset": preset,
            "brand_mode": "off",
            "profile": "corporate",
            "author": "Cursor",
            "date": "2026",
            "slides": [
                {
                    "layout": "title",
                    "deck_tag": "Estilo visual",
                    "title": "Qual preset combina?",
                    "subtitle": "Compare tipografia, cor e ritmo antes de gerar o deck completo.",
                    "date": preset.replace("_", " ").title(),
                }
            ],
        }
        tmp = out_dir / f"_tmp_{preset}.json"
        tmp.write_text(json.dumps(mini, ensure_ascii=False, indent=2), encoding="utf-8")
        target = out_dir / f"preview_{preset}.html"
        render_deck(tmp, target)
        tmp.unlink(missing_ok=True)
        print(f"Wrote {target}")


if __name__ == "__main__":
    main()
