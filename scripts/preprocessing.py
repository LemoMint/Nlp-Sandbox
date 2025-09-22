import logging
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

main_path = Path("../data/interim/comments.csv")
class_labels = {"мусор":0, "негативная": 1, "нейтральная": 2, "позитивная": 3}
class_colors = {0: "blue", 1: "red", 2: "yellow", 3: "green"}

logging.info(f"Reading file: {main_path}")
df = pd.read_csv(main_path)

logging.info("Preproccessing emotional marks")
df.columns = ["text", "class"]
df["class"] = df["class"].str.lower().map(class_labels).dropna()
df.head()

class_values = df["class"].value_counts()

X = df["text"]
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.9, stratify=y, shuffle=True
)

pd.concat([X_train, y_train], axis=1).to_csv("../data/output/train.csv")
pd.concat([X_test, y_test], axis=1).to_csv("../data/output/test.csv")