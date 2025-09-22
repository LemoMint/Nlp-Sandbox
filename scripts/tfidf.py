import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("../data/output/train.csv")
test = pd.read_csv("../data/output/test.csv")

model = TfidfVectorizer()
X_train_vector = model.fit_transform(train["text"])
X_test_vector = model.transform(test["text"])

lr = LogisticRegression(max_iter=200)
lr.fit(X_train_vector, train["label"])
y_pred = lr.predict(X_test_vector)

with open("../models/tf_idf_start.pkl", "wb") as file:
    pickle.dump(model, file=file)

with open("../models/lr_start.pkl", "wb") as file:
    pickle.dump(lr, file=file)