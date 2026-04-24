#!/usr/bin/env python3
"""
render_html.py — gera um HTML self-contained a partir de deck.json (mesmo schema do PPTX).

Uso:
  python render_html.py path/to/deck.json output/presentation.html

Requer: Jinja2 (ver requirements.txt)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from jinja2 import Environment, FileSystemLoader, select_autoescape

from style_presets import (
    Preset,
    apply_brand_to_preset,
    get_preset,
    resolve_brand_mode,
)

SUPPORTED_LAYOUTS = frozenset({
    "title",
    "chapter",
    "scqa_story",
    "hero_split",
    "executive_summary",
    "kpi_callout",
    "two_column",
    "chart",
    "comparison",
    "timeline",
    "image_right",
    "closing",
})


def load_deck(path: Path) -> dict[str, Any]:
    deck: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    bp = deck.get("brand_path")
    if bp:
        brp = (path.parent / str(bp)).resolve()
        if brp.is_file():
            file_brand = json.loads(brp.read_text(encoding="utf-8"))
            deck["brand"] = {**file_brand, **(deck.get("brand") or {})}
    return deck


def is_dark_bg(hex_color: str) -> bool:
    h = hex_color.strip().lstrip("#")
    if len(h) < 6:
        return False
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0
    return lum < 0.42


def chart_svg(chart: dict[str, Any], preset: Preset, width: int = 680, height: int = 260) -> str:
    """SVG para column/bar (agrupado) ou line."""
    if not chart:
        return ""
    ctype = str(chart.get("type", "column")).lower()
    xs = [str(x) for x in chart.get("x", [])]
    series_list = chart.get("series") or []
    if not xs or not series_list:
        return f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg"><text x="10" y="24" fill="{preset.muted}">Sem dados</text></svg>'

    colors = [preset.accent, preset.primary, preset.muted, "#94A3B8"]
    pad_l, pad_r, pad_t, pad_b = 44, 18, 16, 52
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b

    all_vals: list[float] = []
    for s in series_list:
        for v in s.get("values", []):
            try:
                all_vals.append(float(v))
            except (TypeError, ValueError):
                all_vals.append(0.0)
    vmax = max(all_vals + [1e-9])

    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Gráfico">'
    ]

    if ctype == "line":
        n = len(xs)
        step = plot_w / max(n - 1, 1)
        for si, s in enumerate(series_list):
            vals = [float(x) if x is not None else 0.0 for x in s.get("values", [])][:n]
            pts = []
            for i, v in enumerate(vals):
                x = pad_l + i * step
                y = pad_t + plot_h * (1 - v / vmax)
                pts.append(f"{x:.1f},{y:.1f}")
            col = colors[si % len(colors)]
            if pts:
                parts.append(
                    f'<polyline fill="none" stroke="{col}" stroke-width="2.5" points="{" ".join(pts)}" />'
                )
                for i, v in enumerate(vals):
                    x = pad_l + i * step
                    y = pad_t + plot_h * (1 - v / vmax)
                    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{col}" />')
        # eixo X labels
        for i, lab in enumerate(xs):
            x = pad_l + i * (plot_w / max(n - 1, 1))
            parts.append(
                f'<text x="{x:.1f}" y="{height - 18}" text-anchor="middle" font-size="10" fill="{preset.muted}">{_esc_xml(lab)}</text>'
            )
        parts.append(
            f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" y2="{pad_t + plot_h}" stroke="{preset.muted}" stroke-width="1" opacity="0.35"/>'
        )
        parts.append("</svg>")
        return "".join(parts)

    # column / bar vertical columns
    n = len(xs)
    m = len(series_list)
    group_w = plot_w / max(n, 1) * 0.72
    gap = plot_w / max(n, 1) * 0.14
    start_x = pad_l + gap / 2
    bar_w = group_w / max(m, 1) * 0.88
    bar_gap = group_w * 0.04

    for i in range(n):
        gx = start_x + i * (group_w + gap)
        for j, s in enumerate(series_list):
            vals = s.get("values", [])
            v = float(vals[i]) if i < len(vals) else 0.0
            bh = plot_h * (v / vmax)
            x = gx + j * (bar_w + bar_gap / max(m, 1))
            y = pad_t + plot_h - bh
            col = colors[j % len(colors)]
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{max(bh, 1):.1f}" rx="3" fill="{col}" />')

    for i, lab in enumerate(xs):
        cx = start_x + i * (group_w + gap) + group_w / 2
        parts.append(
            f'<text x="{cx:.1f}" y="{height - 14}" text-anchor="middle" font-size="10" fill="{preset.muted}">{_esc_xml(lab)}</text>'
        )

    # legenda simples
    ly = 8
    for j, s in enumerate(series_list[:4]):
        col = colors[j % len(colors)]
        lx = pad_l + j * 120
        parts.append(f'<rect x="{lx}" y="{ly}" width="10" height="10" rx="2" fill="{col}" />')
        parts.append(
            f'<text x="{lx + 14}" y="{ly + 9}" font-size="10" fill="{preset.ink}">{_esc_xml(str(s.get("label", "")))}</text>'
        )

    parts.append(
        f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" y2="{pad_t + plot_h}" stroke="{preset.muted}" stroke-width="1" opacity="0.35"/>'
    )
    parts.append("</svg>")
    return "".join(parts)


def _esc_xml(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def mini_bar_svg(rv: dict[str, Any], preset: Preset) -> str:
    data = rv.get("data") or []
    unit = str(rv.get("unit", ""))
    if not data:
        return ""
    maxv = max(float(d.get("value", 0) or 0) for d in data) or 1.0
    w, row_h, gap = 280, 28, 10
    h = len(data) * (row_h + gap) + 24
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">']
    y = 8
    for d in data:
        lab = str(d.get("label", ""))
        val = float(d.get("value", 0) or 0)
        hi = bool(d.get("highlight"))
        bw = (w - 100) * (val / maxv)
        col = preset.accent if hi else preset.primary
        parts.append(f'<text x="0" y="{y + 16}" font-size="11" fill="{preset.ink}">{_esc_xml(lab)}</text>')
        parts.append(
            f'<rect x="90" y="{y + 4}" width="{max(bw, 2):.1f}" height="{row_h - 8}" rx="3" fill="{col}" opacity="0.9" />'
        )
        parts.append(
            f'<text x="{min(90 + bw + 6, w - 4):.1f}" y="{y + 16}" font-size="10" fill="{preset.muted}">{val:g}{_esc_xml(unit)}</text>'
        )
        y += row_h + gap
    parts.append("</svg>")
    return "".join(parts)


def build_asset_resolver(deck_dir: Path, out_path: Path) -> Callable[[str | None], str]:
    out_dir = out_path.parent

    def asset(rel: str | None) -> str:
        if not rel:
            return ""
        s = str(rel).strip()
        if s.startswith("http://") or s.startswith("https://"):
            return s
        ap = (deck_dir / s).resolve()
        if not ap.is_file():
            return ""
        try:
            return Path(os.path.relpath(ap, out_dir)).as_posix()
        except ValueError:
            return ap.as_uri()

    return asset


def render_deck(deck_path: Path, out_path: Path) -> None:
    deck = load_deck(deck_path)
    deck_dir = deck_path.parent

    raw_preset = deck.get("preset")
    profile = str(deck.get("profile", "corporate"))
    base_preset = get_preset(str(raw_preset) if raw_preset else None, profile)
    brand = deck.get("brand") if isinstance(deck.get("brand"), dict) else None
    mode = resolve_brand_mode(deck)
    preset = apply_brand_to_preset(base_preset, brand, mode)

    tpl_root = Path(__file__).resolve().parent.parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(tpl_root)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    asset = build_asset_resolver(deck_dir, out_path)

    def chart_fn(c: dict[str, Any]) -> str:
        return chart_svg(c, preset)

    def bar_fn(rv: dict[str, Any]) -> str:
        return mini_bar_svg(rv or {}, preset)

    bodies: list[str] = []
    slides = deck.get("slides") or []
    for i, slide in enumerate(slides):
        layout = str(slide.get("layout", "two_column"))
        if layout not in SUPPORTED_LAYOUTS:
            layout = "two_column"
        tmpl = env.get_template(f"slides/{layout}.j2")
        bodies.append(
            tmpl.render(
                slide=slide,
                deck=deck,
                slide_index=i,
                asset=asset,
                chart_svg=chart_fn,
                mini_bar_svg=bar_fn,
            )
        )

    inner_html = "\n".join(bodies)
    css_lines = "\n".join(f"  {k}: {v};" for k, v in preset.css_variables().items())

    body_class = "theme-dark" if is_dark_bg(preset.bg) else "theme-light"
    deck_title = str(deck.get("title", "Apresentação"))

    base = env.get_template("base.html.j2")
    html = base.render(
        deck_title=deck_title,
        fonts_url=preset.google_fonts_url(),
        css_variables=css_lines,
        signature_css=preset.signature_css,
        inner_html=inner_html,
        slide_count=len(slides),
        body_class=body_class,
    )

    out_path.write_text(html, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Render deck.json to self-contained HTML")
    ap.add_argument("deck_json", type=Path)
    ap.add_argument("output_html", type=Path)
    args = ap.parse_args()
    render_deck(args.deck_json.resolve(), args.output_html.resolve())
    print(f"Wrote {args.output_html}")


if __name__ == "__main__":
    main()
