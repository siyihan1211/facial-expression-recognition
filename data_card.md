Data Card — FER2013

Status: Draft — to be completed after the first successful data load.

Dataset Source

* Dataset: FER2013 (Facial Expression Recognition 2013).
* Source: Kaggle, Facial Expression Recognition Challenge.
* Exact dataset version and download URL: To be recorded after download.
* Download date: To be recorded.
* Redistribution: Raw dataset images will not be included in this public repository.

Data Format

* Input: 48 × 48 grayscale facial image.
* Target: One of seven facial-expression categories.
* Classes: angry, disgust, fear, happy, sad, surprise, neutral.

Dataset Splits

Commonly reported FER2013 split sizes, pending verification against the downloaded dataset:

Split	Usage	Images
Training	Training	28,709
Validation	PublicTest	3,589
Test	PrivateTest	3,589

Actual sample counts will be verified after loading the data.

Class Imbalance

FER2013 has an imbalanced class distribution.

* Happy is the largest category.
* Disgust is significantly underrepresented, commonly reported at approximately 1.5–2% of the training data.
* Exact class counts will be calculated from the downloaded dataset.

Planned handling: Evaluate per-class performance and experiment with class weighting.

Label Quality

FER2013 contains ambiguous and potentially mislabeled examples.

Some classification errors may reflect ambiguity in the dataset labels rather than model failure alone.

A specific label-noise percentage will not be reported without a reliable supporting source.

Preprocessing

To be documented after implementation:

* Image rescaling and normalization.
* Input formatting.
* Data augmentation, if used.
* Any excluded or corrupted samples.

Limitations and Responsible Use

* Facial-expression categories do not necessarily represent a person’s actual emotional state.
* Dataset imbalance and ambiguous labels can affect model performance.
* Results may not generalize to real-world images or different populations.
* This project is not intended for diagnosing mental-health conditions, predicting internal emotions, or clinical decision-making.

Licensing and Redistribution

The exact Kaggle dataset terms will be reviewed before publishing any dataset-derived material.

This repository will contain original project code and documentation, but raw FER2013 images will not be redistributed without verified permission.

To Complete After First Data Load

* [ ]	Record the exact Kaggle dataset URL and version.
* [ ]	Record the download date and verify dataset terms.
* [ ]	Calculate actual sample counts for each split.
* [ ]	Calculate per-class distributions.
* [ ]	Check for corrupted or unreadable images.
* [ ]	Document preprocessing and normalization.
* [ ]	Document augmentation settings, if used.