// Classic professional resume template — serif, navy headers
#set document(title: "Resume")
#set page(paper: "us-letter", margin: (x: 0.75in, top: 0.6in, bottom: 0.6in))
#set text(font: "New Computer Modern", size: 11pt)
#set list(marker: "▸", indent: 10pt, body-indent: 6pt)
#set par(spacing: 0.55em, leading: 0.7em)

#let navy = rgb("#1F3864")

#show heading.where(level: 2): h => {
  v(10pt)
  text(fill: navy, weight: "bold", size: 12pt)[#h.body]
  v(-5pt)
  line(length: 100%, stroke: 1.2pt + navy)
  v(4pt)
}

// ── Header ──────────────────────────────────────────────────────────────────
#align(center)[
  #text(size: 24pt, weight: "bold", font: "New Computer Modern")[{{ basic_details.name | typst_escape }}]
  #v(2pt)
  #text(size: 10pt, fill: rgb("#444444"))[
    {% set parts = [] %}
    {% if basic_details.email %}{% set _ = parts.append("#link(\"mailto:" ~ basic_details.email ~ "\")[" ~ (basic_details.email | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.phone %}{% set _ = parts.append("#link(\"tel:" ~ basic_details.phone ~ "\")[" ~ (basic_details.phone | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.github %}{% set _ = parts.append("#link(\"" ~ basic_details.github ~ "\")[" ~ (basic_details.github | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.linkedin %}{% set _ = parts.append("#link(\"" ~ basic_details.linkedin ~ "\")[" ~ (basic_details.linkedin | typst_escape) ~ "]") %}{% endif %}
    {{ parts | join("  ·  ") }}
  ]
]

#v(6pt)

{% if summary %}
// ── Summary ─────────────────────────────────────────────────────────────────
== Summary
{{ summary | typst_escape }}
{% endif %}

{% if education %}
// ── Education ───────────────────────────────────────────────────────────────
== Education
{% for school in education %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ school.institution | typst_escape }}*, #text(style: "italic")[{{ school.location | typst_escape }}]],
  align(right)[#text(fill: navy)[{{ school.year }}]],
)
#v(2pt)
{{ school.degree | typst_escape }}{% if school.gpa %} — GPA: {{ school.gpa | typst_escape }}{% endif %}
#v(5pt)
{% endfor %}
{% endif %}
{% if work %}
// ── Experience ──────────────────────────────────────────────────────────────
== Experience

{% for job in work %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ job.company | typst_escape }}*{% if job.location %}, #text(style: "italic")[{{ job.location | typst_escape }}]{% endif %}],
  align(right)[#text(fill: navy, style: "italic")[{{ job.start | typst_escape }} -- {{ job.end | typst_escape }}]],
)
#v(2pt)
#text(style: "italic")[{{ job.role | typst_escape }}]
#v(3pt)
{% for item in job.achievements %}
▸ {{ item | typst_escape }} \
{% endfor %}
{% if job.technologies %}
#v(1pt)
#text(size: 10pt, fill: rgb("#555555"))[_Technologies:_ {{ job.technologies | join(", ") | typst_escape }}]
{% endif %}
#v(7pt)
{% endfor %}
{% endif %}
{% if projects %}
// ── Projects ────────────────────────────────────────────────────────────────
== Projects

{% for proj in projects %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [{% if proj.link %}#link("{{ proj.link }}")[*{{ proj.name | typst_escape }}*]{% else %}*{{ proj.name | typst_escape }}*{% endif %}],
  align(right)[#text(fill: navy, style: "italic")[{{ proj.start | typst_escape }} -- {{ proj.end | typst_escape }}]],
)
#v(2pt)
{% for item in proj.description %}
▸ {{ item | typst_escape }} \
{% endfor %}
{% if proj.technologies %}
#text(size: 10pt, fill: rgb("#555555"))[_Technologies:_ {{ proj.technologies | join(", ") | typst_escape }}]
{% endif %}
#v(7pt)
{% endfor %}
{% endif %}
{% if skills %}
// ── Skills ──────────────────────────────────────────────────────────────────
== Technical Skills

#grid(
  columns: (auto, 1fr),
  gutter: (8pt, 4pt),
  {% for skill in skills %}
  [*{{ skill.category | typst_escape }}:*],
  [{{ skill.featured | join("  •  ") | typst_escape }}],
  {% endfor %}
)
{% endif %}
