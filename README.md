# CoVR Reproduction & Extensions — Guillaume Henon-Just

This repository documents my work reproducing and extending **BLIP-CoVR** (Ventura et al., 2024) 
during my Master's in Machine Learning (MVA @ ENS Paris).  
The work was done in collaboration with my project partner Arthur Bresnu, supervised by Lucas Ventura 
(author of CoVR).

---

## ✨ Project Overview

- **Baseline reproduction:** Reproduced CoVR evaluation on **CIRR** benchmark, verifying the published retrieval performance.
- **MLP-based combiner:** Implemented a lightweight MLP that learns to combine multimodal, image, and text embeddings for image/video retrieval across large datasets. 
  → Improved retrieval R@1 by ~0.8–1.2 points in fine-tuning setups.
- **WebVid-CoVR filtering:** Filtered the large WebVid-CoVR dataset using CleanVid metadata for more consistant training over smaller dataset. Filtered out video-text-video triplet with different author and category.
  → Achieved similar zero-shot performance with ~3× less data and compute.
- **Analysis:** Investigated learned weight distributions and provided qualitative retrieval examples.

---

## 📁 Repository Contents

- `REPORT.pdf` — Full report with methodology, experiments, and discussion.
- `results/` — Experiment outputs (tables, figures, qualitative examples, logs).
- `src_diffs/` — Code snippets showing my modifications to the original CoVR repository ([src_diffs/notes.md](src_diffs/notes.md)):
  - `mlp_combiner.py` — New module for the MLP combiner.
  - `filter_webvid.py` — Dataset filtering script.
  - `notes.md` — Overview of modified files/commits.
- `experiments/` — Config files used for different runs (baseline, MLP, filtered dataset).

⚠️ **Note:** The embeddings and full checkpoints used in these experiments are not included 
(due to storage and compute cost). The results here are drawn from experiments run on GCP, 
and config files for reproductibility are available here.

---

## 🔗 References

- Original repository: [CoVR (Ventura et al.)]([https://github.com/lucas-ventura/CoVR])  
- Paper: Ventura, L. *et al.*, “CoVR: Composed Visual Retrieval with BLIP-2” (2024)  
- This work: Henon-Just G. & Bresnu A., *Extensions of CoVR with MLP-based Combination Methods*, 2024 (see `REPORT.pdf`).

---

## 👨‍💻 Author Contributions

- Ran full training and evaluation pipelines on GCP.  
- Reproduced baseline CoVR results on CIRR.  
- Developed and integrated MLP combiner into the retrieval model.  
- Filtered WebVid-CoVR dataset and evaluated compute-efficient pretraining.  
- Performed weight analysis and curated qualitative retrieval examples.  

---
