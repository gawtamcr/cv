---
name: cv-tailoring-workflow
description: Step-by-step process for tailoring a CV when Gawtam provides a job description
metadata: 
  node_type: memory
  type: project
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

When Gawtam provides a job opportunity / description, tailor a CV by this process. **Why:** keeps
output consistent, relevant, and within his rules across sessions.

**How to apply:**
1. Recall [[master-profile]] and [[project-deep-reference]]; read the job description for role type,
   must-have skills, keywords, and seniority.
2. **Choose template** — Gawtam decides single-* vs acad-* per application (he said "ask each time").
   Confirm, defaulting to single-* for industry roles and acad-* for research/PhD if he doesn't specify.
3. Select & reorder content to match the role; map job keywords to his real experience.
4. **Proactively ASK** when the role needs a skill you suspect he has from a project but isn't explicit
   (his explicit example: a CAD role → ask about CAD done in projects like Hyperloop battery pack /
   Human Powered Segway / Fusion360 API). Also ask if a relevant project lacks detail (see [[cv-open-gaps]]).
5. Draft the .tex: for single-* COPY `scripts/single-ref.tex` (the canonical seed — NOT ComVis/GenMod, which
   may be deleted) and fill its bracketed hints; for acad-* copy the closest `acad-*` (see [[cv-repo-structure]]).
   Rename to a role-specific name (pattern: `single-<Role>.tex` or `acad-<Company>.tex`).
   Entry counts per section are flexible (e.g. trade a Technical Project for a 4th Professional Experience) as
   long as the 30-line floor and all other rules hold — see [[single-page-density-rules]].
6. Enforce [[cv-formatting-rules]] — STRICT one page + 1-line bullets for single-*; 2 pages OK for acad-*.
7. Build with `./build.sh scripts/<file>.tex` and verify length/overflow before handing back.
8. Save any newly learned facts to memory (update [[master-profile]] / resolve [[cv-open-gaps]]).
