Facial Expression Recognition — Project Brief

Draft date: October 9, 2026
Status: In progress — project design and baseline setup.

Research Question

Which facial expression categories does a small CNN confuse most often on FER2013, and how do those errors compare with reported patterns of human expression confusion?

This project focuses on classifying facial expressions in images, not inferring a person’s actual emotional state.

Dataset

* Dataset: FER2013, originally released for the 2013 Facial Expression Recognition Challenge.
* Format: 48 × 48 grayscale facial images.
* Classes (7): angry, disgust, fear, happy, sad, surprise, neutral.
* Reported splits: Training 28,709 / Validation 3,589 / Test 3,589.
* Known limitations: Class imbalance, ambiguous labels, and differences between benchmark images and real-world conditions.

See data_card.md for more details.

Baseline

Train a small convolutional neural network (CNN) end-to-end.

The first goal is to establish a working data-loading, training, and evaluation pipeline, then record the first real validation accuracy in experiments.csv.

Planned Experiments

1. Data augmentation: Compare performance with and without augmentation.
2. Class weighting: Evaluate whether class weighting improves performance on underrepresented categories.
3. Transfer learning (optional): Experiment with a pretrained ResNet if time allows.

Evaluation and Error Analysis

* Validation accuracy.
* Confusion matrix.
* Per-class performance and misclassification examples.
* Comparison with published research on human facial-expression confusion patterns.

The main focus is understanding where the model makes mistakes, rather than maximizing accuracy alone.

Limitations

* Potential label noise and ambiguous expressions.
* Class imbalance, particularly for the disgust category.
* Limited generalizability to real-world images.
* Facial expressions do not necessarily reflect internal emotional states.
* No mental-health or clinical inference.

Project Timeline

Week 1 (October 10–16, 2026) — Initial targets

* Project brief and repository structure.
* Dataset loading and data card.
* First CNN baseline.
* Augmentation and class-weighting experiments, if time allows.
* Confusion matrix and README updates.

October 26, 2026 — Project Milestone

Aim to have an in-progress version containing:

* Project documentation and repository structure.
* Completed data card.
* At least one real baseline result.
* Initial error analysis or a clearly documented analysis plan.

These are planned milestones, not claims of completed work.

Current Status

In progress — project design and baseline setup.

Results and experimental findings will be added only after actual training and evaluation.