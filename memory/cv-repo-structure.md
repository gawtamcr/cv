---
name: cv-repo-structure
description: "Layout of the Overleaf/cv repo, the build system, and known errors in master.tex to avoid/fix"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

Repo: /home/gawtam_wsl/thesis/ARCHIVE/Overleaf/cv

**Layout (reorganized 2026-06-02 — scripts/ moved under src/):**
- `master.tex` (repo root) — working LaTeX MasterCV (messy; see errors below). REFERENCE/scratch ONLY:
  never read it during tailoring and never produce an output from it. Canonical profile is [[master-profile]].
- `src/` — ALL active LaTeX lives here.
  - `src/single-ref.tex` — the **PRIMARY canonical seed** (gold preamble, the 18 named vspace variables
    [[vspace-variables]], rules-as-comments + [bracketed hints], worked ABB/Ericsson examples, canonical
    Publications block). **Seed EVERY single-* resume by copying this one file — nothing else.**
  - `src/scripts/` — tailored/generated resumes: single-FactoryAutomation.tex, single-FieldRobotics.tex
    (single-page blue); acad-bosch.tex, acad-jana.tex (academic 2-page black — copy the closest for acad-*).
  - `src/scripts/archive/` — DEPRECATED old outputs single-ComVis.tex / single-GenMod.tex. Do NOT read or
    seed from these; they predate current conventions and have errors.
- `pdfs/` — output PDFs. `build/` — latexmk artifacts. `references/` — project report PDFs ([[project-deep-reference]]).
- **Build**: from repo root run `./build.sh src/single-ref.tex` (or `./build.sh src/scripts/<file>.tex`); the
  script resolves any path → PDF goes to `pdfs/<name>.pdf`, artifacts to `build/`. See [[single-page-density-rules]].

**Known errors in master.tex (fix from [[master-profile]], don't copy blindly):**
- Course codes are almost all wrongly "DD2348". Correct ones in [[project-deep-reference]].
- Many KTH course projects have copy-pasted wrong dates ("Mar 2021 – Jun 2021").
- Advisor name "Nirav Partel" should be "Nirav Patel".
- Several projects have empty/placeholder bullets ("battle snake", "Mean Flow", "SimCLR", "VAE",
  "MAPF", "Minimax", blank `\resumeItem{}`) — fill from [[master-profile]]/[[project-deep-reference]].
- GPA shown inconsistently (4.56 vs 4.62 /5) — confirm exact value before use.
