import re, base64

# 1. Load assets
with open('logo_al_creative.png', 'rb') as f:
    logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

with open('photo_natural_sharp.png', 'rb') as f:
    photo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

with open('flyer_opt.jpg', 'rb') as f:
    flyer_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')

# 2. Extract portfolio items from original index.html
with open('index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    orig_text = f.read()

active_idx = orig_text.rfind('<!DOCTYPE html>')
active_html = orig_text[active_idx:]

gallery_m = re.search(r'<div class="gallery">(.*?)</div>\s*</section>', active_html, re.DOTALL)
portfolio_items_html = gallery_m.group(1).strip() if gallery_m else ""

# 3. Construct HTML
html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AL Creative Design Studio LLC | Alba Laguna</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {{
  --pink: #E91E79;
  --pink-dark: #B8125F;
  --plum-dark: #2A0E20;
  --rose: #F6DDE4;
  --rose-2: #FBECEF;
  --rose-3: #FFF6F8;
  --gold: #D7A33C;
  --gold-soft: #F0C96F;
  --gold-light: #FCE8B8;
  --ink: #351E27;
  --muted: #765D65;
  --white: #fffafc;
  --shadow: 0 14px 34px rgba(137,32,76,.14);
}}

* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}

body {{
  margin: 0;
  min-height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: var(--ink);
  background:
    radial-gradient(circle at 8% 8%, rgba(255,255,255,.65), transparent 25%),
    radial-gradient(circle at 92% 22%, rgba(231,94,143,.14), transparent 30%),
    radial-gradient(circle at 50% 90%, rgba(215,163,60,.12), transparent 40%),
    linear-gradient(180deg, #F8E8EC 0%, #F9E7EB 45%, #F6DDE4 100%);
  overflow-x: hidden;
}}

body:before {{
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: .25;
  background-image: radial-gradient(rgba(184,18,95,.18) .7px, transparent .7px);
  background-size: 16px 16px;
}}

.page {{
  width: min(100%, 780px);
  margin: 0 auto;
  padding: 18px 15px 50px;
  position: relative;
}}

/* ===== Language toggle ===== */
.lang-toggle {{
  position: fixed;
  top: 14px;
  right: 14px;
  z-index: 30;
  display: flex;
  gap: 3px;
  padding: 4px;
  background: rgba(255,250,252,.92);
  border: 1px solid rgba(184,18,95,.18);
  border-radius: 999px;
  box-shadow: 0 6px 18px rgba(93,20,51,.14);
  backdrop-filter: blur(8px);
}}
.lang-toggle button {{
  border: 0;
  background: transparent;
  color: var(--muted);
  padding: 7px 13px;
  border-radius: 999px;
  font: 600 11px 'Poppins', sans-serif;
  cursor: pointer;
  transition: all .25s ease;
}}
.lang-toggle button.active {{
  background: linear-gradient(135deg, var(--pink), #D64D87);
  color: #fff;
  box-shadow: 0 3px 8px rgba(227,28,121,.3);
}}

.es {{ display: inline; }}
.en {{ display: none; }}
body.lang-en .es {{ display: none; }}
body.lang-en .en {{ display: inline; }}

/* ===== Hero section ===== */
.hero {{
  margin-top: 32px;
  position: relative;
  overflow: hidden;
  border-radius: 30px;
  padding: 24px 20px 22px;
  background: rgba(255,246,248,.82);
  border: 1.5px solid rgba(184,18,95,.18);
  box-shadow: var(--shadow);
}}
.hero:after {{
  content: "";
  position: absolute;
  width: 190px;
  height: 190px;
  border-radius: 50%;
  right: -80px;
  top: -85px;
  border: 20px solid rgba(227,28,121,.08);
  pointer-events: none;
}}

.hero-inner {{
  display: grid;
  grid-template-columns: 1.1fr 1px 1.15fr 0.85fr;
  align-items: center;
  gap: 16px;
  position: relative;
  z-index: 1;
}}

.logo-box {{
  display: flex;
  justify-content: center;
  align-items: center;
}}
.logo-box img {{
  width: 100%;
  max-width: 215px;
  height: auto;
  display: block;
  filter: drop-shadow(0 8px 16px rgba(184,18,95,.15));
  transition: transform .3s ease;
}}
.logo-box img:hover {{
  transform: scale(1.03);
}}

.hero-divider {{
  width: 1px;
  height: 115px;
  background: linear-gradient(var(--gold), var(--pink), var(--gold));
  opacity: .75;
}}

.hero-copy {{
  text-align: center;
}}
.hero-copy .small {{
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .24em;
  color: var(--gold);
  font-weight: 700;
  display: block;
}}
.hero-copy h1 {{
  margin: 6px 0 2px;
  font: 500 27px/1.12 'Alex Brush', cursive;
  color: var(--pink-dark);
}}
.hero-copy .studio-name {{
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink);
  margin-bottom: 6px;
}}
.hero-copy p {{
  margin: 0;
  font: italic 600 13.5px/1.38 'Playfair Display', serif;
  color: var(--ink);
}}

/* Hero photo frame: CLEAN, NATURAL COLORS, ZERO PINK MULTIPLY OVERLAY */
.hero-photo {{
  justify-self: end;
  position: relative;
  width: 145px;
  height: 172px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}}
.hero-photo-frame {{
  position: relative;
  width: 145px;
  height: 172px;
  border-radius: 68px 68px 22px 22px;
  overflow: hidden;
  background: #ffffff;
  border: 3.5px solid #ffffff;
  box-shadow: 0 10px 24px rgba(184,18,95,.18), 0 0 0 2px rgba(215,163,60,.55);
}}
.hero-photo-frame img {{
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  display: block;
  /* NATURAL, UNALTERED COLOR — NO MULTIPLY FILTER */
  mix-blend-mode: normal !important;
}}

.badge {{
  position: absolute;
  right: -4px;
  bottom: 8px;
  z-index: 4;
  background: #ffffff;
  color: var(--pink-dark);
  border: 1.5px solid rgba(184,18,95,.25);
  border-radius: 999px;
  padding: 4px 10px;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.05em;
  box-shadow: 0 5px 14px rgba(100,20,50,.15);
}}

.tagline-band {{
  margin: 14px 0 0;
  padding: 12px 18px;
  text-align: center;
  border-radius: 18px;
  background: linear-gradient(90deg, rgba(227,28,121,.10), rgba(215,163,60,.14), rgba(227,28,121,.10));
  border: 1px solid rgba(184,18,95,.14);
}}
.tagline-band strong {{
  color: var(--pink-dark);
  font: italic 16.5px 'Playfair Display', serif;
}}

/* ===== Section common ===== */
.section {{
  margin-top: 28px;
}}
.section-head {{
  text-align: center;
  margin-bottom: 16px;
}}
.section-head .eyebrow {{
  display: block;
  font-size: 9.5px;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 700;
  margin-bottom: 4px;
}}
.section-head h2 {{
  margin: 0;
  color: var(--pink-dark);
  font: 700 24px 'Playfair Display', serif;
}}
.section-head p {{
  max-width: 540px;
  margin: 6px auto 0;
  color: var(--muted);
  font-size: 12px;
  line-height: 1.55;
}}

/* ===== PACKAGES / SERVICIOS SECTION ===== */
.packages-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  margin-top: 14px;
}}

.package-card {{
  position: relative;
  border-radius: 24px;
  background: rgba(255, 250, 252, 0.90);
  border: 1.5px solid rgba(184, 18, 95, 0.18);
  box-shadow: 0 10px 28px rgba(137, 32, 76, 0.10);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.28s ease, box-shadow 0.28s ease;
}}
.package-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 16px 36px rgba(137, 32, 76, 0.16);
}}

.package-header {{
  padding: 16px 14px 14px;
  text-align: center;
  position: relative;
  overflow: hidden;
  color: #fff;
}}

.package-card.business .package-header {{
  background: linear-gradient(135deg, #1C0A17 0%, #3B1127 50%, #B8125F 100%);
  border-bottom: 2px solid var(--gold);
}}

.package-card.events .package-header {{
  background: linear-gradient(135deg, #6C0E3D 0%, #B8125F 50%, #E91E79 100%);
  border-bottom: 2px solid var(--gold);
}}

.package-badge {{
  display: inline-block;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 999px;
  background: rgba(215, 163, 60, 0.25);
  color: #FFE599;
  border: 1px solid rgba(215, 163, 60, 0.55);
  margin-bottom: 6px;
}}

.package-title {{
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: 21px;
  font-weight: 700;
  color: #ffffff;
  text-shadow: 0 2px 8px rgba(0,0,0,0.35);
}}

.package-subtitle {{
  font-size: 10.5px;
  color: #FBECEF;
  margin-top: 4px;
  line-height: 1.35;
  opacity: .95;
}}

.package-body {{
  padding: 15px 14px 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

.package-list {{
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 7.5px;
}}

.package-list li {{
  font-size: 11.5px;
  line-height: 1.38;
  color: var(--ink);
  display: flex;
  align-items: flex-start;
  gap: 8px;
}}

.pkg-check {{
  width: 18px;
  height: 18px;
  border-radius: 50%;
  flex: 0 0 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--pink), var(--gold));
  color: #ffffff;
  font-size: 10.5px;
  font-weight: bold;
  box-shadow: 0 2px 6px rgba(227, 28, 121, 0.28);
  margin-top: 1px;
}}

.package-footer-note {{
  margin-top: 14px;
  padding: 9px 11px;
  border-radius: 12px;
  background: rgba(215, 163, 60, 0.12);
  border: 1px dashed rgba(215, 163, 60, 0.5);
  font-size: 10.5px;
  font-weight: 600;
  color: #8C2153;
  display: flex;
  align-items: center;
  gap: 7px;
}}

.package-cta {{
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 22px;
  border-radius: 999px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.02em;
  color: #ffffff;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease, filter 0.25s ease;
  position: relative;
  overflow: hidden;
}}
.package-cta svg {{
  width: 21px;
  height: 21px;
  flex: 0 0 21px;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.25));
}}
.package-card.business .package-cta {{
  background: linear-gradient(135deg, #1C0A17 0%, #3B1127 45%, #B8125F 100%);
  border: 1.5px solid rgba(215, 163, 60, 0.55);
  box-shadow: 0 6px 20px rgba(184, 18, 95, 0.35), 0 2px 6px rgba(0,0,0,0.18);
}}
.package-card.events .package-cta {{
  background: linear-gradient(135deg, #A80D55 0%, #D81B73 50%, #FF2E8C 100%);
  border: 1.5px solid rgba(255, 235, 170, 0.55);
  box-shadow: 0 6px 20px rgba(233, 30, 121, 0.40), 0 2px 6px rgba(0,0,0,0.18);
}}
.package-cta:hover {{
  transform: translateY(-3px) scale(1.02);
  filter: brightness(1.08);
}}
.package-card.business .package-cta:hover {{
  box-shadow: 0 10px 28px rgba(184, 18, 95, 0.50), 0 0 0 3px rgba(215, 163, 60, 0.35);
}}
.package-card.events .package-cta:hover {{
  box-shadow: 0 10px 28px rgba(233, 30, 121, 0.55), 0 0 0 3px rgba(255, 235, 170, 0.4);
}}
.package-cta:active {{
  transform: translateY(0) scale(0.98);
}}

/* Flyer banner & CTA */
.flyer-banner {{
  margin: 18px 0 0;
  padding: 16px 18px;
  border-radius: 22px;
  background: linear-gradient(135deg, rgba(233,30,121,.10), rgba(215,163,60,.16), rgba(233,30,121,.10));
  border: 1.5px solid rgba(215, 163, 60, 0.45);
  text-align: center;
  box-shadow: 0 6px 18px rgba(184, 18, 95, 0.08);
}}

.flyer-banner-quote {{
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-weight: 700;
  font-size: 16px;
  color: var(--pink-dark);
  margin-bottom: 8px;
}}

.flyer-actions {{
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 12px;
}}

.btn-flyer-modal, .btn-flyer-quote {{
  padding: 13px 24px;
  border-radius: 999px;
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
  border: none;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  text-decoration: none;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.btn-flyer-modal {{
  background: #ffffff;
  color: var(--pink-dark);
  border: 1.5px solid rgba(184,18,95,.35);
  box-shadow: 0 4px 14px rgba(184,18,95,.12);
}}
.btn-flyer-modal:hover {{
  background: #FFF5F8;
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 8px 22px rgba(184,18,95,.22);
}}

.btn-flyer-quote {{
  background: linear-gradient(135deg, var(--pink), #D64D87);
  color: #ffffff;
  border: 1.5px solid rgba(255, 235, 170, 0.45);
  box-shadow: 0 6px 20px rgba(227,28,121,.35);
}}
.btn-flyer-quote:hover {{
  transform: translateY(-3px) scale(1.02);
  filter: brightness(1.08);
  box-shadow: 0 10px 28px rgba(227,28,121,.48);
}}

/* ===== Modal for flyer ===== */
.flyer-modal {{
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(28, 10, 22, 0.88);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}}
.flyer-modal.open {{
  opacity: 1;
  pointer-events: auto;
}}
.flyer-modal-content {{
  position: relative;
  max-width: 520px;
  width: 100%;
  max-height: 90vh;
  background: #140810;
  border-radius: 24px;
  border: 2px solid var(--gold);
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0,0,0,0.6);
  display: flex;
  flex-direction: column;
  animation: zoomIn 0.3s cubic-bezier(0.18, 0.89, 0.32, 1.28);
}}
@keyframes zoomIn {{
  from {{ transform: scale(0.92); opacity: 0; }}
  to {{ transform: scale(1); opacity: 1; }}
}}

.flyer-modal-content img {{
  width: 100%;
  height: auto;
  max-height: 80vh;
  object-fit: contain;
  display: block;
  background: #000;
}}
.flyer-modal-footer {{
  padding: 10px 14px;
  background: #1C0A17;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.flyer-modal-footer span {{
  font-size: 11px;
  color: #F8DDE5;
}}
.flyer-modal-close {{
  position: absolute;
  top: 10px;
  right: 10px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(0,0,0,0.7);
  color: #fff;
  border: 1.5px solid rgba(255,255,255,0.6);
  font-size: 20px;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: background 0.2s ease, transform 0.2s ease;
}}
.flyer-modal-close:hover {{
  background: var(--pink);
  transform: scale(1.08);
}}

/* ===== Products grid ===== */
.product-grid {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 9px;
}}
.product-card {{
  min-height: 145px;
  padding: 10px 7px 12px;
  text-align: center;
  border-radius: 20px;
  background: rgba(255,250,252,.58);
  border: 1px solid rgba(184,18,95,.13);
  box-shadow: 0 7px 18px rgba(137,32,76,.08);
  transition: .25s ease;
}}
.product-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(137,32,76,.14);
}}
.product-art {{
  height: 82px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 5px;
}}
.product-art svg {{
  width: 82px;
  height: 76px;
  overflow: visible;
  filter: drop-shadow(0 5px 4px rgba(137,32,76,.10));
}}
.product-card strong {{
  display: block;
  font-size: 10.5px;
  color: var(--ink);
}}
.product-card span {{
  display: block;
  font-size: 8.5px;
  color: var(--muted);
  line-height: 1.25;
  margin-top: 2px;
}}

.note {{
  margin: 18px 0 0;
  padding: 15px 17px;
  border-left: 4px solid var(--pink);
  border-radius: 0 17px 17px 0;
  background: rgba(255,250,252,.55);
  color: var(--muted);
  font-size: 11px;
  line-height: 1.65;
}}
.note strong {{
  color: var(--pink-dark);
}}

/* ===== Gallery ===== */
.gallery {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 11px;
}}
.gallery-item {{
  position: relative;
  display: block;
  overflow: hidden;
  border-radius: 19px;
  min-height: 165px;
  background: #f5dce3;
  border: 2px solid rgba(255,255,255,.72);
  box-shadow: 0 8px 20px rgba(137,32,76,.12);
  text-decoration: none;
  animation: rise .65s ease both;
  animation-delay: var(--delay);
}}
.gallery-item img {{
  width: 100%;
  height: 100%;
  min-height: 165px;
  object-fit: cover;
  display: block;
  transition: transform .45s ease;
}}
.gallery-item:hover img {{
  transform: scale(1.06);
}}
.gallery-overlay {{
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 27px 11px 10px;
  color: #fff;
  background: linear-gradient(transparent, rgba(52,22,35,.82));
}}
.gallery-overlay strong {{
  display: block;
  font-size: 11px;
}}
.gallery-overlay span {{
  display: block;
  font-size: 9px;
  opacity: .9;
  margin-top: 2px;
}}

/* ===== Links section ===== */
.links {{
  display: grid;
  gap: 10px;
}}
.link-btn {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  text-decoration: none;
  color: var(--ink);
  background: rgba(255,250,252,.65);
  border: 1px solid rgba(184,18,95,.15);
  border-radius: 17px;
  box-shadow: 0 5px 15px rgba(137,32,76,.07);
  transition: .22s ease;
}}
.link-btn:hover {{
  transform: translateY(-2px);
  background: rgba(255,250,252,.92);
  box-shadow: 0 8px 20px rgba(137,32,76,.12);
}}
.link-left {{
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}}
.icon-solid {{
  width: 42px;
  height: 42px;
  flex: 0 0 42px;
  border-radius: 13px;
  background: var(--pink);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 12px rgba(227,28,121,.22);
}}
.icon-solid svg {{
  width: 19px;
  height: 19px;
}}
.link-title {{
  font-size: 13px;
  font-weight: 700;
}}
.link-sub {{
  font-size: 10.5px;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}
.chevron {{
  color: var(--pink-dark);
  display: flex;
}}
.chevron svg {{
  width: 18px;
}}

/* ===== Footer ===== */
.footer {{
  margin-top: 28px;
  padding: 20px 18px 10px;
  text-align: center;
  border-top: 1px solid rgba(184,18,95,.14);
}}
.loc {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--pink-dark);
}}
.essence {{
  font-size: 10.5px;
  line-height: 1.6;
  color: var(--muted);
  max-width: 440px;
  margin: 8px auto;
}}
.essence strong {{
  color: var(--gold);
}}
.copyright {{
  font-size: 9.5px;
  color: #9c7c86;
  margin: 14px 0 0;
}}

@keyframes rise {{
  from {{ opacity: 0; transform: translateY(16px); }}
  to {{ opacity: 1; transform: none; }}
}}

/* ===== Responsive adjustments ===== */
@media(max-width: 680px) {{
  .page {{ padding-left: 12px; padding-right: 12px; }}
  .hero {{ padding: 22px 14px 18px; margin-top: 48px; }}
  .hero-inner {{
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }}
  .hero-divider {{ display: none; }}
  .logo-box {{
    grid-column: 1;
    grid-row: 1;
    justify-content: center;
  }}
  .logo-box img {{ max-width: 155px; }}
  .hero-photo {{
    grid-column: 2;
    grid-row: 1;
    justify-self: center;
  }}
  .hero-photo, .hero-photo-frame {{ width: 124px; height: 152px; }}
  .hero-copy {{
    grid-column: 1 / -1;
    grid-row: 2;
    padding-top: 10px;
    border-top: 1px dashed rgba(184,18,95,.18);
  }}
  .hero-copy h1 {{ font-size: 24px; }}
  .hero-copy p {{ font-size: 12px; }}
  
  .packages-grid {{
    grid-template-columns: 1fr;
    gap: 16px;
  }}
  .product-grid {{ grid-template-columns: repeat(3, 1fr); }}
}}

@media(max-width: 440px) {{
  .logo-box img {{ max-width: 135px; }}
  .hero-photo, .hero-photo-frame {{ width: 112px; height: 140px; }}
  .product-grid {{ grid-template-columns: repeat(2, 1fr); }}
  .gallery {{ gap: 9px; }}
  .gallery-item, .gallery-item img {{ min-height: 145px; }}
}}

@media(prefers-reduced-motion: reduce) {{
  * {{ animation-duration: .01ms !important; transition: none !important; }}
}}
</style>
</head>

<body>

<div class="lang-toggle">
  <button id="btn-es" class="active" onclick="setLang('es')">ES</button>
  <button id="btn-en" onclick="setLang('en')">EN</button>
</div>

<main class="page">
  <!-- HERO -->
  <header class="hero">
    <div class="hero-inner">
      <div class="logo-box">
        <img src="{logo_b64}" alt="AL Creative Design Studio LLC">
      </div>
      <div class="hero-divider"></div>
      <div class="hero-copy">
        <span class="small"><span class="es">Diseños personalizados</span><span class="en">Custom designs</span></span>
        <h1>Alba Laguna</h1>
        <div class="studio-name">AL Creative</div>
        <p><span class="es">Creamos piezas únicas que conectan con tu estilo, tu marca y tu celebración.</span><span class="en">We create unique pieces that connect with your style, your brand, and your celebration.</span></p>
      </div>
      <div class="hero-photo">
        <div class="hero-photo-frame">
          <img src="{photo_b64}" alt="Alba Laguna — AL Creative">
        </div>
        <span class="badge">AL Creative</span>
      </div>
    </div>
    <div class="tagline-band">
      <strong><span class="es">Tu idea toma vida • Diseños que dejan huella ♡</span><span class="en">Your idea comes to life • Designs that leave a mark ♡</span></strong>
    </div>
  </header>

  <!-- SERVICIOS Y PAQUETES (DESDE EL FLYER OFICIAL) -->
  <section class="section" id="paquetes">
    <div class="section-head">
      <span class="eyebrow"><span class="es">Nuestros Paquetes</span><span class="en">Our Packages</span></span>
      <h2><span class="es">Servicios y Paquetes Especiales</span><span class="en">Special Packages & Services</span></h2>
      <p><span class="es">Diseños personalizados para negocios y momentos especiales. Elige tu paquete o personalízalo a tu medida.</span><span class="en">Custom designs for businesses and special moments. Choose your package or customize it to your needs.</span></p>
    </div>

    <div class="packages-grid">
      <!-- PAQUETE EMPRESARIAL -->
      <div class="package-card business">
        <div class="package-header">
          <span class="package-badge"><span class="es">Negocios & Marcas</span><span class="en">Business & Brands</span></span>
          <h3 class="package-title"><span class="es">Paquete Empresarial</span><span class="en">Business Package</span></h3>
          <div class="package-subtitle"><span class="es">Todo para proyectar tu marca con impacto</span><span class="en">Everything to project your brand with impact</span></div>
        </div>
        <div class="package-body">
          <ul class="package-list">
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Playeras</span><span class="en">T-Shirts</span></strong>: <span class="es">Playera + diseño exclusivo + tu logo</span><span class="en">Tees + custom design + your logo</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Tarjetas de presentación</span><span class="en">Business cards</span></strong>: <span class="es">Impresión profesional y elegante</span><span class="en">Professional elegant printing</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Código QR</span><span class="en">QR Code</span></strong>: <span class="es">Integrado a tus redes, menú o web</span><span class="en">Linked to socials, menu or website</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Taza o Tumbler</span><span class="en">Mug or Tumbler</span></strong>: <span class="es">Con tu logo en alta calidad</span><span class="en">High quality with your logo</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Stickers</span><span class="en">Stickers</span></strong>: <span class="es">Calcomanías troqueladas resistentes</span><span class="en">Durable die-cut stickers</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Llaveros</span><span class="en">Keychains</span></strong>: <span class="es">Personalizados con tu marca</span><span class="en">Customized with your brand</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Gorras</span><span class="en">Caps</span></strong>: <span class="es">Bordadas o con vinil/DTF</span><span class="en">Embroidered or vinyl/DTF</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Mouse pad</span><span class="en">Mouse pad</span></strong>: <span class="es">Con diseño corporativo a full color</span><span class="en">Full color corporate design</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Flyers</span><span class="en">Flyers</span></strong>: <span class="es">Volantes publicitarios llamativos</span><span class="en">Eye-catching promo flyers</span></span></li>
          </ul>

          <div class="package-footer-note">
            <span>💼</span>
            <span><span class="es">Proyecta una imagen profesional y creativa</span><span class="en">Project a professional and creative image</span></span>
          </div>

          <a class="package-cta" href="https://wa.me/14804535638?text=Hola%20Alba,%20me%20interesa%20cotizar%20el%20Paquete%20Empresarial%20de%20AL%20Creative" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.24.66-1.4 1.26-1.94 1.34-.5.08-1.12.11-1.8-.11-.42-.13-.96-.32-1.65-.62-2.9-1.25-4.8-4.18-4.94-4.38-.14-.2-1.18-1.57-1.18-3 0-1.42.75-2.12 1.02-2.41.26-.28.58-.36.77-.36h.55c.18 0 .42-.07.65.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.19-.15.31-.3.48-.15.17-.31.38-.44.51-.15.15-.3.31-.13.6.17.3.76 1.26 1.63 2.04 1.12 1 2.06 1.32 2.36 1.47.3.15.47.13.65-.08.18-.2.75-.87"/></svg>
            <span class="es">Cotizar Paquete Empresarial</span>
            <span class="en">Quote Business Package</span>
          </a>
        </div>
      </div>

      <!-- PAQUETE DE EVENTOS -->
      <div class="package-card events">
        <div class="package-header">
          <span class="package-badge"><span class="es">Celebraciones</span><span class="en">Celebrations</span></span>
          <h3 class="package-title"><span class="es">Paquete de Eventos</span><span class="en">Events Package</span></h3>
          <div class="package-subtitle"><span class="es">Para XV años, bodas, bautizos, graduaciones y más</span><span class="en">For XV years, weddings, baptisms, graduations & more</span></div>
        </div>
        <div class="package-body">
          <ul class="package-list">
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Playeras temáticas</span><span class="en">Themed tees</span></strong>: <span class="es">Para la festejada, corte o familia</span><span class="en">For the honoree, court or family</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Vasos con popote</span><span class="en">Cups with straw</span></strong>: <span class="es">Vasos plásticos personalizados</span><span class="en">Personalized plastic cups</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Llaveros de recuerdo</span><span class="en">Souvenir keychains</span></strong>: <span class="es">Detalle conmemorativo único</span><span class="en">Unique commemorative favor</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Batas de XV años</span><span class="en">XV satin robes</span></strong>: <span class="es">Satín suave con nombre y corona</span><span class="en">Soft satin with name & crown</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Sandalias</span><span class="en">Party sandals</span></strong>: <span class="es">Comodidad personalizada para la pista</span><span class="en">Custom comfort for dancing</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Lentes</span><span class="en">Party glasses</span></strong>: <span class="es">Lentes con estilo para fotos</span><span class="en">Stylish glasses for photo moments</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Gorras</span><span class="en">Caps</span></strong>: <span class="es">Para el festejo y la fiesta</span><span class="en">For the party and celebration</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Pulseras</span><span class="en">Wristbands</span></strong>: <span class="es">Acceso y recuerdo del evento</span><span class="en">Access and event keepsake</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Cake toppers</span><span class="en">Cake toppers</span></strong>: <span class="es">El toque final para tu pastel</span><span class="en">The crowning touch for your cake</span></span></li>
            <li><span class="pkg-check">✓</span><span><strong><span class="es">Stickers</span><span class="en">Stickers</span></strong>: <span class="es">Para recuerditos y cajitas</span><span class="en">For party favors & gift boxes</span></span></li>
          </ul>

          <div class="package-footer-note">
            <span>🎁</span>
            <span><span class="es">Detalles que hacen cada evento aún más especial</span><span class="en">Details that make every event even more special</span></span>
          </div>

          <a class="package-cta" href="https://wa.me/14804535638?text=Hola%20Alba,%20me%20interesa%20cotizar%20el%20Paquete%20de%20Eventos%20de%20AL%20Creative" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.24.66-1.4 1.26-1.94 1.34-.5.08-1.12.11-1.8-.11-.42-.13-.96-.32-1.65-.62-2.9-1.25-4.8-4.18-4.94-4.38-.14-.2-1.18-1.57-1.18-3 0-1.42.75-2.12 1.02-2.41.26-.28.58-.36.77-.36h.55c.18 0 .42-.07.65.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.19-.15.31-.3.48-.15.17-.31.38-.44.51-.15.15-.3.31-.13.6.17.3.76 1.26 1.63 2.04 1.12 1 2.06 1.32 2.36 1.47.3.15.47.13.65-.08.18-.2.75-.87"/></svg>
            <span class="es">Cotizar Paquete de Eventos</span>
            <span class="en">Quote Events Package</span>
          </a>
        </div>
      </div>
    </div>

    <!-- BANNER Y MODAL DEL FLYER -->
    <div class="flyer-banner">
      <div class="flyer-banner-quote">
        <span class="es">Tu idea + nuestra creatividad = resultados que enamoran ♡</span>
        <span class="en">Your idea + our creativity = results you'll love ♡</span>
      </div>
      <div class="flyer-actions">
        <button class="btn-flyer-modal" onclick="openFlyerModal()">
          <span>🖼️</span>
          <span class="es">Ver Flyer Oficial (Foto)</span>
          <span class="en">View Official Flyer</span>
        </button>
        <a class="btn-flyer-quote" href="https://wa.me/14804535638?text=Hola%20Alba,%20quisiera%20preguntar%20por%20mi%20paquete%20ideal%20en%20AL%20Creative" target="_blank" rel="noopener">
          <span>✨</span>
          <span class="es">Pregunta por tu paquete ideal</span>
          <span class="en">Ask about your ideal package</span>
        </a>
      </div>
    </div>
  </section>

  <!-- MODAL LIGHTBOX PARA EL FLYER OFICIAL -->
  <div id="flyerModal" class="flyer-modal" onclick="if(event.target===this)closeFlyerModal()">
    <div class="flyer-modal-content">
      <button class="flyer-modal-close" onclick="closeFlyerModal()" aria-label="Cerrar">×</button>
      <img src="{flyer_b64}" alt="Flyer Oficial de Servicios — AL Creative Design Studio LLC">
      <div class="flyer-modal-footer">
        <span>AL Creative DESIGN STUDIO LLC</span>
        <a class="btn-flyer-quote" style="padding:8px 16px;font-size:12px;font-weight:700;" href="https://wa.me/14804535638?text=Hola%20Alba,%20vi%20el%20flyer%20de%20AL%20Creative%20y%20quiero%20cotizar" target="_blank" rel="noopener">
          <span class="es">Cotizar</span><span class="en">Quote</span>
        </a>
      </div>
    </div>
  </div>

  <!-- LO QUE HACEMOS (PRODUCTOS INDIVIDUALES) -->
  <section class="section">
    <div class="section-head">
      <span class="eyebrow"><span class="es">Lo que hacemos</span><span class="en">What we create</span></span>
      <h2><span class="es">Productos que cuentan historias</span><span class="en">Products that tell stories</span></h2>
      <p><span class="es">Diseños personalizados para personas, familias, negocios, eventos y organizaciones.</span><span class="en">Custom designs for people, families, businesses, events and organizations.</span></p>
    </div>

    <div class="product-grid">
      <div class="product-card">
        <div class="product-art"><svg viewBox="0 0 100 90" aria-label="Playera"><path d="M29 20 13 31l9 13 8-6v34h40V38l8 6 9-13-16-11-9-4H38z" fill="#F39AB8" stroke="#B8125F" stroke-width="3" stroke-linejoin="round"/><path d="M39 17c2 9 20 9 22 0" fill="none" stroke="#fff" stroke-width="3"/><path d="M34 52h32" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M42 48v8m16-8v8" stroke="#D7A33C" stroke-width="2" stroke-linecap="round"/></svg></div>
        <strong><span class="es">Playeras</span><span class="en">T-Shirts</span></strong><span><span class="es">Diseños únicos</span><span class="en">Unique designs</span></span>
      </div>
      <div class="product-card">
        <div class="product-art"><svg viewBox="0 0 100 90" aria-label="Taza"><path d="M24 22h48v42a8 8 0 0 1-8 8H32a8 8 0 0 1-8-8z" fill="#FFF8FA" stroke="#B8125F" stroke-width="3"/><path d="M72 32h8a11 11 0 0 1 0 22h-8" fill="none" stroke="#B8125F" stroke-width="3"/><path d="M33 42h30" stroke="#E91E79" stroke-width="5" stroke-linecap="round"/><path d="M39 35c3-4 7-4 10 0s7 4 10 0" fill="none" stroke="#D7A33C" stroke-width="2"/></svg></div>
        <strong><span class="es">Tazas</span><span class="en">Mugs</span></strong><span><span class="es">Detalles especiales</span><span class="en">Special details</span></span>
      </div>
      <div class="product-card">
        <div class="product-art"><svg viewBox="0 0 100 90" aria-label="Termo"><rect x="34" y="16" width="32" height="59" rx="9" fill="#F2C4D2" stroke="#B8125F" stroke-width="3"/><rect x="40" y="10" width="20" height="10" rx="3" fill="#D7A33C" stroke="#B8125F" stroke-width="2"/><path d="M43 37h14M43 45h14M43 53h10" stroke="#E91E79" stroke-width="3" stroke-linecap="round"/></svg></div>
        <strong><span class="es">Termos</span><span class="en">Tumblers</span></strong><span><span class="es">Personalizados</span><span class="en">Personalized</span></span>
      </div>
      <div class="product-card">
        <div class="product-art"><svg viewBox="0 0 100 90" aria-label="Gorra"><path d="M20 50c2-19 15-29 31-29 15 0 25 10 27 25l-1 7H20z" fill="#F3A7BF" stroke="#B8125F" stroke-width="3"/><path d="M20 51c19 4 42 2 61-4 7-2 13 0 12 5-1 7-22 10-40 10-17 0-30-3-33-6-2-2-2-4 0-5z" fill="#E91E79" stroke="#B8125F" stroke-width="3"/><path d="M46 30h9" stroke="#D7A33C" stroke-width="3" stroke-linecap="round"/></svg></div>
        <strong><span class="es">Gorras</span><span class="en">Caps</span></strong><span><span class="es">Para marcas y eventos</span><span class="en">For brands & events</span></span>
      </div>
      <div class="product-card">
        <div class="product-art"><svg viewBox="0 0 100 90" aria-label="Tarjeta de presentación"><rect x="14" y="22" width="72" height="46" rx="5" fill="#FFF9FB" stroke="#B8125F" stroke-width="3"/><circle cx="31" cy="45" r="9" fill="#F2A5BE"/><path d="M45 38h29M45 45h22M45 52h27" stroke="#E91E79" stroke-width="3" stroke-linecap="round"/><path d="M24 60h50" stroke="#D7A33C" stroke-width="2"/></svg></div>
        <strong><span class="es">Tarjetas</span><span class="en">Business cards</span></strong><span><span class="es">Tu marca presente</span><span class="en">Keep your brand present</span></span>
      </div>
    </div>

    <div class="note">
      <strong><span class="es">Una idea, muchas formas de contarla.</span><span class="en">One idea, many ways to tell it.</span></strong><br>
      <span class="es">Desde ropa personalizada hasta productos promocionales, cada pieza se diseña para que tu historia se vea, se sienta y se recuerde con DTF, sublimación y vinil textil de la más alta calidad.</span>
      <span class="en">From personalized apparel to promotional products, every piece is designed so your story can be seen, felt and remembered with top-grade DTF, sublimation and vinyl.</span>
    </div>
  </section>

  <!-- PORTAFOLIO -->
  <section class="section" id="portfolio">
    <div class="section-head">
      <span class="eyebrow"><span class="es">Portafolio</span><span class="en">Portfolio</span></span>
      <h2><span class="es">Nuestros trabajos</span><span class="en">Our work</span></h2>
      <p><span class="es">Cada pieza, hecha a la medida de una historia distinta.</span><span class="en">Every piece, made to fit a different story.</span></p>
    </div>
    <div class="gallery">
{portfolio_items_html}
    </div>
  </section>

  <!-- ENLACES Y CONTACTO -->
  <section class="section">
    <div class="section-head">
      <span class="eyebrow"><span class="es">Conecta con nosotros</span><span class="en">Connect with us</span></span>
      <h2><span class="es">Síguenos y escríbenos</span><span class="en">Follow & message us</span></h2>
    </div>
    <div class="links">
      <a class="link-btn" href="#paquetes">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 6h-4V4c0-1.1-.9-2-2-2h-4c-1.1 0-2 .9-2 2v2H4c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-10-2h4v2h-4V4zm10 15H4V8h16v11z"/></svg></div><div><div class="link-title"><span class="es">Paquetes y Servicios</span><span class="en">Packages & Services</span></div><div class="link-sub"><span class="es">Empresarial & Eventos especiales</span><span class="en">Business & Special events</span></div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 5v14M5 12l7 7 7-7"/></svg></div>
      </a>
      <a class="link-btn" href="#portfolio">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></div><div><div class="link-title"><span class="es">Portafolio</span><span class="en">Portfolio</span></div><div class="link-sub"><span class="es">Mira nuestros trabajos</span><span class="en">See our work</span></div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 5v14M5 12l7 7 7-7"/></svg></div>
      </a>
      <a class="link-btn" href="https://wa.me/14804535638" target="_blank" rel="noopener">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.24.66-1.4 1.26-1.94 1.34-.5.08-1.12.11-1.8-.11-.42-.13-.96-.32-1.65-.62-2.9-1.25-4.8-4.18-4.94-4.38-.14-.2-1.18-1.57-1.18-3 0-1.42.75-2.12 1.02-2.41.26-.28.58-.36.77-.36h.55c.18 0 .42-.07.65.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.19-.15.31-.3.48-.15.17-.31.38-.44.51-.15.15-.3.31-.13.6.17.3.76 1.26 1.63 2.04 1.12 1 2.06 1.32 2.36 1.47.3.15.47.13.65-.08.18-.2.75-.87"/></svg></div><div><div class="link-title">WhatsApp</div><div class="link-sub">(480) 453-5638</div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 5l7 7-7-7"/></svg></div>
      </a>
      <a class="link-btn" href="https://www.instagram.com/a.lagunacreatingtshirts?igsh=cTl6bDZwcDJmZHB1&utm_source=qr" target="_blank" rel="noopener">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1"/></svg></div><div><div class="link-title">Instagram</div><div class="link-sub">@a.lagunacreatingtshirts</div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 5l7 7-7-7"/></svg></div>
      </a>
      <a class="link-btn" href="https://www.tiktok.com/@creandoconalba1?_r=1&_t=ZP-98bt0Zp6vPC" target="_blank" rel="noopener">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.5 3c.4 2.2 2 3.9 4.5 4.2v3c-1.6 0-3.1-.5-4.5-1.4v6.7c0 3.6-2.9 6.5-6.5 6.5S3.5 19.1 3.5 15.5c0-3.5 2.7-6.3 6.1-6.5v3.1c-1.7.2-3 1.6-3 3.4 0 1.9 1.6 3.5 3.5 3.5s3.5-1.6 3.5-3.5V3h3z"/></svg></div><div><div class="link-title">TikTok</div><div class="link-sub">@creandoconalba1</div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 5l7 7-7-7"/></svg></div>
      </a>
      <a class="link-btn" href="https://www.facebook.com/share/1CMc4EvxWs/?mibextid=wwXIfr" target="_blank" rel="noopener">
        <div class="link-left"><div class="icon-solid"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V8c0-.9.25-1.5 1.55-1.5H17V3.7C16.6 3.65 15.5 3.55 14.2 3.55c-2.7 0-4.5 1.65-4.5 4.65V10H7v3.1h2.7V21h3.8z"/></svg></div><div><div class="link-title">Facebook</div><div class="link-sub">Alba Laguna</div></div></div>
        <div class="chevron"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 5l7 7-7-7"/></svg></div>
      </a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="loc"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>Glendale, Arizona</div>
    <p class="essence"><span class="es"><strong>Nuestra esencia:</strong> creatividad, calidad y pasión en cada diseño.</span><span class="en"><strong>Our essence:</strong> creativity, quality and passion in every design.</span></p>
    <p class="copyright">© 2026 AL Creative Design Studio LLC — Alba Laguna</p>
  </footer>
</main>

<script>
function setLang(lang){{
  document.body.classList.toggle('lang-en', lang === 'en');
  document.getElementById('btn-es').classList.toggle('active', lang === 'es');
  document.getElementById('btn-en').classList.toggle('active', lang === 'en');
  document.documentElement.lang = lang;
}}

function openFlyerModal(){{
  var modal = document.getElementById('flyerModal');
  if(modal) modal.classList.add('open');
}}

function closeFlyerModal(){{
  var modal = document.getElementById('flyerModal');
  if(modal) modal.classList.remove('open');
}}

document.addEventListener('keydown', function(e){{
  if(e.key === 'Escape') closeFlyerModal();
}});
</script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated index.html! Total length: {len(html_content)} characters")
