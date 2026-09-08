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
before `% Sections formatting`. `src/single-ref.tex` is the canonical home (its values are the seed defaults);
a new resume inherits the block on copy. `src/scripts/single-FactoryAutomation.tex` was the first resume to use it.
(The archived `src/scripts/archive/single-ComVis.tex` / `single-GenMod.tex` predate this — do not seed from them anyway.)

**The 18 canonical variable names, grouped by section (Global/Shared first, then document order):**
- *Global/Shared (macro-wide):* `\vSectionBefore` (before `\section` title), `\vSectionRule` (after blue
  titlerule), `\vTableRowSep` (title/subtitle row strut in `\resumeSubheading`), `\vItemTop` (atop
  resumeItem/subheading/project), `\vSubheadingEnd` (after a `\resumeSubheading`), `\vSubItem` (after a
  `\resumeSubItem`), `\vListStart` (before an item list / the Education list), `\vListEnd` (after
  `\resumeItemListEnd` — **do NOT tighten; see the locked set below**), `\vListGroupEnd` (after
  `\resumeSubHeadingListEnd`).
- *Header:* `\vHeadingName` (under the name), `\vHeadingEnd` (after the header block).
- *Summary (only if an optional Summary is added — rule 15):* `\vSummaryTop`, `\vSummaryEnd`.
- *Education:* `\vEduSep` (between degree entries; `0pt` = adjacent seed default), `\vEduItemSep` (itemsep
  between achievement bullets), `\vEduSkills` (before the Skills line).
- *Technical Projects:* `\vProjectEnd` (after a `\resumeProjectHeading`).
- *Publications:* `\vPubSep` (itemsep between publication entries).

## LOCKED VALUES — never modify (instructed by Gawtam 2026-09-08)

These 18 values are settled. **Copy them verbatim into every new single-* resume and DO NOT change any of
them** — not to fit a page, not to fix overlap, not slightly. Rule 8's old "tighten `\vListEnd` first" advice
is OBSOLETE for single-* and must not be followed.

```latex
\newcommand{\vSectionBefore}{-3pt}   \newcommand{\vSectionRule}{-5pt}
\newcommand{\vTableRowSep}{-2pt}     \newcommand{\vItemTop}{-3pt}
\newcommand{\vSubheadingEnd}{-12pt}  \newcommand{\vSubItem}{-4pt}
\newcommand{\vListStart}{0em}        \newcommand{\vListEnd}{-2pt}
\newcommand{\vListGroupEnd}{-1.5em}
\newcommand{\vHeadingName}{3pt}      \newcommand{\vHeadingEnd}{-8pt}
\newcommand{\vSummaryTop}{2pt}       \newcommand{\vSummaryEnd}{-6pt}
\newcommand{\vEduSep}{5pt}           \newcommand{\vEduItemSep}{-0.3em}
\newcommand{\vEduSkills}{-0.7em}     \newcommand{\vProjectEnd}{-20pt}
\newcommand{\vPubSep}{-4pt}
```

Verified 2026-09-08 on `src/scripts/single-SeniorRoboticsResearcher.tex`: renders Summary + Education +
4 Professional Experience + 2 Research + 2 Technical Projects + 3 Publications (30 content lines) on exactly
ONE page with ZERO overlaps.

**If a resume spills to page 2: CUT CONTENT.** Drop a bullet, drop an entry, or shorten a wrapped bullet.
Never re-tune the variables.

**Why this rule exists (learned the hard way 2026-09-08):** while fitting the Senior Robotics Researcher
resume, Claude repeatedly pushed `\vListEnd` to -8/-9pt and `\vListGroupEnd` to -2.1em to force a fit. Each
attempt oscillated between "fits but text collides" and "clean but 2 pages", and Claude wrongly concluded the
content was ~9 lines too long and proposed deleting a whole section. Gawtam reverted to the locked set — which
has a much LOOSER `\vListEnd` (-2pt) paired with a tight `\vItemTop` (-3pt) — and everything fit on one page
cleanly with all content intact. Over-tightening `\vListEnd`/`\vListGroupEnd` collapses list glue and forces
bad page breaks; loose per-list gaps with a tight heading pull is what actually fits.

Mirrored in CLAUDE.md section 3 as density rules 16, 16b, 16c, 16d (CLAUDE.md wins on any disagreement).
