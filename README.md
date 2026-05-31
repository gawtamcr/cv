# CV — Gawtam Chithra Ramesh

LaTeX-based CV system. Maintains a master profile and generates tailored CVs for job applications.

## Repo layout

```
cv/
├── master.tex          — MasterCV (reference only — has known errors, see CLAUDE.md §6)
├── build.sh            — build helper
├── CLAUDE.md           — full profile, formatting rules, tailoring workflow (read this first)
├── scripts/            — all tailored CVs
│   ├── single-ComVis.tex     (single-page, Computer Vision)
│   ├── single-GenMod.tex     (single-page, Generative Modelling)
│   ├── acad-bosch.tex        (academic 2-page, Bosch)
│   └── acad-jana.tex         (academic 2-page, Jana)
├── pdfs/               — output PDFs
├── build/              — latexmk artifacts (auto-generated, do not commit)
└── references/         — project reports, transcripts, course materials
```

## Build

```bash
# From repo root
./build.sh scripts/<file>.tex

# Examples
./build.sh scripts/acad-bosch.tex
./build.sh scripts/single-ComVis.tex
```

The PDF is written next to the `.tex` source. Build artifacts go to `build/`.

## Two CV families

| Family | Use for | Length | Accent colour |
|--------|---------|--------|---------------|
| `single-*` | Industry / focused tech roles | Exactly 1 page | Blue |
| `acad-*` | Research / PhD / academic roles | Up to 2 pages | Black |

## Tailoring workflow

1. Drop a job description into a Claude Code session opened in this directory.
2. Claude loads `CLAUDE.md` automatically — full profile and rules are pre-loaded.
3. Confirm template family (`single-*` vs `acad-*`).
4. Claude drafts the `.tex`, builds it, confirms no overflow.

See `CLAUDE.md` for the complete profile, all formatting rules, and the step-by-step tailoring process.
