// FAANG / ATS-optimized resume template
#set document(title: "Resume")
#set page(paper: "us-letter", margin: (x: 0.6in, top: 0.45in, bottom: 0.45in))
#set text(size: 10.5pt)
#set list(marker: "•", indent: 10pt, body-indent: 6pt)
#set par(spacing: 0.45em, leading: 0.65em)

#show heading.where(level: 2): h => {
  v(7pt)
  text(weight: "bold", size: 11pt)[#upper[#h.body]]
  v(-3pt)
  line(length: 100%, stroke: 0.8pt)
  v(2pt)
}

// ── Header ──────────────────────────────────────────────────────────────────
#align(center)[
  #text(size: 20pt, weight: "bold")[{{ basic_details.name | typst_escape }}]
  #linebreak()
  #text(size: 10pt)[
    {% set parts = [] %}
    {% if basic_details.email %}{% set _ = parts.append("#link(\"mailto:" ~ basic_details.email ~ "\")[" ~ (basic_details.email | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.phone %}{% set _ = parts.append("#link(\"tel:" ~ basic_details.phone ~ "\")[" ~ (basic_details.phone | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.github %}{% set _ = parts.append("#link(\"" ~ basic_details.github ~ "\")[" ~ (basic_details.github | typst_escape) ~ "]") %}{% endif %}
    {% if basic_details.linkedin %}{% set _ = parts.append("#link(\"" ~ basic_details.linkedin ~ "\")[" ~ (basic_details.linkedin | typst_escape) ~ "]") %}{% endif %}
    {{ parts | join(" $|$ ") }}
  ]
]

#v(4pt)

{% if summary %}
// ── Summary ─────────────────────────────────────────────────────────────────
== Summary

#text(size: 10.5pt)[{{ summary | typst_escape }}]

{% endif %}
{% if education %}
// ── Education ───────────────────────────────────────────────────────────────
== Education

{% for school in education %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ school.institution | typst_escape }}*#h(6pt){{ school.location | typst_escape }}],
  align(right)[{{ school.year }}],
)
#v(2pt)
#text(size: 10pt)[{{ school.degree | typst_escape }}{% if school.gpa %} — GPA: {{ school.gpa | typst_escape }}{% endif %}]
#v(4pt)
{% endfor %}
{% endif %}
{% if work %}
// ── Experience ──────────────────────────────────────────────────────────────
== Experience

{% for job in work %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [*{{ job.company | typst_escape }}*{% if job.location %} #h(6pt) #text(style: "italic")[{{ job.location | typst_escape }}]{% endif %}],
  align(right)[#text(style: "italic")[{{ job.start | typst_escape }} -- {{ job.end | typst_escape }}]],
)
#v(2pt)
#text(style: "italic")[{{ job.role | typst_escape }}]
#v(3pt)
{% for item in job.achievements %}
- {{ item | typst_escape }}
{% endfor %}
#v(2pt)
{% if job.technologies %}
#text(size: 10pt)[*Technologies:* {{ job.technologies | join(", ") | typst_escape }}]
{% endif %}
#v(5pt)
{% endfor %}
{% endif %}
{% if projects %}
// ── Projects ────────────────────────────────────────────────────────────────
== Projects

{% for proj in projects %}
#grid(
  columns: (1fr, auto),
  gutter: 0pt,
  [{% if proj.link %}#link("{{ proj.link }}")[*{{ proj.name | typst_escape }}*]{% else %}*{{ proj.name | typst_escape }}*{% endif %}{% if proj.technologies %} #h(6pt)#text(style: "italic")[{{ proj.technologies | join(", ") | typst_escape }}]{% endif %}],
  align(right)[#text(style: "italic")[{{ proj.start | typst_escape }} -- {{ proj.end | typst_escape }}]],
)
#v(1pt)
{% for item in proj.description %}
- {{ item | typst_escape }}
{% endfor %}
#v(5pt)
{% endfor %}
{% endif %}
{% if skills %}
// ── Skills ──────────────────────────────────────────────────────────────────
== Technical Skills

{% for skill in skills %}
*{{ skill.category | typst_escape }}:* {{ skill.featured | join(", ") | typst_escape }}
#linebreak()
{% endfor %}
{% endif %}
