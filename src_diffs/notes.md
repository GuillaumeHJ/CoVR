# Code Contributions — CoVR Project

This folder (`src_diffs/`) contains the main code contributions I made while working on the CoVR project, under the supervision of Lucas Ventura.  
The full integration of these changes can be found in our fork’s commit history:  
👉 https://github.com/arthurbr11/CoVR

---

## 1. MLP Combiner for Query Fusion
**Commit:** [bf2c0e1](https://github.com/arthurbr11/CoVR/commit/bf2c0e119944d4eabf559c9d64572a717ddd925f#diff-fce1f0b382dadccbf2978acdd597b5abb3407e7a4b906192bac1f31f7aef85bb)

- **File modified:** `blip_cir.py`  
- **Motivation:** Allow flexible combination of query-image and query-text features beyond simple averaging.  
- **Key additions:**
  - New argument `combination_method ∈ { "NA", "avg", "MLP" }`.  
  - Introduced a lightweight MLP (`nn.Sequential`) to dynamically compute weights over the three embeddings:  
    - similarity feature `f(q, t)`  
    - reference image embedding  
    - reference caption embedding  
  - Predicted weights are normalized with a softmax and applied to produce the final combined embedding.  
  - Hidden dimension configurable via `hidden_dim` (default: 128).  
- **Outcome:** Enabled the model to learn adaptive weighting between modalities, improving retrieval performance compared to static averaging.  

For clarity, the extracted standalone version is provided here:  
📄 [`mlp_combiner.py`](mlp_combiner.py)

---

## 2. WebVid Filtering Script
**Commit:** [462b469](https://github.com/arthurbr11/CoVR/commit/462b4694ec5704c461ec2e33d628b5294911a1ef)

- **File added:** `filter_webvid.py`  
- **Purpose:**  Retain video triplets with common **authors** or **categories** (based on WebVid metadata).  
- **Functionality:**
  - Loads WebVid metadata.  
  - Removes mismatched samples to ensure higher-quality training data.  
  - Outputs a cleaned version of the dataset indices for downstream training.  
- **Role:** Preprocessing step to reduce noise and improve visual consistancy for better learning.

---

## Repository Structure (this folder)

- `mlp_combiner.py` — Extracted MLP combiner implementation from `blip_cir.py`.  
- `filter_webvid.py` — Full filtering script added for WebVid preprocessing.  
- `notes.md` — Documentation of the above contributions with links to commits.

---

### Summary
- **MLP Combiner** (commit `bf2c0e1`): Adaptive feature fusion between query, image, and text embeddings.  
- **WebVid Filtering** (commit `462b469`): Improved dataset quality through metadata-based filtering.  

These were my two main code contributions to the CoVR project.
