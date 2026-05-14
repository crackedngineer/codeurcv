import re

_PREAMBLE = """\
#set document(title: "Resume")
#set page(paper: "us-letter", margin: (x: 0.5in, y: 0.5in))
#set text(size: 11pt)
#set list(indent: 8pt)
#set par(spacing: 0.6em)

#show heading.where(level: 1): h => align(center)[
  #v(4pt)
  #text(size: 22pt, weight: "bold")[#h.body]
  #v(2pt)
]
#show heading.where(level: 2): h => [
  #v(8pt)
  #text(size: 11pt, weight: "bold")[#upper[#h.body]]
  #line(length: 100%, stroke: 0.5pt + black)
  #v(3pt)
]
#show heading.where(level: 3): h => [
  #text(size: 11pt, weight: "bold")[#h.body]
]

"""

_TYPST_ESCAPE = re.compile(r"([$\\@])")

# Matches **[text](url)** (bold link) or [text](url) (plain link)
_LINK_RE = re.compile(r"(\*\*)?\[([^\]]*)\]\(([^)]*)\)(\*\*)?")


def _escape_typst(text: str) -> str:
    return _TYPST_ESCAPE.sub(r"\\\1", text)


def _convert_spans(text: str) -> str:
    """Convert bold/italic in plain text and escape Typst specials."""
    text = re.sub(r"\*\*(.+?)\*\*", r"*\1*", text)
    parts = re.split(r"(\*[^*]+\*|_[^_]+_)", text)
    result = []
    for part in parts:
        if part.startswith(("*", "_")) and part.endswith(("*", "_")):
            result.append(part)
        else:
            result.append(_escape_typst(part))
    return "".join(result)


def _convert_inline(text: str) -> str:
    """Convert inline Markdown → Typst.

    Handles **[text](url)** (bold link) and [text](url) (plain link) as units
    so surrounding bold markers aren't left as orphaned ** fragments.
    """
    parts: list[str] = []
    last_end = 0
    for m in _LINK_RE.finditer(text):
        parts.append(_convert_spans(text[last_end : m.start()]))
        display = _convert_spans(m.group(2))
        url = m.group(3)
        if m.group(1):  # leading **
            parts.append(f'#link("{url}")[*{display}*]')
        else:
            parts.append(f'#link("{url}")[{display}]')
        last_end = m.end()
    parts.append(_convert_spans(text[last_end:]))
    return "".join(parts)


def convert(markdown: str, preamble: str = _PREAMBLE) -> str:
    """Return a complete Typst document (preamble + body) from a Markdown string."""
    lines = markdown.splitlines()
    out: list[str] = [preamble]
    for line in lines:
        if line.startswith("### "):
            out.append(f"=== {_convert_inline(line[4:].strip())}\n")
        elif line.startswith("## "):
            out.append(f"== {_convert_inline(line[3:].strip())}\n")
        elif line.startswith("# "):
            out.append(f"= {_convert_inline(line[2:].strip())}\n")
        elif line.strip() == "---":
            out.append("#line(length: 100%, stroke: 0.5pt)\n")
        elif line.startswith("- "):
            out.append(f"- {_convert_inline(line[2:])}\n")
        elif line.strip() == "":
            out.append("\n")
        else:
            out.append(_convert_inline(line) + "\n")
    return "".join(out)
