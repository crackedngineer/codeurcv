// Modern resume template — teal accent, clean hierarchy
#set document(title: "Resume")
#set page(paper: "us-letter", margin: (x: 0.6in, top: 0.5in, bottom: 0.5in))
#set text(size: 10.5pt)
#set list(marker: "–", indent: 10pt, body-indent: 6pt)
#set par(spacing: 0.5em, leading: 0.65em)

#let accent = rgb("#2E86AB")
#let subtle = rgb("#666666")

#show heading.where(level: 2): h => {
  v(9pt)
  text(fill: accent, weight: "bold", size: 11.5pt)[#upper[#h.body]]
  v(1pt)
}

// ── Header ──────────────────────────────────────────────────────────────────
#text(size: 26pt, weight: "bold", fill: accent)[{{ basic_details.name | typst_escape }}]
#v(-2pt)
#line(length: 100%, stroke: 1.5pt + accent)
#v(3pt)
#text(size: 10pt, fill: subtle)[
  {% set parts = [] %}
  {% if basic_details.email %}{% set _ = parts.append("#link(\"mailto:" ~ basic_details.email ~ "\")[" ~ (basic_details.email | typst_escape) ~ "]") %}{% endif %}
  {% if basic_details.phone %}{% set _ = parts.append("#link(\"tel:" ~ basic_details.phone ~ "\")[" ~ (basic_details.phone | typst_escape) ~ "]") %}{% endif %}
  {% if basic_details.github %}{% set _ = parts.append("#link(\"" ~ basic_details.github ~ "\")[" ~ (basic_details.github | typst_escape) ~ "]") %}{% endif %}
  {% if basic_details.linkedin %}{% set _ = parts.append("#link(\"" ~ basic_details.linkedin ~ "\")[" ~ (basic_details.linkedin | typst_escape) ~ "]") %}{% endif %}
  {{ parts | join("  |  ") }}
]

#v(8pt)

{% if summary %}
// ── Summary ─────────────────────────────────────────────────────────────────
== Summary

{{ summary | typst_escape }}

{% endif %}
{% if work %}
// ── Experience ──────────────────────────────────────────────────────────────
== Experience

{% for job in work %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ job.company | typst_escape }}*{% if job.location %} #h(4pt)#text(fill: subtle)[{{ job.location | typst_escape }}]{% endif %}],
  align(right)[#text(fill: accent, weight: "bold")[{{ job.start | typst_escape }} -- {{ job.end | typst_escape }}]],
)
#v(-3pt)
#text(style: "italic")[{{ job.role | typst_escape }}]
#v(3pt)
{% for item in job.achievements %}
- {{ item | typst_escape }}
{% endfor %}
{% if job.technologies %}
#v(1pt)#text(size: 10pt, fill: subtle)[{{ job.technologies | join(" · ") | typst_escape }}]
{% endif %}
#v(6pt)
{% endfor %}
{% endif %}
{% if projects %}
// ── Projects ────────────────────────────────────────────────────────────────
== Projects

{% for proj in projects %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [{% if proj.link %}#link("{{ proj.link }}")[#text(fill: accent, weight: "bold")[{{ proj.name | typst_escape }}]]{% else %}*{{ proj.name | typst_escape }}*{% endif %}{% if proj.technologies %} #h(4pt)#text(fill: subtle, size: 10pt)[{{ proj.technologies | join(" · ") | typst_escape }}]{% endif %}],
  align(right)[#text(fill: subtle)[{{ proj.start | typst_escape }} -- {{ proj.end | typst_escape }}]],
)
#v(2pt)
{% for item in proj.description %}
- {{ item | typst_escape }}
{% endfor %}
#v(5pt)
{% endfor %}
{% endif %}
{% if education %}
// ── Education ───────────────────────────────────────────────────────────────
== Education

{% for school in education %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ school.institution | typst_escape }}*],
  align(right)[#text(fill: accent, weight: "bold")[{{ school.year }}]],
)
#v(-3pt)
#text(fill: subtle)[{{ school.degree | typst_escape }}{% if school.gpa %} — GPA: {{ school.gpa | typst_escape }}{% endif %}]
#v(6pt)
{% endfor %}
{% endif %}
{% if skills %}
// ── Skills ──────────────────────────────────────────────────────────────────
== Technical Skills

{% for skill in skills %}
#text(fill: accent, weight: "bold")[{{ skill.category | typst_escape }}] #h(4pt) {{ skill.featured | join("  ·  ") | typst_escape }} \
{% endfor %}
{% endif %}
