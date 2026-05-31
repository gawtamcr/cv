---
name: project-deep-reference
description: "Deep technical details (metrics, methods, collaborators, course codes) mined from the 8 report PDFs in references/ — use to fill CV bullets and answer role-specific questions"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 7386347f-e350-4626-bfe2-94970f6fb102
---

# Deep project reference (mined from references/*.pdf, May 2026)

Use these concrete details when a role calls for depth. Each entry: course/venue, collaborators, what was actually done, hard numbers.

## EKF-SLAM (AE_EKF_SLAM_Report.pdf) — EL2320 Applied Estimation, SOLO
2D EKF-SLAM in MATLAB; known + unknown data association. Maximum-likelihood / Mahalanobis gating for
association; dynamic state-vector + covariance expansion for new landmarks (resolved matrix-consistency
bug when initializing landmarks). Known-association: x-error peak ~0.01m, within 3σ (√Σ11≈0.07m) —
consistent. Unknown-association on symmetric maps → divergence, NaN errors: classic EKF overconfidence
(covariance shrinks as error explodes) from linearization + single-hypothesis Gaussian. Motivates
FastSLAM / factor-graph. Based on Probabilistic Robotics (Thrun) + EL2320 lab files.

## Four-Tank Process (CTAP_Project_Report.pdf) — EL2520 (Advanced/Robust Control), TEAM
Team: Cezary Banaszek, Joachim Jobard, Gawtam, Aassik Pazhani. Modeled 4-tank dynamics from first
principles; linearized; transfer function; RGA analysis; minimum vs non-minimum phase (γ1+γ2 condition).
Designed decentralized dynamic-decoupling controller + robustified Glover-McFarlane (H∞ loop-shaping).
Robust controller: min-phase rise ~4s, 20% overshoot, 2% ss error; better disturbance rejection, lower
oscillation. Non-min phase harder (rise ~75s). Experimental k1=5.52, k2=5.45; identified outlet areas.

## MeanFlow (DL_MeanFlow_Report.pdf) — DD2610 Deep Learning Advanced, TEAM
Team: Joar Paganus, Haoran Jin, Gawtam. Reimplemented MeanFlow (one-step generative modeling, learns
average velocity field over finite interval) from scratch in PyTorch (except U-Net arch); MNIST + CIFAR-10.
Ablations on time sampler (logit-normal μ), CFG (ω, κ, p_c), and r≠t ratio (75% best for MNIST).
Introduced Classification Accuracy Score (CAS) for MNIST and showed CAS is unreliable under CFG/guidance
mixing. CIFAR-10 best FID ~160 @ epoch 600 (limited compute, batch 32). Repo: github.com/joarp/meanflow-reproducibility.
DIRECTLY RELEVANT to ABB thesis (flow matching / generative modeling).

## MAPF (MAS_MAPF_Report.pdf) — DD2438 Multi-Agent Systems, Assignment 2, Group 7
Team: Gawtam, Zyad Haddad. Conflict-Based Search (CBS): low-level time-aware A*, high-level constraint
tree (min-heap by makespan), vertex/edge constraints, "earliest conflict first", path reuse. Mitigations:
goal padding, conflict-prioritization node pruning, fail-safe node-expansion bound. Hybrid A* + waypoint
follower (from Group 6) for kinematic agents. "Bakery problem": greedy goal assignment minimizing
accumulated travel distance D_ij = T_i + d_ij. Honest result: CBS-centralized failed most high-complexity
Car-Model benchmarks (no local replanning); Group 1/8 outperformed. Strong on theory, weak on integration.

## Pacman Capture-the-Flag (MAS_PacmanCTF_Report.pdf) — DD2438 Multi-Agent Systems, Group 13
Team: Banah Abdeljaber, Gawtam. Hybrid: custom Behavior Tree (sequence/selector/switched-learning-action/
predicate-condition) for high-level strategy + 3 role-specific PPO policies (attack/defend/escape) via
Unity ML-Agents. Rewards: eat enemy pill +0.0125, kill +1, die −1/−2, time −0.00002, normalized [-1,1].
25-action 5×5 discrete space; raycast(×6) + normalized spatial obs; blackboard for teammate state.
Training: 2-phase (isolation pretrain → joint fine-tune), self-play, curriculum, composite episodes (10k steps),
LR 3e4 decaying, batch 1024. Honest result: scaled poorly to full adversarial maps (obs dimensionality
exploded, near-random walk); succeeded in simple/single-agent. Only team to combine BT + RL.

## Path Planning car & drone (MAS_PathPlanning_Report.pdf) — DD2380 Artificial Intelligence, Assignment 1, Group 24
Team: Max Decman, Gawtam. Modified Hybrid A* with motion primitives from bicycle model (step ~3.5,
wheelbase 2, 11 steering values over 50° car / 9 over 60° drone); orientation binning (18/36) for node
hashing; Euclidean heuristic + sharp-turn penalty; minimal post-processing. Waypoint tracker: car base
speed 10 (max 22), 8-unit switch radius, reverse fallback; drone adaptive braking (decel <11 units,
switch <4). Result: car robust & competitive (initial maps 2nd of 5, total 422.3s); drone failed
terrains K/L/O (fixed-collision-box corner crashes — derived w_adj = w+(l−w)|sin α|). Honest failure analysis.

## VLM + Taxonomy for DOM (VLM_Report.pdf / VLM_ROMADO_Paper.pdf) — KTH RPL, IROS 2025 ROMADO workshop, LEAD AUTHOR
Authors: Gawtam Chithra Ramesh, David Blanco-Mulero (UPC), Yifei Dong. Advisor Prof. Florian Pokorny.
Integrated SOTA VLM (GPT-4o, Gemini) with T-DOM taxonomy (Blanco-Mulero et al.) for long-horizon DOM.
Pipeline: scene image + task → VLM scene comprehension (+ OpenCV) → state abstraction → high-level planner
(action abstraction) → problem manager → PyBullet sim → verification loop. VLM predicts structured taxonomy
codes + NL justification (deformation/motion/interaction types). Metrics: taxonomy-code accuracy (exact/
partial/Hamming), NL correctness (BLEU/ROUGE/METEOR/BERT), robot task success. Finding: VLMs strong on
motion/interaction reasoning, weak on deformation perception. Example F1 0.8–1.0, BERT ~0.75. Used Gemini
for language editing only. Targeting IROS2026 + IJRR full version.

NOTE on course codes: master.tex labels nearly everything "DD2348" — WRONG. Correct: DD2438=Multi-Agent
Systems, DD2380=Artificial Intelligence, DD2610=Deep Learning Advanced, EL2320=Applied Estimation,
EL2520=Advanced Control, DD2410=Introduction to Robotics, **DD2600=Robot Learning & Embodied AI** (confirmed).
There is NO "Deep Generative Modelling" course (erroneous in old files) — generative content lives in DD2610 (MeanFlow).
