# CV Project — Claude Instructions

This file makes every Claude Code session in this directory self-contained.
Read the full file before acting. No external memory is needed; everything is here.

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
├── master.tex         — working MasterCV LaTeX (messy; contains errors — see section 6)
├── build.sh           — build helper: ./build.sh scripts/<file>.tex
├── CLAUDE.md          — this file
├── scripts/           — all tailored CVs live here
│   ├── single-ComVis.tex    (single-page blue, Computer Vision role)
│   ├── single-GenMod.tex    (single-page blue, Generative Modelling role — partially empty)
│   ├── acad-bosch.tex       (academic 2-page, Bosch)
│   └── acad-jana.tex        (academic 2-page, Jana)
├── pdfs/              — output PDFs
├── build/             — latexmk artifacts (auto-generated)
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

Build command (from repo root):
```bash
./build.sh scripts/<file>.tex
# → PDF written next to the .tex; build artifacts go to build/
```

NOTE: `README.md` mentions `multi-page/` and `single-page/` dirs — those do NOT exist.
All tailored CVs are in `scripts/`.

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
- Tailor by selecting/reordering content to match the job description, not by dumping everything.
- Quantify with real numbers from section 5 where they strengthen relevance.
- **Never invent experience**. If you suspect relevant unlisted experience, ask (see section 7).

### Naming convention for new files
- `scripts/single-<RoleKeyword>.tex` for single-page
- `scripts/acad-<CompanyOrRole>.tex` for academic

---

## 4. Tailoring workflow (follow this every time a job description is provided)

1. Read the job description: extract must-have skills, keywords, seniority level, domain focus.
2. Confirm template choice (ask if not specified).
3. Map job keywords to Gawtam's real experience (section 4–5).
4. **Proactively ask** when the role needs something you suspect he's done but hasn't stated explicitly.
   Classic example: a role needing CAD → ask about CAD done in Hyperloop battery pack (COMSOL),
   Human Powered Segway (Fusion360 + COMSOL stress), Fusion360 API project. See section 7 for open gaps.
5. Copy the closest existing template from `scripts/`, rename per convention above.
6. Draft the .tex with selected/reordered content, enforcing rules from section 3.
7. Build: `./build.sh scripts/<file>.tex` — confirm no page overflow before reporting done.
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
- **Lead author:** IMPROVE 2026 (accepted, Long Oral, Best Paper nominee); ICPR 2026 (under review).

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

**Robot Learning & Embodied AI — DD2600** (KTH, 2025, grade: A)
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

**Deep Learning Advanced — DD2610** (KTH, 2026, grade: A)
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

**Image Analysis & Computer Vision — DD2423** (KTH, Oct–Nov 2024, grade: A)
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
1. "Robust Object-layer Construction of 3D Scene Graphs Using Instance Segmentation." **IMPROVE 2026** (Accepted, Long Oral, Best Paper nominee).
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
| README dirs | References `multi-page/`, `single-page/` | Files actually live in `scripts/` |

---

## 7. Open gaps — ask Gawtam before using these on a CV

1. ~~**Deep Generative Modelling project**~~ — **RESOLVED: does not exist as a separate course.** Gawtam only did DD2610 (Deep Learning Advanced). The "Deep Generative Modelling" entry in master.tex and single-GenMod.tex is erroneous — remove from all CVs. DD2610 details fully documented in section 5.
2. ~~**Robot Learning & Embodied AI course code**~~ — **RESOLVED: DD2600** (confirmed from KTH transcript).
3. ~~**Exact KTH GPA**~~ — **RESOLVED: 4.62/5.0** (credit-weighted: A=5, B=4.5, C=4, D=3.5, E=3; 57 graded hp, P/F excluded). IIT Madras CGPA confirmed **7.9/10** (546 credits, Jul 2024).
4. ~~**Solidworks / Ansys**~~ — **RESOLVED: both used in CFD Aerofoil project (ED4040, Solidworks CAD + Ansys CFD).** Only cite for multi-disciplinary/mechatronics roles — Gawtam is not pursuing purely mechanical roles.
5. ~~**SimCLR / VAE details in DD2610**~~ — **RESOLVED: full details now documented** in section 5. No VAE project; the practicals were MAE, SimCLR, FixMatch, MeanFlow, Uncertainty Estimation.

---

## 8. Session behavior summary

- Load this file first; no external memory needed.
- When tailoring: follow section 4 workflow; enforce section 3 rules.
- When in doubt about a fact: check section 5 first; if still unsure, ask Gawtam.
- When you learn new confirmed facts: update this CLAUDE.md (the section 5 profile or section 7 gaps).
- Never summarize what you just did at the end of a response — Gawtam can read the diff.
