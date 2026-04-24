"""
style_presets.py — catálogo de presets visuais (inspirado em frontend-slides).
4 presets implementados; demais ids existem como aliases para swiss_modern até expansão.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Preset:
    id: str
    name: str
    mood_tags: list[str]
    # Google Fonts: families para URL (substituir espaço por +)
    font_display: str
    font_body: str
    # Valores CSS (hex com #)
    bg: str
    surface: str
    ink: str
    muted: str
    accent: str
    highlight: str
    on_dark: str
    primary: str = ""
    primary_dark: str = ""
    # Assinatura visual: CSS extra (gradientes, grid, etc.)
    signature_css: str = ""

    def __post_init__(self) -> None:
        if not self.primary:
            object.__setattr__(self, "primary", self.accent)
        if not self.primary_dark:
            object.__setattr__(self, "primary_dark", self.ink)

    def google_fonts_url(self) -> str:
        d = self.font_display.replace(" ", "+")
        b = self.font_body.replace(" ", "+")
        if d == b:
            return f"https://fonts.googleapis.com/css2?family={d}:wght@400;600;700&display=swap"
        return (
            "https://fonts.googleapis.com/css2?"
            f"family={d}:wght@400;600;700&"
            f"family={b}:wght@400;500;600;700&"
            "display=swap"
        )

    def css_variables(self) -> dict[str, str]:
        return {
            "--font-display": f'"{self.font_display}", system-ui, sans-serif',
            "--font-body": f'"{self.font_body}", system-ui, sans-serif',
            "--color-bg": self.bg,
            "--color-surface": self.surface,
            "--color-ink": self.ink,
            "--color-muted": self.muted,
            "--color-accent": self.accent,
            "--color-highlight": self.highlight,
            "--color-on-dark": self.on_dark,
            "--color-primary": self.primary,
            "--color-primary-dark": self.primary_dark,
        }


# --- 4 presets completos (implementação inicial) ---

PRESET_SWISS = Preset(
    id="swiss_modern",
    name="Swiss Modern",
    mood_tags=["calm", "focused", "corporate", "data"],
    font_display="Archivo",
    font_body="Nunito Sans",
    bg="#FFFFFF",
    surface="#F3F4F6",
    ink="#0A0A0A",
    muted="#6B7280",
    accent="#DC2626",
    highlight="#FEE2E2",
    on_dark="#FFFFFF",
    primary="#111827",
    primary_dark="#0B0F1A",
    signature_css="""
    .slide { background: var(--color-bg); }
    .preset-signature::before {
      content: "";
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(to right, rgba(0,0,0,0.06) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(0,0,0,0.06) 1px, transparent 1px);
      background-size: clamp(24px, 4vw, 48px) clamp(24px, 4vw, 48px);
      pointer-events: none;
      opacity: 0.35;
    }
    .kicker { letter-spacing: 0.12em; text-transform: uppercase; font-weight: 600; color: var(--color-accent); }
    .big-number { font-family: var(--font-display); font-weight: 700; color: var(--color-ink); }
    """,
)

PRESET_BOLD = Preset(
    id="bold_signal",
    name="Bold Signal",
    mood_tags=["impressed", "confident", "pitch"],
    font_display="Archivo Black",
    font_body="Space Grotesk",
    bg="#141414",
    surface="#1F1F1F",
    ink="#FAFAFA",
    muted="#A3A3A3",
    accent="#EA580C",
    highlight="#431407",
    on_dark="#FFFFFF",
    primary="#EA580C",
    primary_dark="#0A0A0A",
    signature_css="""
    .slide { background: var(--color-bg); color: var(--color-ink); }
    .card-accent {
      background: linear-gradient(135deg, var(--color-accent) 0%, #F97316 100%);
      color: #0A0A0A;
      border: none;
    }
    .kicker { color: var(--color-accent); letter-spacing: 0.15em; }
    .big-number { font-family: var(--font-display); color: var(--color-ink); }
    .chapter-num { font-family: var(--font-display); color: var(--color-accent); opacity: 0.9; }
    """,
)

PRESET_BOTANICAL = Preset(
    id="dark_botanical",
    name="Dark Botanical",
    mood_tags=["inspired", "premium", "elegant"],
    font_display="Cormorant Garamond",
    font_body="IBM Plex Sans",
    bg="#0C0A09",
    surface="#1C1917",
    ink="#FAF7F2",
    muted="#A8A29E",
    accent="#D97757",
    highlight="#44403C",
    on_dark="#FAF7F2",
    primary="#D97757",
    primary_dark="#050403",
    signature_css="""
    .slide {
      background: radial-gradient(ellipse 120% 80% at 80% 20%, rgba(217,119,87,0.12) 0%, transparent 50%),
                  radial-gradient(ellipse 80% 60% at 10% 90%, rgba(120,113,108,0.15) 0%, transparent 45%),
                  var(--color-bg);
      color: var(--color-ink);
    }
    .kicker { color: #C4A484; letter-spacing: 0.1em; text-transform: uppercase; font-size: var(--small-size); }
    .big-number { font-family: var(--font-display); font-weight: 600; color: var(--color-ink); }
    .scqa-card { border: 1px solid rgba(250,247,242,0.12); background: rgba(28,25,23,0.85); }
    """,
)

PRESET_PAPER = Preset(
    id="paper_ink",
    name="Paper & Ink",
    mood_tags=["calm", "story", "editorial"],
    font_display="Cormorant Garamond",
    font_body="Source Serif 4",
    bg="#FDF6E3",
    surface="#F5ECD7",
    ink="#1C1917",
    muted="#57534E",
    accent="#991B1B",
    highlight="#FECACA",
    on_dark="#FDF6E3",
    primary="#991B1B",
    primary_dark="#1C1917",
    signature_css="""
    .slide { background: var(--color-bg); color: var(--color-ink); }
    .pull-quote { font-family: var(--font-display); font-style: italic; font-size: var(--h2-size); border-left: 4px solid var(--color-accent); padding-left: var(--content-gap); }
    .kicker { color: var(--color-accent); font-variant: small-caps; letter-spacing: 0.14em; }
    .big-number { font-family: var(--font-display); font-weight: 600; color: var(--color-ink); }
    .scqa-card { background: var(--color-surface); border: 1px solid rgba(28,25,23,0.08); }
    """,
)

# Stubs: mapeiam para preset próximo até implementação completa
STUB_ALIASES: dict[str, str] = {
    "electric_studio": "swiss_modern",
    "creative_voltage": "bold_signal",
    "notebook_tabs": "paper_ink",
    "pastel_geometry": "paper_ink",
    "split_pastel": "paper_ink",
    "vintage_editorial": "paper_ink",
    "neon_cyber": "bold_signal",
    "terminal_green": "swiss_modern",
}

PRESETS: dict[str, Preset] = {
    "swiss_modern": PRESET_SWISS,
    "bold_signal": PRESET_BOLD,
    "dark_botanical": PRESET_BOTANICAL,
    "paper_ink": PRESET_PAPER,
}

PROFILE_DEFAULT_PRESET: dict[str, str] = {
    "corporate": "swiss_modern",
    "startup": "bold_signal",
    "consulting": "swiss_modern",
}


def normalize_hex(h: str) -> str:
    h = str(h).strip().lstrip("#")
    if len(h) == 6:
        return "#" + h.upper()
    return "#" + h


def get_preset(preset_id: str | None, profile: str | None) -> Preset:
    pid = (preset_id or "").strip().lower()
    if pid in STUB_ALIASES:
        pid = STUB_ALIASES[pid]
    if pid in PRESETS:
        return PRESETS[pid]
    prof = (profile or "corporate").lower()
    fallback = PROFILE_DEFAULT_PRESET.get(prof, "swiss_modern")
    return PRESETS[fallback]


def apply_brand_to_preset(
    preset: Preset,
    brand: dict[str, Any] | None,
    brand_mode: str,
) -> Preset:
    """
    brand_mode: strict | accent_only | off
    """
    mode = (brand_mode or "off").strip().lower()
    if not brand or mode == "off":
        return preset

    b = {k: normalize_hex(v) if isinstance(v, str) and k not in ("logo_path", "header_font", "body_font") else v for k, v in brand.items()}

    if mode == "accent_only":
        acc = b.get("accent")
        if acc:
            return Preset(
                id=preset.id,
                name=preset.name,
                mood_tags=preset.mood_tags,
                font_display=preset.font_display,
                font_body=preset.font_body,
                bg=preset.bg,
                surface=preset.surface,
                ink=preset.ink,
                muted=preset.muted,
                accent=acc,
                highlight=preset.highlight,
                on_dark=preset.on_dark,
                primary=preset.primary,
                primary_dark=preset.primary_dark,
                signature_css=preset.signature_css,
            )
        return preset

    # strict
    primary = b.get("primary", preset.surface)
    primary_dark = b.get("primary_dark", primary)
    accent = b.get("accent", preset.accent)
    surface = b.get("surface", preset.surface)
    ink = b.get("text_dark", preset.ink)
    muted = b.get("muted", preset.muted)
    on_dark = b.get("on_dark", preset.on_dark)

    # Fundo: presets escuros usam primary_dark como bg aproximado; claros mantêm branco/cream com surface da marca
    is_dark = preset.bg.lower() in ("#141414", "#0c0a09") or preset.id in ("bold_signal", "dark_botanical")
    br_primary = str(b.get("primary", preset.primary))
    br_primary_dark = str(b.get("primary_dark", preset.primary_dark))

    if is_dark:
        new_bg = primary_dark
        new_surface = primary
        new_ink = str(b.get("on_dark") or preset.ink)
        new_muted = preset.muted  # evita muted corporativo escuro ilegível no fundo escuro
        new_primary = br_primary
        new_primary_dark = br_primary_dark
    else:
        new_bg = "#FFFFFF" if preset.bg.upper().startswith("#FFF") or preset.bg == "#FFFFFF" else surface
        new_surface = surface
        new_ink = ink
        new_muted = muted
        new_primary = br_primary
        new_primary_dark = br_primary_dark

    return Preset(
        id=preset.id,
        name=preset.name,
        mood_tags=preset.mood_tags,
        font_display=preset.font_display,
        font_body=preset.font_body,
        bg=new_bg,
        surface=new_surface if not is_dark else preset.surface,
        ink=new_ink,
        muted=new_muted,
        accent=accent,
        highlight=b.get("secondary", preset.highlight) if isinstance(b.get("secondary"), str) else preset.highlight,
        on_dark=on_dark,
        primary=normalize_hex(new_primary) if not new_primary.startswith("#") else new_primary,
        primary_dark=normalize_hex(new_primary_dark) if not new_primary_dark.startswith("#") else new_primary_dark,
        signature_css=preset.signature_css,
    )


def resolve_brand_mode(deck: dict[str, Any]) -> str:
    explicit = deck.get("brand_mode")
    if explicit:
        return str(explicit).strip().lower()
    brand = deck.get("brand") or deck.get("brand_path")
    if brand or deck.get("brand_path"):
        return "strict"
    return "off"
