FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    # ---- LaTeX minimal ----
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-latex-extra \
    # ---- Python ----
    python3 \
    python3-venv \
    python3-pip \
    # ---- Utilities ----
    make \
    git \
    pandoc \
    ca-certificates \
    && python3 -m venv $VIRTUAL_ENV \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["bash"]