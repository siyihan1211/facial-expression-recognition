"""Count FER2013 images per expression, in train and test.

The Kaggle download on this machine is image folders, not fer2013.csv:
data/train/<expression>/*.jpg and data/test/<expression>/*.jpg.
There is no pre-made validation split, so validation will be carved out
of train later. This script only counts what is actually there.

Run from the repo root:
    python src/load_data.py
"""

from pathlib import Path

CLASSES = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
IMAGE_ENDINGS = {".jpg", ".jpeg", ".png"}


def count_split(split_dir):
    """Return {expression: image count} for one split folder."""
    counts = {}
    for expression in CLASSES:
        folder = split_dir / expression
        if not folder.is_dir():
            counts[expression] = None
            continue
        counts[expression] = sum(
            1 for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in IMAGE_ENDINGS
        )
    return counts


def main():
    root = Path(__file__).resolve().parent.parent
    for split in ("train", "test"):
        split_dir = root / "data" / split
        counts = count_split(split_dir)
        print(f"{split}: {split_dir}")
        total = 0
        for expression in CLASSES:
            n = counts[expression]
            if n is None:
                print(f"  {expression:10s} folder missing")
            else:
                print(f"  {expression:10s} {n}")
                total += n
        print(f"  {'total':10s} {total}\n")


if __name__ == "__main__":
    main()
