#!/usr/bin/env python3
"""
export_pdf.py — exporta HTML de slides para PDF (Chromium headless; Playwright como fallback).

Uso:
  python export_pdf.py entrada.html saida.pdf
  python export_pdf.py entrada.html saida.pdf --landscape
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_chrome_executable() -> str | None:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for p in candidates:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    for name in ("google-chrome", "chromium", "chromium-browser", "google-chrome-stable"):
        w = shutil.which(name)
        if w:
            return w
    return None


def export_via_chrome(html_path: Path, pdf_path: Path, landscape: bool) -> bool:
    chrome = find_chrome_executable()
    if not chrome:
        return False
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    args = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        f"--print-to-pdf={pdf_path}",
    ]
    if landscape:
        args.append("--landscape")
    args.append(f"file://{html_path}")
    try:
        subprocess.run(args, check=True, capture_output=True, text=True, timeout=120)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return False
    return pdf_path.is_file() and pdf_path.stat().st_size > 0


def export_via_playwright(html_path: Path, pdf_path: Path, landscape: bool) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle", timeout=60000)
            page.pdf(
                path=str(pdf_path),
                print_background=True,
                landscape=landscape,
                format="A4",
            )
            browser.close()
    except Exception:
        return False
    return pdf_path.is_file() and pdf_path.stat().st_size > 0


def main() -> None:
    ap = argparse.ArgumentParser(description="Export slide HTML to PDF")
    ap.add_argument("input_html", type=Path)
    ap.add_argument("output_pdf", type=Path)
    ap.add_argument("--landscape", action="store_true", help="Landscape PDF (útil para 16:9)")
    args = ap.parse_args()
    html_path = args.input_html.resolve()
    pdf_path = args.output_pdf.resolve()
    if not html_path.is_file():
        print(f"Arquivo não encontrado: {html_path}", file=sys.stderr)
        sys.exit(1)

    if export_via_chrome(html_path, pdf_path, args.landscape):
        print(f"PDF (Chrome): {pdf_path}")
        return
    if export_via_playwright(html_path, pdf_path, args.landscape):
        print(f"PDF (Playwright): {pdf_path}")
        return

    print(
        "Não foi possível gerar PDF: instale Google Chrome/Chromium ou rode\n"
        "  pip install playwright && playwright install chromium",
        file=sys.stderr,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
