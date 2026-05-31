---
name: master-profile
description: "Canonical end-to-end profile of Gawtam Chithra Ramesh (education, experience, research, projects, skills) — the source of truth for tailoring CVs"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

# Gawtam Chithra Ramesh — Master Profile (canonical source of truth)

Contact: gawtamcr3@gmail.com · (+46) 76541-8589 · Stockholm, Sweden ·
LinkedIn linkedin.com/in/gawtamcr · GitHub github.com/gawtamcr · Portfolio gawtamcr.github.io

NOTE: the in-repo `CLAUDE.md` (section 5) is the PRIMARY self-contained source of truth and is auto-loaded
on every clone; this file is the vendored memory mirror. If the two disagree, CLAUDE.md wins.

This file is the canonical profile. `master.tex` in the repo is a messy working LaTeX file with
duplicate/placeholder bullets and wrong dates/course codes — trust THIS file over master.tex when
they disagree. See [[cv-repo-structure]] for the known errors in master.tex.
Deep per-project facts (metrics, methods) mined from the report PDFs live in [[project-deep-reference]].

## Education
- **KTH Royal Institute of Technology** — MSc Systems, Control & Robotics, Aug 2024 – Jun 2026,
  Stockholm. **GPA 4.62/5.0** (credit-weighted: A=5, B=4.5, C=4, D=3.5, E=3; 57 graded hp, P/F excluded — confirmed).
- **IIT Madras** — Dual Degree (B.Tech Engineering Design + M.Tech Robotics), Aug 2019 – Jul 2024,
  Chennai. CGPA 7.9/10.

## Professional Experience
- **Master's Thesis, ABB Robotics** (Västerås) — Jan–Jun 2026. Mentors: Matthew Lock, Jonathan Styrud.
  Generative flow-matching trajectory planner (System 1) steered at inference by Signal Temporal Logic
  (STL) robustness gradients (System 2); NL → control policy; one model steerable by arbitrary STL specs
  without retraining; benchmarked vs DAG-STL, ZSTP on Maze2D/AntMaze; reach-avoid full-spec satisfaction;
  targeting top robotics venue; transfer to long-horizon 6-DoF manipulation with ABB R&D.
- **Device Research Intern, 3D Scene Graphs, Ericsson Research** (Lund) — Jul–Dec 2025.
  Mentors: Püren Güler, Hector Caltenco. Robust 3DSG pipeline integrating instance segmentation +
  tracking into Hydra (SOTA); synchronized RGB-D inpainting to remove privacy-sensitive objects in
  real time; reduced parameter sensitivity; benchmarked SOTA inpainting (fidelity vs real-time).
  **Lead author**: IMPROVE 2026 (accepted, Long Oral, Best Paper Award), ICPR 2026 (under review).
- **Graduate Robotics Intern, Modular Collaborative Robots, Systemantics India** (Bangalore) — Dec 2022 – Jul 2023.
  Mentor: Jagannath Raju. Backward-chained Behavior Trees for 6-DoF manipulator long-horizon planning;
  6-DoF trajectory generation + control pipeline in C++; real-time joint actuation via low-latency
  D-Bus and SocketCAN to motor controllers. (ROS2/MoveIt2 context.)
- **Multi-Object Detection & Tracking, Blurgs Research Labs** (Remote) — Jun–Jul 2021.
  Analyzed 5 SOTA MOT networks for startup's first product for the Indian Navy; trained/tested
  Siam-MOT and FairMOT for drone/CCTV surveillance; real-time multi-object tracking + re-identification.
- **Robotics Intern, Pallet Handling, Yaskawa** (Gurgaon) — Jun–Jul 2021. Mentor: Manju Tiwari.
  Modeled 3D palletizing for mixed carton sizes using MotoSim + teach pendant; C++ algorithm to
  optimize robot memory when streaming data PC→robot.
- **Software Development Intern, Imaginate Software Labs** (Remote) — May–Aug 2020.
  Unity3D toolkit in C# to upload 3D models (60+ formats) into VR via Autodesk Forge APIs in real time;
  Heroku web app for 3D viewing; removed engineer dependency for content upload.

## Research Experience
- **Graduate Research, Deformable Object Manipulation (DOM), KTH RPL** — Jan–Nov 2025.
  Advisor: Florian T. Pokorny (collaborators David Blanco-Mulero, Yifei Dong, UPC). Taxonomy-guided
  VLMs (Gemini, GPT-4o, Qwen) interpret DOM scenes → motion primitives; T-DOM taxonomy; prompt–taxonomy
  framework producing robot-parsable structured specs from NL; quantitative failure-mode analysis;
  multimodal + temporal cues. Lead author, ROMADO workshop @ IROS 2025. See [[project-deep-reference]].
- **Dual Degree Project, Structure-from-Motion for Autonomous Ultrasound, IIT Madras INSPIRE Lab** — Jan–May 2024.
  Advisor: Nirav Patel (NOTE: spelled "Patel", master.tex sometimes wrongly says "Partel").
  COLMAP SfM from monocular RGB → human torso reconstruction for low-cost ultrasound; autonomous
  scanning with 5-DoF arm + single RGB camera; ROS, MoveIt, Gazebo; perception→planning loop.
- **Offline & Online Motion Planning/Control of UAVs, IIT Madras Young Research Fellowship** — Sep 2021 – Apr 2022.
  Advisor: Prof. Satadal Ghosh. Target-driven motion planning + obstacle avoidance for UAVs; Proportional
  Navigation + Acceleration-Velocity Obstacles in 2D; ~20% faster & more compute-efficient than classical
  aerospace algorithms.

## Notable course / personal projects (KTH unless noted) — see [[project-deep-reference]] for depth
- **Robot Learning & Embodied AI** (DD2600, confirmed) — 3D open-vocab semantic mapping (ARKitScenes RGB-D,
  OwlV2 + SAM + CLIP, depth-fusion 2D→3D); deployed pretrained VLA model for manipulation; generalization study.
- **Deep Learning Advanced (DD2610)** — MeanFlow one-step generative modeling: reproduced + extended,
  ablations on time sampler / CFG / r≠t ratio, Classification Accuracy Score (CAS) critique. Practicals:
  MeanFlow, MAE, SimCLR, FixMatch, Uncertainty Estimation (Deep Ensembles + VI). No VAE practical.
- **Multi-Agent Systems (DD2438)** — MAPF: Hybrid A* + Conflict-Based Search (CBS) for 20+ holonomic
  (drone) / non-holonomic (car) agents; greedy "bakery" goal assignment. Plus Pacman CTF (RL+BT).
- **Artificial Intelligence (DD2380)** — Path planning: Hybrid A* + waypoint tracking for car & drone.
- **Image Analysis & Computer Vision (single-ComVis target)** — Fourier/FFT filtering, multi-scale
  differential-geometry edge detection (L_vv, L_vvv), Hough; SIFT+RANSAC homography/fundamental matrix, triangulation.
- **Applied Estimation (EL2320)** — 2D EKF-SLAM in MATLAB, known + unknown data association, filter
  consistency/overconfidence analysis (solo project).
- **Control Theory Advanced / Advanced Control (EL2520)** — Four-Tank process: modeling, RGA, min/non-min
  phase, decentralized + robust Glover-McFarlane control (team of 4).
- **Introduction to Robotics (DD2410)** — IK solver from scratch (7-DoF KUKA), RRT* Dubins car, 2D
  occupancy grid mapping, Behavior Tree mission planner for TIAGo (ROS/Gazebo).
- **NOTE:** there is NO "Deep Generative Modelling" course — that entry in old files was erroneous.
  The generative-modeling content is the MeanFlow practical inside DD2610 (above). single-GenMod.tex now
  targets a Generative/Foundation-Model role using DD2610 + ABB thesis content.
- IIT/other: Control of Automotive Systems (heading-angle controller, P/PI brake, Sliding Mode tractor
  hitch); Human Powered Segway (Fusion360 CAD + COMSOL stress); Path Finder PyQt5 (A*, Dijkstra);
  VR + RL shooter (PPO, Unity, superhuman, VR); Python API for Fusion360 (CSV-driven model duplication);
  Discord bot (C#, ffmpeg). Hyperloop battery pack (high discharge, Al heat sink +10% life / −10°C peak,
  top-24 European Hyperloop Week Valencia).

## Technical Skills
- Languages: Python, C, C++, C#
- Robotics/Sim: ROS/ROS2, MoveIt, Gazebo, MuJoCo, PyBullet, Unity3D, Unity ML-Agents, CoppeliaSim, MATLAB
- ML/DL: PyTorch, JAX, OpenCV, wandb, (YOLO)
- Tools: Docker, Git, LaTeX, CUDA, Slurm, VS Code
- CAD/CAE: Fusion360, Solidworks, Ansys, COMSOL

## Achievements / Leadership
- IIT Madras Young Research Fellowship (top 30 of 800+).
- JEE Advanced 97.64 %ile, JEE Mains 99.10 %ile (of 1.5M); UCEED All-India Rank 52 of 50k.
- Head of Industrial & Public Relations, Dept. of Engineering Design IITM (1,200+ students, first hybrid recruitment).
- Strategist, Computer Vision & Intelligence Group (CVIG) IITM (DL summer school 500+).
- Associate Manager, E-Cell IITM; GTA Field & Service Robotics (ID4060, 40 students); THS Student Buddy (KTH).
- IIT Madras Volleyball (Agrata); national drawing competition winner (Times of India); Valorant Silver 2.
