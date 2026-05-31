---
name: cv-repo-structure
description: "Layout of the Overleaf/cv repo, the build system, and known errors in master.tex to avoid/fix"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

Repo: /home/gawtam_wsl/thesis/ARCHIVE/Overleaf/cv

- `master.tex` — working LaTeX MasterCV (messy; see errors below). Canonical profile is [[master-profile]].
- `scripts/` — tailored CVs live here. **For single-* roles COPY `scripts/single-ref.tex`** — the CANONICAL
  SEED (gold preamble, rules-as-comments + [bracketed hints], worked ABB/Ericsson examples, canonical Publications
  block). single-ComVis.tex / single-GenMod.tex (single-page blue) are compliant EXAMPLE OUTPUTS that Gawtam may
  delete — do NOT seed from them. A single-ref2.tex alternate may be added. For acad-* copy acad-bosch.tex /
  acad-jana.tex (academic black). See [[single-page-density-rules]].
- `pdfs/` — output PDFs. `build/` — latexmk artifacts. `references/` — 8 project report PDFs ([[project-deep-reference]]).
- **Build**: from repo root run `./build.sh scripts/<file>.tex` → PDF written next to the .tex; artifacts to build/.
  README mentions `multi-page/` and `single-page/` dirs but those DON'T exist — files are all in `scripts/`.

**Known errors in master.tex (fix from [[master-profile]], don't copy blindly):**
- Course codes are almost all wrongly "DD2348". Correct ones in [[project-deep-reference]].
- Many KTH course projects have copy-pasted wrong dates ("Mar 2021 – Jun 2021").
- Advisor name "Nirav Partel" should be "Nirav Patel".
- Several projects have empty/placeholder bullets ("battle snake", "Mean Flow", "SimCLR", "VAE",
  "MAPF", "Minimax", blank `\resumeItem{}`) — fill from [[master-profile]]/[[project-deep-reference]].
- GPA shown inconsistently (4.56 vs 4.62 /5) — confirm exact value before use.
