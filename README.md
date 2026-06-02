# CV — Gawtam Chithra Ramesh

LaTeX-based CV system. Maintains a master profile and generates tailored CVs for job applications.

## Repo layout

```
cv/
├── master.tex          — MasterCV (reference/scratch only — has known errors, see CLAUDE.md §6; never seed output from it)
├── build.sh            — build helper (resolves any path)
├── CLAUDE.md           — full profile, formatting rules, tailoring workflow (read this first)
├── src/                — ALL active LaTeX
│   ├── single-ref.tex          ← canonical SEED — copy this to start any single-* resume
│   └── scripts/                — tailored / generated resumes
│       ├── single-FactoryAutomation.tex  (single-page, Robotics & Factory Automation)
│       ├── single-FieldRobotics.tex      (single-page, Field Robotics)
│       ├── acad-bosch.tex                (academic 2-page, Bosch)
│       ├── acad-jana.tex                 (academic 2-page, Jana)
│       └── archive/                      — deprecated old outputs (do not use)
├── pdfs/               — output PDFs
├── build/              — latexmk artifacts (auto-generated, do not commit)
├── memory/             — vendored persistent memory (travels with the repo)
└── references/         — project reports, transcripts, course materials
```

## Build

```bash
# From repo root (any path works)
./build.sh src/single-ref.tex
./build.sh src/scripts/single-FactoryAutomation.tex
./build.sh src/scripts/acad-bosch.tex
```

The PDF is written to `pdfs/<name>.pdf`. Build artifacts go to `build/`.

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
