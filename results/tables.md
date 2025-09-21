# Results Tables

## Table 1 — Evaluation results on CIRR
Comparing the origin of the evaluation (O.R.), with personal (O: Ours) and paper (T: Their) results, for various pretraining data (P.D.) and training data (T.D.) configurations.

| P.D.   | T.D.  | O.R. | R@1   | R@5   | R@10  | R@50  | Rsub@1 | Rsub@2 | Rsub@3 |
|--------|-------|------|-------|-------|-------|-------|--------|--------|--------|
| -      | -     | T    | 19.76 | 41.23 | 50.89 | 71.64 | 63.04  | 81.01  | 89.37  |
| -      | -     | O    | 20.02 | 42.00 | 52.34 | 73.57 | 64.77  | 83.42  | 91.98  |
| -      | CIRR  | T    | 48.84 | 78.05 | 86.10 | 94.19 | 75.78  | 88.22  | 92.80  |
| -      | CIRR  | O    |   -   |   -   |   -   |   -   |   -    |   -    |   -    |
| WebVid | -     | T    | 38.48 | 66.70 | 77.25 | 91.47 | 69.28  | 83.76  | 91.11  |
| WebVid | -     | O    | 39.28 | 68.24 | 78.94 | 94.65 | 71.28  | 86.22  | 94.02  |
| WebVid | CIRR  | T    | 49.69 | 78.60 | 86.77 | 94.31 | 75.01  | 88.12  | 93.16  |
| WebVid | CIRR  | O    | 50.04 | 80.96 | 89.33 | 97.64 | 77.25  | 91.04  | 96.34  |

---

## Table 2 — Training reproduction vs baseline (CIRR)

| P.D.        | T.D.  | O.R. | R@1   | R@5   | R@10  | R@50  | Rsub@1 | Rsub@2 | Rsub@3 |
|-------------|-------|------|-------|-------|-------|-------|--------|--------|--------|
| -           | CIRR  | T    | 48.84 | 78.05 | 86.10 | 94.19 | 75.78  | 88.22  | 92.80  |
| -           | CIRR  | T.R. | 49.33 | 80.72 | 88.92 | 97.61 | 76.70  | 90.29  | 95.83  |
| WebVid-CoVR | CIRR  | O    | 50.34 | 80.96 | 89.33 | 97.64 | 77.25  | 91.04  | 96.34  |
| WebVid-CoVR | CIRR  | T.R. | 49.13 | 80.70 | 89.23 | 97.49 | 76.12  | 90.02  | 95.74  |

---

## Table 3 — Dataset statistics
Filtering using WebVid metadata

| Dataset                         | # Target Videos | # Triplets | # Query Videos |
|---------------------------------|-----------------|------------|----------------|
| WebVid-CoVR                     | 129,954         | 1,644,276  | 129,921        |
| WebVid-CoVR Same Author         | 20,727          | 99,861     | 20,727         |
| WebVid-CoVR Same Category       | 47,334          | 325,320    | 47,331         |
| WebVid-CoVR Same Author/Category| 48,097          | 339,265    | 48,093         |


---

## Table 4 — WebVid-CoVR test dataset results
Results of CoVR models trained on filtered data

| Pretraining Data   | R@1   | R@5   | R@10  | R@50  |
|--------------------|-------|-------|-------|-------|
| -                  | 15.85 | 32.79 | 40.30 | 58.37 |
| WebVid-CoVR        | 55.75 | 81.77 | 89.44 | 98.32 |
| WebVid-CoVR_F      | 52.82 | 80.05 | 87.64 | 97.93 |
| WebVid-CoVR_F_S.I  | 55.20 | 81.06 | 89.01 | 98.20 |

---

## Table 5 — CIRR evaluation with different pretraining & combiner methods
Overall Results with various Pretraining Data and combiner methods

| Mode      | Pretraining Data   | C.M. | R@1   | R@5   | R@10  | R@50  | Rsub@1 | Rsub@2 | Rsub@3 |
|-----------|-------------------|------|-------|-------|-------|-------|--------|--------|--------|
| Train     | -                 | NA   | 49.33 | 80.72 | 88.92 | 97.61 | 76.70  | 90.29  | 95.83  |
| Train     | -                 | AVG  | 49.33 | 80.19 | 88.55 | 97.57 | 75.35  | 89.35  | 95.59  |
| Train     | -                 | MLP  | 49.33 | 80.99 | 88.89 | 97.59 | 77.23  | 90.39  | 95.83  |
| Train     | WebVid-CoVR       | NA   | 49.13 | 80.70 | 89.23 | 97.49 | 76.12  | 90.02  | 95.74  |
| Train     | WebVid-CoVR       | MLP  | 50.15 | 80.55 | 88.84 | 97.59 | 76.65  | 90.19  | 95.81  |
| Train     | WebVid-CoVR_F     | NA   | 48.96 | 80.75 | 89.25 | 97.66 | 76.39  | 90.22  | 95.74  |
| Train     | WebVid-CoVR_F     | MLP  | 50.55 | 80.48 | 88.89 | 97.61 | 76.73  | 90.02  | 95.69  |
| Train     | WebVid-CoVR_F_S.I | NA   | 49.54 | 80.55 | 88.96 | 97.49 | 76.36  | 89.98  | 95.83  |
| Train     | WebVid-CoVR_F_S.I | MLP  | 50.10 | 80.87 | 88.92 | 97.66 | 76.55  | 90.10  | 95.74  |
| Zero-shot | WebVid-CoVR       | -    | 36.17 | 66.58 | 78.34 | 94.19 | 68.75  | 84.75  | 93.13  |
| Zero-shot | WebVid-CoVR_F     | -    | 37.87 | 67.35 | 78.65 | 94.43 | 70.82  | 86.41  | 94.05  |
| Zero-shot | WebVid-CoVR_F_S.I | -    | 36.63 | 66.43 | 77.81 | 94.10 | 70.02  | 85.21  | 93.59  |
