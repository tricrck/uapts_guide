#!/usr/bin/env python3
"""Render the Markdown user guide to static HTML next to each .md file.

Usage:  python3 docs/guide/_tools/build_site.py
Needs:  pip install markdown
The .md files are the source of truth; re-run after editing them.
Open docs/guide/index.html in a browser - no server needed.
"""
import html, os, re
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_URL = "https://uapts.transport.go.ke/uapts-logo.png"

# Lucide-style stroke icons (24x24 grid)
ICONS = {
    "panel": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'{ICONS[name]}</svg>')


def title_of(md):
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else "UAPTS User Guide"


def collect():
    pages = {}
    for d, _, fs in os.walk(ROOT):
        if "_tools" in d:
            continue
        for f in fs:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(d, f), ROOT)[:-3].replace(os.sep, "/")
                pages[rel] = open(os.path.join(d, f), encoding="utf-8").read()
    return pages


def sidebar_spec(pages):
    """Parse _sidebar.md (nested bullet list of [label](path.md) or **Group**)."""
    out = []
    for line in open(os.path.join(ROOT, "_sidebar.md"), encoding="utf-8"):
        m = re.match(r"^(\s*)[-*]\s+(?:\[([^\]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*|(.+))$", line.rstrip())
        if not m:
            continue
        depth = len(m.group(1)) // 2
        if m.group(2):
            target = m.group(3)[:-3] if m.group(3).endswith(".md") else m.group(3)
            out.append((depth, m.group(2), target))
        else:
            out.append((depth, (m.group(4) or m.group(5)).strip(), None))
    return out


def build_tree(spec):
    """Turn the flat (depth, label, target) list into nested sections and links."""
    root = []
    stack = [(-1, root)]
    for depth, label, target in spec:
        node = {"label": label, "target": target, "children": []}
        while stack[-1][0] >= depth:
            stack.pop()
        stack[-1][1].append(node)
        if target is None:
            stack.append((depth, node["children"]))
    return root


def render_nodes(nodes, rel, base):
    out = []
    for n in nodes:
        label = html.escape(n["label"])
        if n["target"] is None:
            kids = render_nodes(n["children"], rel, base)
            key = html.escape(n["label"], quote=True)
            out.append(
                f'<section class="sec" data-key="{key}">'
                f'<button class="sec-h" type="button" aria-expanded="true">{icon("chevron", "chev")}'
                f'<span>{label}</span></button>'
                f'<div class="sec-b"><div class="sec-i">{kids}</div></div></section>'
            )
        else:
            cls = "link cur" if n["target"] == rel else "link"
            out.append(f'<a class="{cls}" href="{base}{n["target"]}.html">{icon("file")}<span>{label}</span></a>')
    return "".join(out)


CSS = """
:root{--brand:#0f4c8a;--gold:#f2b705;--bg:#fff;--fg:#1c2733;--muted:#5b6b7b;--line:#e3e8ee;
--side:#f6f8fb;--code:#f1f4f8;--hover:#e6eef8;--side-w:288px;--toc-w:220px;--hdr:56px;--ease:cubic-bezier(.4,0,.2,1)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font:clamp(14px,1.5vw,15.5px)/1.65 Inter,system-ui,"Segoe UI",Roboto,sans-serif;color:var(--fg);background:var(--bg);overflow-x:hidden}
a{color:var(--brand)}
img{max-width:100%;height:auto}

/* Header */
header{position:sticky;top:0;z-index:20;height:var(--hdr);background:var(--brand);color:#fff;border-bottom:3px solid var(--gold);
display:flex;align-items:center;gap:12px;padding:0 clamp(10px,2vw,20px)}
.iconbtn{background:transparent;border:0;color:#fff;width:38px;height:38px;border-radius:8px;display:grid;place-items:center;cursor:pointer;flex:none;transition:background .2s}
.iconbtn:hover{background:rgba(255,255,255,.16)}
.ic{width:20px;height:20px;flex:none}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;min-width:0}
.logo{height:34px;width:auto;background:#fff;border-radius:6px;padding:3px 6px;display:block;flex:none}
.brand b{font-weight:700;letter-spacing:.04em;white-space:nowrap}
.brand small{opacity:.8;font-weight:400;white-space:nowrap}
.search{margin-left:auto;position:relative;display:flex;align-items:center;min-width:0;width:clamp(130px,28vw,300px)}
.search .ic{position:absolute;left:9px;color:var(--muted);pointer-events:none;width:16px;height:16px}
#q{width:100%;padding:7px 12px 7px 32px;border-radius:8px;border:0;font:inherit;font-size:14px;color:var(--fg);background:#fff;min-width:0}
#q:focus{outline:2px solid var(--gold)}

/* Layout */
.layout{display:grid;grid-template-columns:var(--side-w) minmax(0,1fr) var(--toc-w);max-width:1600px;margin:0 auto;
transition:grid-template-columns .3s var(--ease)}
body.nav-off{--side-w:0px}

/* Sidebar */
nav.side{position:sticky;top:var(--hdr);height:calc(100vh - var(--hdr));overflow:hidden;background:var(--side);transition:width .3s var(--ease)}
nav.side .scroll{position:relative;width:var(--side-w-inner,288px);height:100%;overflow:auto;padding:10px 10px 60px;font-size:13.5px;
border-right:1px solid var(--line);background:var(--side)}
body.nav-off nav.side .scroll{border-right-color:transparent}
.sec-h{all:unset;box-sizing:border-box;display:flex;align-items:center;gap:6px;width:100%;padding:8px 10px;margin-top:8px;cursor:pointer;
color:var(--brand);font-weight:700;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;border-radius:7px;transition:background .2s}
.sec-h:hover{background:var(--hover)}
.sec-h:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
.chev{width:15px;height:15px;transition:transform .28s var(--ease)}
.sec.closed .chev{transform:rotate(-90deg)}
.sec-b{display:grid;grid-template-rows:1fr;transition:grid-template-rows .28s var(--ease)}
.sec.closed .sec-b{grid-template-rows:0fr}
.sec-i{min-height:0;overflow:hidden}
.sec .sec .sec-h{font-size:11px;padding-left:20px}
.link{display:flex;align-items:center;gap:9px;padding:6px 10px 6px 14px;margin:1px 0;border-radius:7px;color:var(--fg);text-decoration:none;
transition:background .2s,color .2s,transform .2s}
.link .ic{width:16px;height:16px;color:var(--muted);transition:color .2s}
.link span{min-width:0;overflow-wrap:anywhere}
.link:hover{background:var(--hover);transform:translateX(2px)}
.link.cur{background:var(--brand);color:#fff}
.link.cur .ic{color:var(--gold)}
.sec-i .sec-i .link{padding-left:26px}
.hide{display:none!important}
nav.side.filtering .sec .sec-b{grid-template-rows:1fr}
nav.side.filtering .sec .chev{transform:none}

/* Main */
main{min-width:0;padding:clamp(18px,3vw,40px) clamp(16px,4vw,56px) 80px}
main h1{font-size:clamp(24px,3.4vw,32px);margin:0 0 4px;line-height:1.2}
main h2{margin-top:36px;padding-bottom:6px;border-bottom:1px solid var(--line);line-height:1.3}
main h3{margin-top:26px}
main img{border:1px solid var(--line);border-radius:8px;margin:10px 0;box-shadow:0 2px 8px rgba(0,0,0,.06)}
main table{display:block;overflow:auto;max-width:100%;border-collapse:collapse;font-size:13.5px;margin:12px 0}
main th,main td{border:1px solid var(--line);padding:6px 10px;vertical-align:top;text-align:left}
main th{background:var(--side)}
main blockquote{margin:14px 0;padding:10px 16px;border-left:4px solid var(--gold);background:#fffbea;color:#4a3b00}
main pre{max-width:100%;overflow-x:auto;background:var(--code);padding:12px;border-radius:8px}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:90%;overflow-wrap:anywhere}
main pre code{background:none;padding:0}

/* On this page */
aside.toc{position:sticky;top:var(--hdr);height:calc(100vh - var(--hdr));overflow:auto;padding:28px 14px;font-size:13px}
aside.toc b{display:block;margin-bottom:6px;color:var(--muted);text-transform:uppercase;font-size:11px;letter-spacing:.06em}
aside.toc a{display:block;color:var(--muted);text-decoration:none;padding:2px 0}
aside.toc a:hover{color:var(--brand)}

.scrim{display:none}

/* Tablet: hide the TOC */
@media (max-width:1180px){
  .layout{grid-template-columns:var(--side-w) minmax(0,1fr)}
  aside.toc{display:none}
}

/* Phone: sidebar becomes an off-canvas drawer */
@media (max-width:860px){
  .layout{grid-template-columns:minmax(0,1fr)}
  .brand small{display:none}
  nav.side{position:fixed;top:var(--hdr);left:0;bottom:0;height:auto;width:min(86vw,320px);z-index:15;
  transform:translateX(-102%);transition:transform .3s var(--ease);box-shadow:0 0 24px rgba(0,0,0,.2)}
  nav.side .scroll{width:100%;border-right:0}
  body.nav-open nav.side{transform:none}
  body.nav-open .scrim{display:block;position:fixed;inset:var(--hdr) 0 0 0;background:rgba(10,20,30,.4);z-index:14}
  main{padding:18px 16px 60px}
}

@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

JS = """
const body=document.body, mq=matchMedia('(max-width:860px)');
const q=document.getElementById('q'), nav=document.querySelector('nav.side'), scroller=document.querySelector('nav.side .scroll');
const NAV_KEY='uapts-nav', SEC='uapts-sec:';

// Sidebar open/close (desktop collapses the column, phone toggles the drawer)
if(!mq.matches && localStorage.getItem(NAV_KEY)==='off') body.classList.add('nav-off');
function toggleNav(){
  if(mq.matches){ body.classList.toggle('nav-open'); return; }
  body.classList.toggle('nav-off');
  try{ localStorage.setItem(NAV_KEY, body.classList.contains('nav-off')?'off':'on'); }catch(e){}
}
document.getElementById('navbtn').addEventListener('click', toggleNav);
document.getElementById('scrim').addEventListener('click', ()=>body.classList.remove('nav-open'));
mq.addEventListener('change', ()=>body.classList.remove('nav-open'));
document.addEventListener('keydown', e=>{
  if((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='k'){
    e.preventDefault();
    if(mq.matches){ body.classList.add('nav-open'); }
    else if(body.classList.contains('nav-off')){ toggleNav(); }
    q.focus(); q.select();
  }
  if(e.key==='Escape') body.classList.remove('nav-open');
});
document.querySelectorAll('nav.side a.link').forEach(a=>a.addEventListener('click', ()=>{
  if(mq.matches) body.classList.remove('nav-open');
}));

// Collapsible sections, remembered per section
document.querySelectorAll('nav.side section.sec').forEach(s=>{
  const h=s.querySelector('.sec-h'), key=SEC+s.dataset.key;
  let closed=false; try{ closed=localStorage.getItem(key)==='1'; }catch(e){}
  if(s.querySelector('a.cur')) closed=false;
  s.classList.toggle('closed', closed);
  h.setAttribute('aria-expanded', String(!closed));
  h.addEventListener('click', ()=>{
    const c=!s.classList.contains('closed');
    s.classList.toggle('closed', c);
    h.setAttribute('aria-expanded', String(!c));
    try{ localStorage.setItem(key, c?'1':'0'); }catch(e){}
  });
});

// Filter pages; while filtering, every matching section is shown open
q.addEventListener('input', ()=>{
  const v=q.value.trim().toLowerCase();
  nav.classList.toggle('filtering', !!v);
  document.querySelectorAll('nav.side a.link').forEach(a=>
    a.classList.toggle('hide', !!v && !a.textContent.toLowerCase().includes(v)));
  document.querySelectorAll('nav.side section.sec').forEach(s=>
    s.classList.toggle('hide', ![...s.querySelectorAll('a.link')].some(a=>!a.classList.contains('hide'))));
});

// Keep the current page visible in the sidebar without scrolling the page
const cur=document.querySelector('nav.side a.cur');
if(cur && scroller) scroller.scrollTop = cur.offsetTop - scroller.clientHeight/2;
"""


def render(pages):
    spec = sidebar_spec(pages)
    tree = build_tree(spec)
    for rel, md in pages.items():
        base = "../" * rel.count("/")
        nav = render_nodes(tree, rel, base)
        mdx = markdown.Markdown(
            extensions=["tables", "toc", "fenced_code", "sane_lists", "attr_list"],
            extension_configs={"toc": {"toc_depth": "2-3"}},
        )
        body = mdx.convert(md)
        body = re.sub(r'href="([^":]+?)\.md(#[^"]*)?"',
                      lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', body)
        toc = "".join(f'<a href="#{t["id"]}">{html.escape(t["name"])}</a>'
                      for t in mdx.toc_tokens if t["level"] == 2)
        page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><link rel="icon" href="{LOGO_URL}">
<title>{html.escape(title_of(md))} - UAPTS User Guide</title><style>{CSS}</style></head><body>
<header>
  <button class="iconbtn" id="navbtn" type="button" aria-label="Toggle sidebar" aria-controls="sidenav">{icon("panel")}</button>
  <a class="brand" href="{base}index.html">
    <img class="logo" src="{LOGO_URL}" alt="UAPTS" onerror="this.remove()">
    <span><b>UAPTS</b> <small>User Guide</small></span>
  </a>
  <label class="search">{icon("search")}<input id="q" type="search" placeholder="Filter pages (Ctrl K)" aria-label="Filter pages"></label>
</header>
<div class="layout">
  <nav class="side" id="sidenav"><div class="scroll">{nav}</div></nav>
  <main>{body}</main>
  <aside class="toc"><b>On this page</b>{toc}</aside>
</div>
<div class="scrim" id="scrim"></div>
<script>{JS}</script></body></html>"""
        out = os.path.join(ROOT, rel + ".html")
        open(out, "w", encoding="utf-8").write(page)
    # landing page
    if "README" in pages:
        open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
            open(os.path.join(ROOT, "README.html"), encoding="utf-8").read())


if __name__ == "__main__":
    pgs = collect()
    render(pgs)
    print("rendered", len(pgs), "pages ->", ROOT)