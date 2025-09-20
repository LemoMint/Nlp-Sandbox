import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO)

main_path = Path("../data/raw/raw.csv")
cols = ["Комментарии", "Эмоциональная окраска"]
sheet_names = ["UX", "GP", "AS"]

frames = []

logging.info("Start reading files")

for sheet in sheet_names:
    logging.info(f"Reading sheet: {sheet}")
    df = pd.read_excel(main_path, sheet_name=sheet, usecols=cols)
    frames.append(df)

result = pd.concat(frames, ignore_index=True)

logging.info(f"Final dataset shape: {result.shape}")

output_path = Path("../data/interim/comments.csv")
result.to_csv(output_path, index=False, encoding="utf-8-sig")

logging.info(f"File saved to {output_path}")
