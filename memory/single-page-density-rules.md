---
name: single-page-density-rules
description: "Hard measured numbers for single-page resumes: chars/line capacity, 30-line content floor, one-idea-per-bullet rule"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 79f4d8ef-e79e-4ab0-b70c-52f3fe80e48f
---

Ground rules Gawtam set for ALL single-page (`single-*`) resumes. **Why:** he wants every single-page
resume to maximize information density — fill the page to its limits without wrapping or going to page 2.
Maximizing characters-per-line is the central formatting idea. See [[cv-formatting-rules]].

**Template files (UPDATED 2026-05-31):** COPY `scripts/single-ref.tex` to start every new single-* resume —
it is the CANONICAL SEED (gold preamble, rules-as-comments + [bracketed hints], worked-example ABB/Ericsson
bullets, and the canonical Publications block already in place). Do NOT seed from `single-ComVis.tex` or
`single-GenMod.tex` — those are compliant EXAMPLE OUTPUTS and Gawtam may delete them. A `single-ref2.tex`
alternate may be added. The Publications block + tight spacing (`\resumeItemListEnd` at `-7.5pt`) now live in `single-ref.tex`.

**Measured layout numbers** (11pt article, `\small` bullet font, this repo's margins; usable bullet width = **537.7pt**):
- Plain mixed-case prose wraps **~115–118 chars; target 108–114** (pack bullets full, don't leave them at ~95).
  Write dense + technical (method + mechanism + result), never generic filler.
- **Never use em dashes or dashes as separators/connectors** (titles, bullets, GPA). Use colon/comma/parentheses.
  En-dash `--` allowed ONLY for date/numeric ranges. Titles use `:` (e.g. "Master's Thesis: Generative Flow Matching"); GPA in `()`.
- Bold costs ~15% extra width, ALL-CAPS ~42% vs plain lowercase. Effective caps per line:
  25% bold → ~103 · 50% bold → ~97 · fully bold → ~87 · all-caps → ~70.
- So: write to ~105 chars of plain prose and *spend* bold/caps consciously (each bolded word shrinks the budget).

**How to apply:**
- **Content floor = 30 content lines (HARD MINIMUM; more is fine if it still fits one page — a 31st bullet is allowed).**
  **Entry COUNTS per section are FLEXIBLE (UPDATED 2026-05-31) — distribute by relevance:** you may drop a Technical
  Project to add a 4th Professional Experience, run Research with 3 entries, etc. Inviolable regardless of distribution:
  - Education: 3 achievement bullets + 1 Skills line
  - **Every INCLUDED entry (any section): ≥3 bullets each**
  - Publications: 3 items; Ericsson + ABB always present
  - Default starting shape (from `single-ref.tex`): Professional Experience 3, Research 2, Technical Projects 3 — adjust freely.
  - NOTE: a wrapped 2-line bullet eats the vertical space of a real bullet; tightening it to one line frees room for an extra content line.
- **One idea per bullet** — each bullet is a complete standalone sentence (worst case a phrase).
  Reach 30 lines with real content, NEVER by splitting one sentence across multiple `\resumeItem` lines.
  GenMod's split-sentence padding is the ANTI-PATTERN — do not copy it.
- Prefer full sentences over phrases; no `+` joiners; cite concrete real metrics, not vague/abstract numbers.
- **Always present in every single-page resume:** Publications section, Ericsson internship, ABB thesis. Never drop them — cut/shorten elsewhere.
- **Publications block = LITERAL copy-paste from `single-ref.tex`** (the canonical source as of 2026-05-31). Copy its
  `\section{...Lead Author Publications}` through `\end{itemize}` verbatim — do NOT reword, re-abbreviate,
  restructure titles, change "Best Paper Award", or wrap in `\small`. It already fits one line each at normal 11pt.
  If pub details change, edit `single-ref.tex` first, then re-copy everywhere.
- **Publications stay at normal 11pt** — never `\small` them.
- To fit ≥30 lines on one page, the ONLY lever is tightening vertical `\vspace` (e.g. `\resumeItemListEnd`
  set to `-7.5pt` in single-ComVis) — never shrink margins or font. **DANGER: past ~-11pt the next section
  header OVERLAPS the bullet above it, and pdfinfo/grep still report 1 page + 0 overfull (they miss it).
  Keep `\vspace` in -7.5 to -10pt; if it needs more you have too much content — cut to the 30-line floor
  (drop a 4th bullet, unwrap any 2-line bullet, shorten Skills to ONE line) instead of cranking `\vspace`.**
- **Uneven gaps ABOVE section headers (learned 2026-05-31).** Symptom: some `\section` headers float with a big
  gap above them (measured 36px before Professional Experience, 45px before Research) while others sit tight
  (~15px). Cause: the section before-skip is inflated by the preceding block's trailing list glue, and the
  gap is bigger after a section that ends WITHOUT a bullet list — Education ends on a plain `\textbf{Skills}`
  text line, so the next header (Professional Experience) gets an extra-large gap. **FIX that works:** put a
  corrective `\vspace{-Npt}` on its own line IMMEDIATELY before the offending `\section{...}`, calibrated by
  measuring pixel gaps (values used here: `-9pt` before Professional Experience, `-12pt` before Research; the
  two values differ on purpose to equalize the *visual* gap — that is still "symmetric"). **ANTI-PATTERN — do
  NOT use a global `\titlespacing*{\section}{...}` override to fix this:** it did NOT fix the before-gaps and it
  broke the BELOW-header spacing (the blue `\titlerule` cut through the first entry's title). Tune per-header
  `\vspace` instead, and re-measure.
- **How to measure gaps objectively (don't eyeball thumbnails):** `pdftoppm -png -r 200 -gray pdfs/<f>.pdf full`
  then `convert full-1.png full.pgm`, load with numpy, count blank-row runs (`ink=(data<128).sum(axis=1)`; a row
  is ink if `ink>3`; report runs where `r-prev>=12`). Crop a band at a gap's y with `pdftoppm ... -x 0 -y <Y> -W 1700 -H 60`
  and Read the PNG to label which header it is. Target: every section-header gap within a few px of the others (here 14-16px).
- IITM degree phrasing: "B.Tech Engineering Design **and** M.Tech Robotics" (use "and", not `+`).
- **Ordering: every section is strictly reverse-chronological by END date (latest end first)** — Education, Professional Experience, Research, Technical Projects. Overrides relevance; tailor by which entries to include, never by reordering against chronology. Ongoing entry uses its end month.
- **Dated entries (incl. Technical Projects) use month ranges, not bare years.** KTH transcript shows exam dates, not course periods — use course period, ask if unsure. Confirmed: DD2423 Oct 2024--Jan 2025, DD2600 Aug 2025--Oct 2025, DD2610 Nov 2025--Jan 2026.
- **Favor abstract concepts + results over obscure names** (all resumes). Recruiters skim; niche names are for interviews.
  - STRIP proprietary/research tool, model, dataset, benchmark names and raw math: COLMAP, OpenMVS, ROUGE, BERTScore,
    DAG-STL, ZSTP, Maze2D, AntMaze, ARKitScenes, OwlV2, Siam-MOT, FairMOT, NTXent, `$L_{vv}$`. Use the concept instead.
  - KEEP field-standard ATS keywords (SIFT, RANSAC, CLIP, Hough, FFT, ResNet, SimCLR, ViT/MAE, GPT-4o, Gemini, ROS, MoveIt)
    and a name only if CENTRAL + explained inline (e.g. "Hydra, a SOTA 3D scene graph framework"). Keep result numbers.
- Start from `single-ref.tex` tight spacing. Always Read the final .tex and verify the built PDF:
  pages==1, zero overfull, `^•` count ≥30, each publication on ONE line — before reporting done.
  **Those four checks are NOT enough: also `pdftoppm -png -r 150 pdfs/<f>.pdf /tmp/cv_check` and Read the
  PNG to eyeball it — no overlapping text, no wrapped bullets, even spacing. NEVER ship a PDF unlooked-at.**
- Field-standard ML/robotics terms double as ATS keywords and SHOULD be kept (Gawtam confirmed e.g. **PPO** is fine to name explicitly); only STRIP niche/proprietary names per the rule above.
