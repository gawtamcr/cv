---
name: cv-formatting-rules
description: "STRICT formatting rules for generating Gawtam's CVs/resumes (length, bullets, templates, build)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

Formatting rules Gawtam requires for every generated CV. **Why:** he applies broadly and wants
ATS-parsable, recruiter-skimmable, visually tight documents; violating these means rework.

**How to apply:**
- **Two template families** (pick per role — Gawtam decides each time, see [[cv-tailoring-workflow]]):
  - `single-*` (e.g. single-ComVis, single-GenMod): **STRICT one page, each bullet ≤ 1 line.**
    Blue accents (`\color{Blue}` sections, blue links), Portfolio link in header, condensed
    "Lead Author Publications" list. For industry / focused technical roles.
  - `acad-*` (e.g. acad-bosch, acad-jana): **may run 2 pages**, longer bullets allowed for full detail.
    Black accents, full publication citations, Coursework lines. For academic / research / PhD roles.
- One page is the DEFAULT goal; only acad-* may exceed it.
- Never let a single-page bullet wrap to a second line — rewrite shorter or cut it.
- **Single-page hard numbers (measured in this layout, 11pt, `\small` bullets, usable width 537.7pt) — see [[single-page-density-rules]]:**
  - Maximize chars/line: plain mixed-case prose fits **~110 chars max; target 100–108**. Bold costs ~15% width, ALL-CAPS ~42% — spend them deliberately (25% bold→~103 cap, 50% bold→~97, fully bold→~87, all-caps→~70).
  - **Minimum content floor = 30 content lines (HARD; more OK if it still fits one page).** Per-entry: every INCLUDED entry needs ≥3 bullets; Education = 3 achievement bullets + Skills line; Publications = 3; Ericsson + ABB always present. **Entry COUNTS per section are FLEXIBLE (2026-05-31):** trade a Technical Project for a 4th Professional Experience etc.; default starting shape = Prof Exp 3 / Research 2 / Projects 3. See [[single-page-density-rules]].
  - **One idea per bullet** — each bullet is a complete standalone sentence (or worst-case phrase). Reach the 30-line floor with real content (more entries/bullets), NEVER by chopping one sentence across multiple bullet lines (GenMod's split-sentence style is the anti-pattern, do not copy it).
  - Use full sentences > phrases; avoid `+` joiners and avoid vague/abstract numbers or concepts — cite concrete real metrics.
  - **ALWAYS include: Publications section, the Ericsson internship, and the ABB thesis** — in every single-page resume, regardless of role.
  - **Seed new single-* resumes by copying `scripts/single-ref.tex`** (canonical seed, tight spacing + canonical Publications block built in) — NOT ComVis/GenMod (example outputs, may be deleted). Always Read the .tex and verify the built PDF (page count, no wraps) when done.
- All CVs must stay ATS-parsable (`\pdfgentounicode=1` is already set; keep machine-readable text).
- Tailor: reorder/select experience, projects, and skills to match the job; drop irrelevant items
  to hold the length limit rather than shrinking margins/fonts further.
- Quantify with real numbers from [[project-deep-reference]] where they strengthen relevance.
- Be truthful — never invent experience; if unsure whether Gawtam has a skill, ASK (see [[cv-open-gaps]]).
- **NEVER mention Kattis** or any assignment auto-grader / evaluation platform (confirmed 2026-06-02) — it is just a grading tool, meaningless to recruiters. Drop the score, or state the outcome plainly ("passed all test cases") without naming the grader. No "22/22 on Kattis", "6/6 Grade C cases", etc.
- **Skills line = concrete technologies ONLY** (confirmed 2026-06-02): languages/frameworks/libraries/named tools a reader can verify (Python, C++, ROS/ROS2, MoveIt, PyTorch, JAX, OpenCV, Docker, Gazebo, MuJoCo, CUDA). **Do NOT list generic domain/role labels** ("Robotics", "Cobots", "Factory Automation", "Computer Vision", "Machine Learning", "Real-Time Control") — they are job categories, not skills, and too generic. Those domain words are fine in the Summary and in bullet prose / as ATS keywords, just not as Skills entries. Lead Skills with the role's must-have tools.
- **Summary / overview section (2–3 lines about Gawtam): ASK FIRST every time** (added 2026-06-02). Applies to BOTH single-* and acad-*, but always ask before drafting one — never add unprompted. Tailor it per role (no fixed blurb). On single-* it COUNTS toward the 30-line floor (does not raise it), so adding a summary means cutting equivalent bullet lines to stay one page. Place as the first `\section` directly under the header, above Education.
- **Build**: `./build.sh scripts/<file>.tex` from repo root → PDF written next to the .tex, build
  artifacts go to `build/`. See [[cv-repo-structure]].
