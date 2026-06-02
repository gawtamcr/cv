---
name: vspace-variables
description: "Named \\vspace variables are the PRIMARY way to edit spacing in single-* resumes; 18 canonical names defined in single-ref.tex"
metadata:
  node_type: memory
  type: feedback
---

Gawtam's convention (set 2026-06-02) for ALL single-* resumes: **spacing is edited through NAMED VSPACE
VARIABLES, never by hand-editing raw `\vspace{...}` or `\setlength{\itemsep}{...}` values inline.**
**Why:** he wants one tunable, self-documenting place to adjust layout spacing per resume instead of hunting
scattered magic numbers through the preamble and body. **How to apply:** when ANY spacing needs changing,
edit the relevant variable's value in the block — do NOT touch the number where the `\vspace`/`\setlength`
is consumed. Keep the 18 names IDENTICAL across every single-* resume; only the *values* differ per file.
See [[single-page-density-rules]] and [[cv-formatting-rules]].

**Where:** a categorized block near the top of the preamble, right after `\setlength{\tabcolsep}{0in}` and
before `% Sections formatting`. `single-ref.tex` is the canonical home (its values are the seed defaults);
a new resume inherits the block on copy. `single-FactoryAutomation.tex` was the first resume to use it.
(`single-ComVis.tex` / `single-GenMod.tex` predate this and may lack the block — do not seed from them anyway.)

**The 18 canonical variable names, grouped by section (Global/Shared first, then document order):**
- *Global/Shared (macro-wide):* `\vSectionBefore` (before `\section` title), `\vSectionRule` (after blue
  titlerule), `\vTableRowSep` (title/subtitle row strut in `\resumeSubheading`), `\vItemTop` (atop
  resumeItem/subheading/project), `\vSubheadingEnd` (after a `\resumeSubheading`), `\vSubItem` (after a
  `\resumeSubItem`), `\vListStart` (before an item list / the Education list), `\vListEnd` (after
  `\resumeItemListEnd` — **tighten this FIRST to fit one page**, rule 8), `\vListGroupEnd` (after
  `\resumeSubHeadingListEnd`).
- *Header:* `\vHeadingName` (under the name), `\vHeadingEnd` (after the header block).
- *Summary (only if an optional Summary is added — rule 15):* `\vSummaryTop`, `\vSummaryEnd`.
- *Education:* `\vEduSep` (between degree entries; `0pt` = adjacent seed default), `\vEduItemSep` (itemsep
  between achievement bullets), `\vEduSkills` (before the Skills line).
- *Technical Projects:* `\vProjectEnd` (after a `\resumeProjectHeading`).
- *Publications:* `\vPubSep` (itemsep between publication entries).

Mirrored in CLAUDE.md section 3 as density rule 16 (CLAUDE.md wins on any disagreement).
