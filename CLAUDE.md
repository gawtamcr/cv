# CV Project — Claude Instructions

This file makes every Claude Code session in this directory self-contained.
Read the full file before acting. No external memory is needed; everything is here.

**Portability (clone-and-go):** This `CLAUDE.md` is the PRIMARY, auto-loaded source of truth — it travels
with the repo and is loaded on any machine, so a fresh clone behaves identically with zero external setup.
A full mirror of the project's persistent memory is ALSO vendored in-repo at `./memory/` (see section 2).
The harness's own auto-memory store lives under `~/.claude/...` keyed by absolute path and does NOT travel
with a clone — so do not rely on it. Treat `./memory/` as the canonical, version-controlled memory: read it
and, when you learn something worth persisting, update `./memory/` (and this CLAUDE.md) IN-REPO, not only the
home-dir store. If `./memory/` and CLAUDE.md ever disagree, CLAUDE.md wins.

---

## 1. What this repo is for

Gawtam Chithra Ramesh (the user) maintains a Master CV and generates role-tailored CVs/resumes for
job applications. The workflow: he pastes a job description → Claude tailors a CV → builds a PDF.
Claude must deeply know his profile (sections 3–5 below), recall it without re-asking, and ask
targeted gap questions when a role demands unlisted experience.

---

## 2. Repo layout and build system

```
cv/
├── master.tex         — working MasterCV LaTeX (messy; contains errors — see section 6). REFERENCE/scratch only; NEVER read or seed an output from it.
├── build.sh           — build helper: ./build.sh src/<path>.tex  (resolves any path)
├── CLAUDE.md          — this file
├── src/               — ALL active LaTeX lives here
│   ├── single-ref.tex       ← CANONICAL SEED (PRIMARY FILE): gold preamble + 18 named vspace variables + rules-as-comments + [bracketed hints], worked-example ABB/Ericsson bullets, and the canonical Publications block. COPY THIS to start any new single-* resume. This is the ONLY file to seed single-* resumes from.
│   └── scripts/             — tailored / generated resumes
│       ├── single-FactoryAutomation.tex   (single-page blue, Robotics & Factory Automation)
│       ├── single-FieldRobotics.tex       (single-page blue, Field Robotics)
│       ├── acad-bosch.tex                 (academic 2-page, Bosch)
│       ├── acad-jana.tex                  (academic 2-page, Jana)
│       └── archive/                       — DEPRECATED old outputs; do NOT read or seed from these
│           ├── single-ComVis.tex          (old example output; predates current conventions)
│           └── single-GenMod.tex          (old example output; predates current conventions)
├── pdfs/              — output PDFs
├── build/             — latexmk artifacts (auto-generated)
├── memory/            — VENDORED persistent memory (travels with the repo; canonical store, update here)
│   ├── MEMORY.md                    — memory index (one line per file)
│   ├── master-profile.md            — canonical end-to-end profile (mirrors section 5)
│   ├── project-deep-reference.md    — deep metrics/methods mined from references/*.pdf
│   ├── user-gawtam.md               — who the user is
│   ├── cv-formatting-rules.md       — strict formatting rules (mirrors section 3)
│   ├── single-page-density-rules.md — measured density rules for single-* resumes
│   ├── vspace-variables.md          — the 18 named spacing vars (primary spacing mechanism)
│   ├── cv-tailoring-workflow.md     — step-by-step tailoring process (mirrors section 4)
│   └── cv-repo-structure.md         — repo layout + master.tex errors
└── references/        — project reports, transcripts, course materials (details in section 5)
    ├── Transcript_IITMadras.pdf   — official IITM grade card (CGPA 7.9, 546 credits)
    ├── Transcript_KTH.pdf         — official KTH transcript (grades per course, print date 2026-05-22)
    ├── VLA_Project_Slides.pdf     — DD2600 Robot Learning & Embodied AI course project slides
    ├── Systemantics_Poster.pdf    — IIT Madras project poster for Systemantics internship
    ├── ddp/                       — DDP report + presentation (autonomous ultrasound)
    ├── ComVis/                    — DD2423 lab PDFs (Labs 1–3)
    ├── intro to robo/             — DD2410 assignment PDFs (IK, Planning, Mapping)
    ├── iitm_resumes/              — old IITM intern + placement CVs (reference only)
    └── sop/                       — motivation letters (not used for CV tailoring)
```

**Which .tex to touch (avoid confusion with old files):**
- **Seed every single-* resume from `src/single-ref.tex` — the single PRIMARY file. Never read or copy from anything under `src/scripts/archive/` or from `master.tex`.**
- Active tailored resumes live in `src/scripts/`. For acad-* roles, copy the closest `src/scripts/acad-*.tex`.
- `master.tex` is a messy reference for profile facts only (section 5/6 already capture what matters) — do not read it during tailoring and never produce output from it.

Build command (from repo root):
```bash
./build.sh src/single-ref.tex          # or any path, e.g.:
./build.sh src/scripts/single-FactoryAutomation.tex
# → PDF written to pdfs/<name>.pdf; build artifacts go to build/
```

---

## 3. Formatting rules (STRICT — enforced every time)

### Two template families

| Family | When to use | Length | Bullet length | Accents | Header links |
|--------|-------------|--------|---------------|---------|--------------|
| `single-*` | Industry / focused tech roles | **Exactly 1 page** | **≤ 1 line, no wrap** | Blue (`\color{Blue}`) | Phone, Email, LinkedIn, GitHub, Portfolio, Location |
| `acad-*` | Research / PhD / academic roles | May run 2 pages | Longer OK | Black | Phone, Email, LinkedIn, GitHub |

- **Ask Gawtam which template per application** — he decides every time. Default: single-* for industry, acad-* for research/PhD if he doesn't specify.
- For `single-*`: if content doesn't fit on one page, **cut entries or shorten bullets** — never reduce margins or font size further.
- All CVs must be ATS-parsable (`\pdfgentounicode=1` already set — keep machine-readable text, no images in body).
- Tailor by **selecting** content and rewording to match the job description, not by dumping everything.
- **Ordering (ALL sections, ALL templates): strictly reverse-chronological by END date — latest end first.** Applies to Education, Professional Experience, Research, and Technical Projects. This overrides relevance ordering: tailor by choosing WHICH entries to include, never by moving a newer entry below an older one. (An ongoing entry uses its end month, e.g. `Jun 2026`.)
- Quantify with real numbers from section 5 where they strengthen relevance.
- **Never invent experience**. If you suspect relevant unlisted experience, ask (see section 4, step 4).

### Single-page density rules (STRICT — measured in this exact layout)

Central formatting ideas for every `single-*` resume. Measured: usable bullet width = **537.7pt**, 11pt doc, `\small` bullet font.

1. **Maximize characters per line — pack each bullet full.** Plain mixed-case prose wraps around **~115–118 chars; target 108–114** (do not leave bullets short at ~95). Bold costs ~15% extra width, ALL-CAPS ~42%, so a line ~25% bold caps near ~103, ~50% bold ~97, fully bold ~87, all-caps ~70. Spend bold/caps deliberately. **Write dense and technical**: name the method, the mechanism, and the result/metric — avoid generic filler (e.g. NOT "a single model steerable across task variants"; YES "steered the pretrained flow model toward new temporal-logic specs at inference without retraining"). Verify the build for silent wraps after pushing length.
2. **Minimum content floor = 30 content lines** (HARD — never go below; more is fine if it still fits one page, e.g. a 31st bullet). **Entry counts per section are FLEXIBLE — distribute by relevance:** you may drop a Technical Project to add a 4th Professional Experience, run Research with 3 entries, etc. The non-negotiables regardless of distribution:
   - Education: 3 achievement bullets + 1 Skills line
   - **Every INCLUDED entry (any section): ≥3 bullets each**
   - Publications: 3 items (and rule 5 mandates Ericsson + ABB always present)
   - Suggested default starting shape (from `single-ref.tex`): Professional Experience 3, Research 2, Technical Projects 3 — adjust freely as long as the 30-line floor and all other rules hold.
3. **One idea per bullet** — each bullet is a complete standalone sentence (worst case a phrase). Reach 30 lines with REAL content (more entries/bullets), NEVER by splitting one sentence across multiple `\resumeItem` lines. GenMod's split-sentence padding is the anti-pattern — do not copy it.
4. Prefer full sentences over phrases; no `+` joiners; cite concrete real metrics, not vague/abstract numbers or concepts.
5. **ALWAYS include in every single-page resume: a Publications section, the Ericsson internship, and the ABB thesis** — regardless of role. Never drop any of these to save space; cut/shorten elsewhere instead.
6. **Publications block = LITERAL copy-paste from `single-ref.tex`.** `single-ref.tex` is the canonical source for the Publications block. Copy its `\section{...Lead Author Publications}` through `\end{itemize}` verbatim — do NOT reword, re-abbreviate, restructure titles, change "Best Paper Award", re-expand "3DSG", or wrap it in `\small`. It already fits one line each at the document's normal font size. If publication details genuinely change, update them in `single-ref.tex` FIRST, then re-copy into every other single-* resume.
7. **Publications stay at the document's normal (11pt) font** — never shrink them with `\small`. (At 11pt the one-line budget is ~100 chars; the canonical text is already tuned to fit, which is why rule 6 exists.)
8. `single-ref.tex` is the layout/spacing reference for all single-* resumes (its preamble already sets `\resumeItemListEnd` to `\vspace{-7.5pt}`). To make the ≥30-line content fit exactly one page, the ONLY allowed lever is tightening vertical `\vspace` (make that value more negative to pull Publications onto page 1) — never shrink margins or font. **DANGER: `\resumeItemListEnd` is shared by every entry, so over-tightening it (roughly past `-11pt`) makes the NEXT section header overlap the last bullet above it — `pdfinfo` still reports 1 page and `grep` reports 0 overfull, so these checks DO NOT catch the collision. If one page needs a value past ~-10pt, you have too much content: instead CUT it back to the 30-line floor (drop a 4th bullet, unwrap any 2-line bullet, shorten the Skills line to ONE line) and keep `\vspace` in the comfortable -7.5 to -10pt range. ALWAYS confirm by rendering, not by trusting the numeric checks — see rule 13.**
8b. **Uneven gaps ABOVE section headers — equalize them (learned 2026-05-31).** Some `\section` headers can float with a large gap above them while others sit tight (measured here: 36px above Professional Experience, 45px above Research, vs ~15px elsewhere). Cause: the section before-skip is inflated by the preceding block's trailing list glue, and it is largest after a section that ends WITHOUT a bullet list — Education ends on a plain `\textbf{Skills}` text line, so the following header gets the biggest gap. **FIX:** add a corrective `\vspace{-Npt}` on its own line IMMEDIATELY before the offending `\section{...}`, calibrated by measuring pixel gaps until every header gap matches (values used here: `-9pt` before Professional Experience, `-12pt` before Research). The two `\vspace` values may differ — that is fine; the goal is symmetric *visual* gaps, not identical code. **ANTI-PATTERN: do NOT add a global `\titlespacing*{\section}{...}` override** — it did not fix the before-gaps and it broke the BELOW-header spacing (the blue `\titlerule` cut through the first entry's title). Tune per-header `\vspace` and re-measure. To measure objectively: `pdftoppm -png -r 200 -gray pdfs/<f>.pdf full && convert full-1.png full.pgm`, then with numpy count blank-row runs (a row is ink if `(row<128).sum()>3`; report runs ≥12px); crop a band at a gap's y (`pdftoppm ... -x 0 -y <Y> -W 1700 -H 60`) and Read the PNG to label the header.
9. Use the IIT Madras degree phrasing "B.Tech Engineering Design **and** M.Tech Robotics" (the word "and", not a `+`).
10. **Never use em dashes, and never use a dash as a separator/connector** anywhere (titles, bullets, headings). Use a colon, comma, or parentheses instead — e.g. entry title `Master's Thesis: Generative Flow Matching...` (not `Master's Thesis -- ...`), and GPA in parentheses `\textnormal{(GPA 4.62/5.0)}` (not `-- GPA ...`). The en-dash `--` is allowed ONLY for numeric/date ranges (`Jan 2026 -- Jun 2026`). Never `---`.
11. **Every dated entry — including Technical Projects — uses a month range** (the period the work/course ran), never a bare year. KTH study periods: P1 ≈ Aug–Oct, P2 ≈ Nov–Jan, P3 ≈ Jan–Mar, P4 ≈ Mar–Jun. CAUTION: `references/Transcript_KTH.pdf` lists **grade-registration/exam dates, NOT course periods** (e.g. DD2423 shows 2025-04-22 but the course ran Oct 2024–Jan 2025) — use the course period for the CV, and ask Gawtam if a date is ambiguous. Confirmed CV project dates: DD2423 = Oct 2024 -- Jan 2025; DD2600 = Aug 2025 -- Oct 2025; DD2610 = Nov 2025 -- Jan 2026.
12. **Favor abstract concepts and results over obscure names** (applies to every resume, single- and acad-). A generic recruiter skims bullets; niche names mean nothing to them and are better left for interview discussion. Lead with what was built/achieved and the outcome, not the tool.
   - **STRIP** proprietary/research tool, model, dataset, and benchmark names, and raw math notation. Examples seen here: COLMAP, OpenMVS, ROUGE, BERTScore, DAG-STL, ZSTP, Maze2D, AntMaze, ARKitScenes, OwlV2, Siam-MOT, FairMOT, NTXent, `$L_{vv}$`/`$L_{vvv}$`. Replace with the concept ("structure-from-motion", "multi-view stereo", "deep multi-object tracking models", "text-similarity metrics", "differential-geometry zero-crossings").
   - **NEVER mention Kattis** (or any assignment auto-grader / evaluation platform) — confirmed by Gawtam 2026-06-02. It is just a grading tool and means nothing to recruiters. Drop the score, or if the result matters state the outcome plainly ("passed all test cases") without naming the grader. Do NOT write "22/22 on Kattis", "6/6 Grade C cases", etc.
   - **KEEP** (a) field-standard terms a domain hiring engineer expects, which double as ATS keywords: SIFT, RANSAC, CLIP, Hough, FFT, ResNet, SimCLR, ViT/MAE, GPT-4o, Gemini, ROS, MoveIt; and (b) a name that is CENTRAL to the entry AND explained inline — e.g. "Hydra, a state-of-the-art 3D scene graph framework". Keep concrete result numbers (86.2% accuracy, 0.917 ROC-AUC).
14. **Skills line = concrete technologies ONLY, never domain/role labels** (confirmed by Gawtam 2026-06-02). List languages, frameworks, libraries, and named methods/tools a reader could verify — e.g. Python, C++, ROS/ROS2, MoveIt, PyTorch, JAX, OpenCV, Docker, Gazebo, MuJoCo, CUDA. **Do NOT put generic field/role/domain words in Skills** — e.g. "Robotics", "Cobots", "Factory Automation", "Computer Vision", "Machine Learning", "Real-Time Control" are job categories, not skills, and are too generic to belong there. (You may still use those domain words in the Summary line and in bullet prose / as ATS keywords — just not as Skills entries.) Lead the Skills line with the role's must-have *tools*.
15. **Summary / overview section (2–3 lines about Gawtam) — ASK FIRST, every time** (added by Gawtam 2026-06-02). Applies to BOTH families (single-* and acad-*), but **always ask Gawtam whether to include one before drafting** — never add it unprompted. When included it must be **tailored per role** (rewrite the 2–3 lines to mirror the job's focus and keywords; no fixed canonical blurb). On single-* the summary lines **count toward the 30-line content floor** (they do not raise it) — so adding a summary means cutting an equivalent number of bullet lines to stay on one page. Place it as the first `\section` (e.g. `\section{\color{Blue}Summary}`) directly under the heading, above Education.
13. **Verify before reporting done** — Read the final `.tex` AND run these on the built PDF; all must pass:
   ```bash
   pdfinfo pdfs/<file>.pdf | awk '/Pages/{print $2}'     # must be 1
   grep -c "Overfull \\hbox" build/<file>.log            # must be 0
   pdftotext pdfs/<file>.pdf - | grep -c "^•"            # bullet+pub count must be >= 30
   pdftotext pdfs/<file>.pdf - | sed '/^$/d' | grep -A3 "Lead Author"  # each publication on ONE line
   ```
   **MANDATORY visual render — the four checks above are NOT sufficient.** They miss text overlap caused by over-tightened `\vspace` (rule 8) and bullets that wrap to a 2nd visual line. Always render the page to an image and actually LOOK at it before saying done:
   ```bash
   pdftoppm -png -r 150 pdfs/<file>.pdf /tmp/cv_check     # then Read /tmp/cv_check-1.png
   ```
   Confirm by eye: (a) NO section header or bullet overlaps the line above it; (b) every bullet is exactly ONE line (no wraps); (c) spacing is even/readable, not crushed; (d) Publications sit on page 1. If anything overlaps, you over-compressed — fix per rule 8 (cut content, don't crank `\vspace`), never ship a PDF you have not looked at.

16. **VSPACE VARIABLES are the PRIMARY way to edit spacing — never hand-edit raw `\vspace{...}` / `\setlength{\itemsep}{...}` values inline.** Every single-* resume (seeded from `single-ref.tex`) defines a categorized block of **18 named spacing variables** near the top of the preamble (right after `\setlength{\tabcolsep}{0in}`, before `% Sections formatting`). To adjust ANY spacing, change the variable's value in that block — do NOT edit the number where the `\vspace`/`\setlength` is consumed. Keep the 18 names IDENTICAL across all single-* resumes (only values differ per resume). When tightening to fit one page, the first lever is still `\vListEnd` (rule 8), now via its variable.
   - **The 18 canonical names**, grouped:
     - *Global/Shared (macro-wide):* `\vSectionBefore` (before `\section` title), `\vSectionRule` (after blue titlerule), `\vTableRowSep` (title/subtitle row strut in `\resumeSubheading`), `\vItemTop` (atop resumeItem/subheading/project), `\vSubheadingEnd` (after a `\resumeSubheading`), `\vSubItem` (after a `\resumeSubItem`), `\vListStart` (before an item list / the Education list), `\vListEnd` (after `\resumeItemListEnd` — tighten FIRST to fit), `\vListGroupEnd` (after `\resumeSubHeadingListEnd`).
     - *Header:* `\vHeadingName` (under the name), `\vHeadingEnd` (after the header block).
     - *Summary (only used if an optional Summary is added — rule 15):* `\vSummaryTop`, `\vSummaryEnd`.
     - *Education:* `\vEduSep` (between degree entries; `0pt` = adjacent, the seed default), `\vEduItemSep` (itemsep between achievement bullets), `\vEduSkills` (before the Skills line).
     - *Technical Projects:* `\vProjectEnd` (after a `\resumeProjectHeading`).
     - *Publications:* `\vPubSep` (itemsep between publication entries).
   - `single-ref.tex` is the canonical home of this block; its values are the seed defaults. A new resume inherits the block on copy; only edit the values, never rename. (Older example outputs `single-ComVis.tex` / `single-GenMod.tex` predate this and may not have the block — do not seed from them anyway.)

### Naming convention for new files
- `src/scripts/single-<RoleKeyword>.tex` for single-page
- `src/scripts/acad-<CompanyOrRole>.tex` for academic

---

## 4. Tailoring workflow (follow this every time a job description is provided)

1. Read the job description: extract must-have skills, keywords, seniority level, domain focus.
2. Confirm template choice (ask if not specified).
3. Map job keywords to Gawtam's real experience (section 4–5).
4. **Proactively ask** when the role needs something you suspect he's done but hasn't stated explicitly.
   Classic example: a role needing CAD → ask about CAD done in Hyperloop battery pack (COMSOL),
   Human Powered Segway (Fusion360 + COMSOL stress), Fusion360 API project. (All previously open profile gaps are now resolved — see the section 5 profile.)
5. For single-* roles, **copy `src/single-ref.tex`** (the canonical seed — gold preamble, 18 named vspace variables, rules-in-comments, worked ABB/Ericsson examples, and the canonical Publications block already in place) and fill its bracketed hints with tailored content; for acad-* copy the closest `src/scripts/acad-*`. Rename per convention above. Do NOT read or seed from anything in `src/scripts/archive/` (the old `single-ComVis.tex` / `single-GenMod.tex` outputs) or from `master.tex`.
6. Draft the .tex with selected/reordered content, enforcing rules from section 3.
7. Build: `./build.sh src/scripts/<file>.tex` — confirm no page overflow before reporting done.
8. Update this CLAUDE.md if you learn new facts about Gawtam's profile.

---

## 5. Canonical profile — Gawtam Chithra Ramesh

**Contact:** gawtamcr3@gmail.com · (+46) 76541-8589 · Stockholm, Sweden
**Links:** linkedin.com/in/gawtamcr · github.com/gawtamcr · gawtamcr.github.io

### Education

| Institution | Degree | Dates | Location | GPA |
|-------------|--------|-------|----------|-----|
| KTH Royal Institute of Technology | MSc Systems, Control & Robotics | Aug 2024 – Jun 2026 | Stockholm | **4.62/5.0** (credit-weighted: A=5, B=4.5, C=4, D=3.5, E=3; P/F excluded; 57 graded hp as of May 2026) |
| IIT Madras | Dual Degree B.Tech Engineering Design + M.Tech Robotics | Aug 2019 – Jul 2024 | Chennai | **7.9/10** (confirmed from official transcript, 546 earned credits) |

**KTH course grades (from official transcript, print date 2026-05-22):**

| Code | Course | Grade |
|------|--------|-------|
| DD2410 | Introduction to Robotics | A |
| EL2820 | Modelling of Dynamical Systems | B |
| AK2030 | Theory and Methodology of Science | D |
| DD2423 | Image Analysis and Computer Vision | A |
| DD2438 | Artificial Intelligence and Multi-Agent Systems | P |
| EL2520 | Control Theory and Practice, Advanced Course | C |
| DD2600 | Robot Learning and Embodied AI | A |
| DD2411 | Research project in Robotics, Perception and Learning | P |
| DD2610 | Deep Learning, advanced course | A |
| EL2320 | Applied Estimation | B |

### Professional Experience (reverse chron)

**Master's Thesis — ABB Robotics, Västerås** (Jan–Jun 2026, ongoing)
Mentors: Matthew Lock, Jonathan Styrud.
- System 1/2 framework for industrial manipulation: generative flow-matching trajectory planner (System 1) steered at inference by Signal Temporal Logic (STL) robustness gradients (System 2).
- Single generative model steerable by arbitrary STL specs without retraining; flexible transfer across task variants.
- Validated on reach-avoid benchmarks; benchmarking vs DAG-STL, ZSTP on Maze2D and AntMaze.
- Collaborating with ABB R&D on transfer to long-horizon 6-DoF manipulation.
- Targeting top robotics venue submission.

**Device Research Intern, 3D Scene Graphs — Ericsson Research, Lund** (Jul–Dec 2025)
Mentors: Püren Güler, Hector Caltenco.
- Robust 3DSG pipeline: integrated instance segmentation + tracking into Hydra (SOTA framework); reduced parameter sensitivity for reliable scene interpretation across diverse environments.
- Synchronized RGB-D inpainting pipeline to remove privacy-sensitive objects from 3DSGs in real time; benchmarked SOTA inpainting balancing reconstruction fidelity vs real-time performance.
- **Lead author:** IMPROVE 2026 (accepted, Long Oral, Best Paper Award); ICPR 2026 (under review).

**Graduate Robotics Intern, Modular Collaborative Robots — Systemantics India, Bangalore** (Dec 2022–Jul 2023)
Mentor: Jagannath Raju (CTO, Systemantics India Pvt. Ltd).
- Built complete system controller from scratch for company's cobot portfolio; real-time processes via Linux PREEMPT RT patch; inter-process communication via SocketCAN, FDCAN, semaphores, and signal interrupts.
- S-Curve trajectory generation (7-zone profile) for 6-DoF manipulator; reduces mechanical shock by smooth accel/decel.
- Backward-chained Behavior Trees for task planning (lab pipetting, fast-food kiosk, inspection); robust long-horizon execution.
- Integrated ROS2 (MoveIt2 Hybrid Motion Planning, Gazebo physics sim); created URDFs and SRDFs for cobot.
- Started impedance/admittance control work for collision detection and kinesthetic teaching (disturbance observer).

**Multi-Object Detection & Tracking — Blurgs Research Labs** (Jun–Jul 2021, Remote)
- Analyzed 5 SOTA MOT networks for Indian Navy product; trained/tested Siam-MOT and FairMOT for drone/CCTV surveillance; real-time multi-object tracking + re-identification with FairMOT.

**Robotics Intern, Pallet Handling — Yaskawa, Gurgaon** (Jun–Jul 2021)
Mentor: Manju Tiwari.
- Modeled 3D palletizing for mixed carton sizes using MotoSim + teach pendant.
- C++ algorithm to optimize robot memory when streaming data from PC to robot controller.

**Software Development Intern — Imaginate Software Labs** (May–Aug 2020, Remote)
- Unity3D toolkit in C# to upload 3D models (60+ formats) into VR via Autodesk Forge APIs in real time.
- Heroku web app for 3D content viewing; removed engineer dependency for content upload.

**Battery Pack Design for Hyperloop Pods — Avishkar Hyperloop, IIT Madras** (Oct 2020–Jun 2021)
Mentors: Prof. Satya Chakravarthy, Prof. TM Muruganandam. Role: Power Systems Engineer.
- Designed high-discharge battery pack; extended life **10%** by reducing peak temperature 10°C with Al heat sink.
- Custom Battery Management System (BMS) for voltage/temperature monitoring and safety.
- Won "Most Scalable Design" award by Zeleros (Spanish Hyperloop company); top 5 for mechanical/propulsion.
- Selected in top 24 teams for European Hyperloop Week, Valencia, Spain.

**Graduate Teaching Assistant — Field and Service Robotics (ID4060), IIT Madras** (Aug–Nov 2023)
Mentor: Bijo Sebastian. Designed/graded ROS + CoppeliaSim assignments for 40 students.

### Research Experience

**Graduate Research, Deformable Object Manipulation (DOM) — KTH RPL** (Jan–Nov 2025)
Advisor: Florian T. Pokorny. Collaborators: David Blanco-Mulero (UPC), Yifei Dong.
- Integrated taxonomy-guided VLMs (Gemini, GPT-4o, Qwen) with T-DOM taxonomy to interpret DOM scenes → motion primitives.
- Built prompt–taxonomy framework producing robot-parsable structured specifications from natural language.
- Quantitative failure-mode analysis; integrated multimodal + temporal cues.
- **Lead author:** ROMADO workshop @ IROS 2025 (accepted).
- Evaluated with FI-Score, BERT, BLEU/ROUGE/METEOR on taxonomy-code + NL correctness.
- Simulation in PyBullet; real-world validation planned.

**Dual Degree Project, SfM for Autonomous Ultrasound — IIT Madras INSPIRE Lab** (Jan–May 2024)
Advisor: Nirav Patel (CORRECT spelling — master.tex wrongly says "Partel"). Dept. of Engineering Design, IIT Madras.
Title: "Cost Efficient Autonomous Ultrasound Scan Using a Single RGB-Camera."
Hardware: igus RL-DP-5 (5-DoF), Intel i7-9750H, 16GB RAM, NVIDIA GTX 1660ti, single RGB camera on end-effector.
- COLMAP SfM (pycolmap, Bundle Adjustment) on 20 predefined RGB poses → sparse point cloud; no camera calibration needed.
- OpenMVS Multi-View Stereo → dense 3D torso reconstruction; .ply point cloud published as ROS PointCloud2.
- Point cloud segmentation (abdomen ROI) → tangent vector estimation for probe approach angle.
- ROS/MoveIt motion planning + Gazebo physics simulation; end-to-end perception→planning loop.
- Future work: force-sensor end-effector control and image recognition for automated ROI selection.

**UAV Motion Planning & Control — IIT Madras Young Research Fellowship** (Sep 2021–Apr 2022)
Advisor: Prof. Satadal Ghosh.
- Target-driven motion planning + obstacle avoidance for UAVs.
- Proportional Navigation + Acceleration-Velocity Obstacles in 2D; ~20% faster and more compute-efficient than classical aerospace algorithms.
- Awarded among top 30 of 800+ applicants for the YRF.

### Course / Technical Projects

**Robot Learning & Embodied AI — DD2600** (KTH, Aug–Oct 2025 [P1], grade: A; transcript grade date 2025-10-24)
Team: Carl Clauson, Ilian Lamrani Auffray, Belfor Salazar, Gawtam. GitHub: github.com/gawtamcr/eai2025_project
*Lab 2A extension — Object Presence/Absence in Semantically Queryable Maps:*
- Problem: CLIP-based semantic voxel maps produce false "hot" regions for absent objects due to scene-wise similarity normalization.
- Built pipeline: RGB-D → CLIP embeddings → 3D semantic voxel map → per-frame 2D similarity heatmaps → presence classifier.
- Data: 3 ARKitScenes × ~80 poses/scene × 8 query classes → ~2,000 RGB+heatmap pairs (687 positive / 1,265 negative). Classes: ball, door, floor, painting, sofa, table, wall, window.
- Three classifiers compared: (i) Gemini-based VLM (ground truth labeling), (ii) pixel-threshold (τ=0.8, k=0.1% → 74% accuracy, ROC-AUC 0.803), (iii) voxel-threshold (τ=0.275, count>10 → 85% accuracy, ROC-AUC 0.921), (iv) ResNet18 trained from scratch (binary cross-entropy, AdamW, 80/20 split → **86.2% val accuracy**, ROC-AUC 0.917).
- Also tested Qwen2.5VL (32B) locally: ~87% object presence agreement with Gemini2.5Flash, ~52% map-correctness agreement.
- Takeaway: ResNet18 best accuracy; voxel-threshold best AUC; pixel-threshold weakest. Overfitting limits NN gains.
*Also in DD2600:*
- Deployed pretrained Vision-Language-Action (VLA) model for manipulation; analyzed generalization and robustness limits on unseen tasks.

**Deep Learning Advanced — DD2610** (KTH, Nov 2025–Jan 2026 [P2], grade: A; transcript grade date 2026-01-27)
Five practicals, all implemented from scratch in PyTorch/JAX:
- *MeanFlow* (one-step generative modeling, team: Joar Paganus, Haoran Jin, Gawtam): reimplemented in PyTorch (except U-Net); ablations on time sampler (logit-normal μ), CFG parameters (ω, κ, p_c), r≠t ratio (75% optimal on MNIST, CAS=87.43%); showed CAS unreliable under guidance mixing; CIFAR-10 best FID ~160 @ epoch 600. Directly relevant to ABB thesis (flow matching).
- *MAE (Masked Autoencoders)*: built ViT from scratch — PatchEmbed (Conv2d projection), multi-head self-attention (QKV, scaled dot-product), MLP (GELU), Block (residual + LayerNorm); full asymmetric MAE encoder-decoder with random masking (75%) and MSE loss on masked patches; CIFAR-10, 5 epochs: train loss 0.385→0.127. Ablations: masking ratios (0.5/0.75/0.85/0.95), fixed vs learned vs no positional encodings.
- *SimCLR* (contrastive self-supervised learning): implemented NTXent loss (temperature τ=0.07, full pairwise cosine similarity matrix, masked self-similarity); ResNet18 encoder + 2-layer projection head (128-dim); CIFAR-10; 5 pretrain epochs; linear evaluation with frozen encoder: ~24% val accuracy on 1% labels (vs 10% fully supervised baseline). Framework: JAX/Flax.
- *FixMatch* (semi-supervised): JAX implementation; weak augmentation (flip+crop) and strong augmentation (RandAugment magnitude=9 + Cutout); confidence threshold τ=0.95; ResNet18 backbone; CIFAR-10 with 400 labeled/class (μ=7 unlabeled ratio); cosine LR decay; trained for 20k steps from pretrained checkpoint; val error ~34% with FixMatch vs ~38% supervised-only baseline.
- *Uncertainty Estimation* (2 parts): Part I — Deep Ensembles (M=6 MLPs) on toy cosine regression; Gaussian + Laplacian NLL losses; adversarial training (FGSM ε=0.02–0.08); Shannon entropy for total/data/knowledge uncertainty decomposition via Jensen-Shannon divergence. Part II — Variational Inference (Bayes by Backprop, Blundell et al.); reparametrization trick; VI-FC network with weight distributions N(μ,σ²) via softplus; ELBO loss = KL divergence (prior N(0,a²I), a=1e-2) + NLL; trained on 1D cosine regression with homoscedastic/heteroscedastic noise.

**Multi-Agent Systems — DD2438** (KTH, Feb–May 2025)
- *MAPF:* Conflict-Based Search (CBS) for 20+ holonomic (drones) + non-holonomic (cars) agents; Hybrid A* low-level planner; greedy "bakery" goal-assignment minimizing D_ij = T_i + d_ij; goal padding + node-pruning heuristics; fail-safe expansion bound.
- *Pacman Capture-the-Flag:* Hybrid: custom Behavior Tree (sequence/selector/switched-learning-action/predicate-condition) + 3 role-specific PPO policies (attack/defend/escape) via Unity ML-Agents. 2-phase training (isolation → joint), self-play, curriculum learning, composite episodes (10k steps). Only team to combine BT + RL.

**Artificial Intelligence — DD2380** (KTH, 2025)
- Hybrid A* + waypoint tracking for car & drone in Unity; motion primitives from bicycle model (11 steering values over 50°, wheelbase=2); adaptive braking; car robust on all tracks; competitive total 422.3s (2nd of 5 groups).

**Image Analysis & Computer Vision — DD2423** (KTH, Oct 2024–Jan 2025 [P2]; labs Oct–Nov 2024; grade: A; transcript grade date 2025-04-22 is a delayed registration, NOT the course period)
Three labs confirmed from course materials:
- *Lab 1 (Filtering):* Fourier/FFT properties; Gaussian convolution via FFT (gaussfft); smoothing effects on noise (Gaussian, median, ideal low-pass); subsampling analysis.
- *Lab 2 (Edge detection & Hough):* Differential geometry edge detector — L̃_vv zero-crossings + L̃_vvv sign condition; multi-scale analysis (t=0.0001–64); implemented `extractedge()` and `houghline()` (ρ-θ accumulator, gradient-magnitude weighted); applied to real images.
- *Lab 3 (Image matching & 3D):* SIFT feature extraction + RANSAC for homography estimation (planar scenes); fundamental matrix estimation via SVD + RANSAC (epipolar constraint); 3D triangulation from projection matrices (constrained least squares → smallest eigenvector of G^T G).

**Applied Estimation — EL2320** (KTH, 2025, solo)
- 2D EKF-SLAM in MATLAB; known + unknown data association via Mahalanobis gating; dynamic state-vector/covariance expansion for new landmarks (resolved matrix-consistency bug). Filter consistency analysis: known-assoc x-error peak ~0.01m within 3σ; unknown-assoc on symmetric maps → divergence/NaN (EKF overconfidence).

**Advanced Control — EL2520** (KTH, 2025, grade: C, team: Cezary Banaszek, Joachim Jobard, Aassik Pazhani)
Tools: MATLAB only.
- Four-tank process: modeled from first principles; RGA analysis; min/non-min phase analysis (γ1+γ2 condition). Decentralized dynamic-decoupling controller + robust Glover-McFarlane (H∞ loop-shaping). Robust controller: min-phase rise ~4s, 20% overshoot, 2% ss error.

**Introduction to Robotics — DD2410** (KTH, Sep–Oct 2024, grade: A)
Four assignments confirmed from course materials:
- *IK:* Analytic IK for 3-DoF SCARA; iterative Jacobian-based IK for 7-DoF KUKA (DH table: L=0.4, M=0.39; Kattis score 22/22).
- *Planning:* Hybrid A* / RRT for Dubins car (state: x,y,θ; control: φ∈[-π/4,π/4]); collision-free path with circular + line obstacles; Kattis: 6/6 Grade C cases.
- *Mapping:* 2D occupancy grid from ROS laser scans (LaserScan → map frame → grid indices); E-part: occupied cells; C-part: raytrace free space + C-space inflation + OccupancyGridUpdate (rectangle-only updates).
- *Mobile Manipulation:* Behavior Tree mission planner for TIAGo (ROS/Gazebo) — autonomous navigation, vision-based grasping, kidnapped-robot recovery.

**Control of Automotive Systems** (IIT Madras, Jun–Nov 2022, Mentor: Prof. Srikanthan Sridharan)
- Heading-angle controller for autonomous ground vehicle (vehicle dynamics model).
- P and PI controllers for pneumatic brake system.
- Nonlinear Sliding Mode Controller for tractor hydraulic hitch (attenuate external forces, prevent front-wheel lift-off).

**Human Powered Segway** — ED4060, IIT Madras (Mar–Jun 2021)
- Novel hybrid tricycle-segway concept; Fusion360 CAD model; COMSOL stress analysis.

**Path Finder and Visualizer** (IIT Madras, Jun 2021, Mentor: Prof. Ramanathan)
- 2D path finder in Python/PyQt5; A* and Dijkstra algorithms; interactive Qt Designer UI.

**Multi-Agent RL VR Shooter** (CFI, IIT Madras, May–Aug 2020)
- PPO multi-agent cooperative policies in Unity3D for shooter strategy game; superhuman gameplay vs humans; Unity VR integration.

**Python API for Fusion360** (IIT Madras, Jan–Feb 2020, Mentor: Prof. Ramanathan)
- Fusion360 API script to auto-generate 3D model variants from CSV dimension files; eliminated manual rework.

**CFD Aerofoil for Formula Student Car** — ED4040, IIT Madras (Mar–Apr 2021)
Tools: Solidworks (CAD), Ansys (CFD analysis).
- Designed front-wing aerofoil for maximum downforce/drag ratio; improved F/D ratio by 33% via position/angle optimization.
- CFD analysis in Ansys to determine optimal aerofoil setup.

**Gesture Robot** — ED5080 Mechatronics, IIT Madras (Jul–Nov 2021)
- 2-DoF robotic arm for identifying and lifting objects using electromagnets; programmed on Arduino Mega.
- Proximity sensors for detection; LED light reflection for color sensing; manual and automatic calibration.

**Discord Bot** (Apr 2021) — C#; YouTube search + mp3 conversion via ffmpeg; text/reaction responses.

### Publications (lead author)
1. "Robust Object-layer Construction of 3D Scene Graphs Using Instance Segmentation." **IMPROVE 2026** (Accepted, Long Oral, Best Paper Award).
2. "Synchronized RGB-D Inpainting for Privacy-Aware 3D Scene Graph Construction." **ICPR 2026** (Under Review).
3. "Scene Understanding in Deformable Object Manipulation via Taxonomy-Guided Vision-Language Models." **IROS 2025 Workshop ROMADO** (Accepted).

### Technical Skills

| Category | Skills |
|----------|--------|
| Languages | Python, C, C++, C# |
| Robotics / Sim | ROS/ROS2, MoveIt, Gazebo, MuJoCo, PyBullet, Unity3D, Unity ML-Agents, CoppeliaSim, MATLAB |
| ML / DL | PyTorch, JAX, OpenCV, wandb, YOLO |
| Tools | Docker, Git, LaTeX, CUDA, Slurm, VS Code |
| CAD / CAE | Fusion360, Solidworks, Ansys, COMSOL |

(Note: Fusion360 confirmed in Hyperloop+Segway+API projects. Solidworks+Ansys confirmed in CFD Aerofoil project (ED4040). COMSOL confirmed in Segway stress analysis and Hyperloop. Four-Tank (EL2520) used MATLAB only — not COMSOL.
CAD/CAE skills are real but Gawtam is not currently pursuing mechanical/design roles. Include only for roles explicitly requiring multi-disciplinary or mechatronics background — not as a headline skill for robotics/ML roles.)

### Achievements

- **IIT Madras Young Research Fellowship** — top 30 of 800+ applicants.
- **JEE Advanced** 97.64 percentile; **JEE Mains** 99.10 percentile (of 1.5M candidates).
- **UCEED** All-India Rank 52 of 50,000+.

### Leadership & Positions of Responsibility

- **Head of Industrial & Public Relations**, Dept. of Engineering Design IITM (Apr 2021–May 2022): led 3-tier team for 1,200+ students; designed first hybrid recruitment framework.
- **Strategist**, Computer Vision & Intelligence Group (CVIG) IITM (Apr 2020–May 2021): co-organized DL Summer School (500+), co-mentored student projects.
- **Associate Manager**, Entrepreneurship Cell IITM (Apr 2020–May 2021): Summer Internfair (40 startups), Elevate competition (150 startups), Annual E-Summit.
- **Student Buddy**, THS International Winter Reception 2025, KTH (Jan–Feb 2025): primary contact for 20 international students.
- **Graduate Teaching Assistant**, Field and Service Robotics ID4060, IIT Madras (Aug–Nov 2023): ROS + CoppeliaSim assignments for 40 students.

### Extra-Curricular
- IIT Madras Volleyball (Agrata festival; selected among 20/100 students for freshman NSO training)
- **Drawing:** Won 3 state-level + 5+ district-level competitions (Oil Pastels and Pencils). National competition win was Times of India (Mar 2015) — 1 of the state wins.
- Game development enthusiast; Valorant Silver 2; built complete 3D game solo in Unity3D (obstacles, enemies, points, UI, VFX)
- **ShARE Junior Consultant** (IIT Madras, May 2021): selected from 200 applicants after global interview; 'Mobility' module; global team of 700 across 15 nations

---

## 6. Known errors in master.tex (never blindly copy from it)

| Error | Wrong in master.tex | Correct |
|-------|---------------------|---------|
| Course codes | Nearly everything labeled "DD2348" | DD2438 (MAS), DD2380 (AI), DD2610 (DL Adv), EL2320 (Applied Est), EL2520 (Adv Control), DD2410 (Intro Robotics), **DD2600** (Robot Learning) |
| KTH project dates | Most say "Mar 2021–Jun 2021" | See section 5 for correct dates |
| Advisor name | "Nirav Partel" | Nirav **Patel** |
| Empty bullets | "battle snake", "Mean Flow", "SimCLR", "VAE", "MAPF", "Minimax", blank `\resumeItem{}` | Fill from section 5; note: no "VAE" project — was Uncertainty Estimation |
| "Deep Generative Modelling" course | Appears in master.tex and single-GenMod.tex | Does NOT exist — Gawtam only did DD2610. Remove entirely. |
| KTH GPA | 4.56 vs 4.24 shown in various files | **4.62/5.0** — credit-weighted (A=5, B=4.5, C=4, D=3.5, E=3; 57 graded hp, P/F excluded). Use this figure. |
| IIT Madras GPA | Any value other than 7.9 | **7.9/10** (confirmed from official transcript) |
| Robot Learning code | "TBD" or "DD2601" | **DD2600** |
| `\newpage` in master.tex | Hard page break mid-experience | Remove for single-page variants |
| Layout drift | Older docs reference `multi-page/`, `single-page/`, or `scripts/` at root | Active LaTeX lives under `src/` (seed `src/single-ref.tex`, resumes in `src/scripts/`) |

---

## 7. Session behavior summary

- Load this file first; no external memory needed.
- When tailoring: follow section 4 workflow; enforce section 3 rules.
- When in doubt about a fact: check section 5 first; if still unsure, ask Gawtam.
- When you learn new confirmed facts: update this CLAUDE.md (primarily the section 5 profile).
- Never summarize what you just did at the end of a response — Gawtam can read the diff.
