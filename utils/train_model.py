import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

from sklearn.metrics import classification_report

import joblib

import os

from preprocess import preprocess


# ----------------------------
# Load Dataset
# ----------------------------

current_dir = os.path.dirname(__file__)

project_dir = os.path.dirname(current_dir)

csv_path = os.path.join(project_dir, "data", "dataset_A.csv")

df = pd.read_csv(csv_path)


# ----------------------------
# Preprocess
# ----------------------------

df["Description"] = df["Description"].apply(preprocess)


# ----------------------------
# Split
# ----------------------------

X = df["Description"]

y = df["Disaster"]

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)


# ----------------------------
# Build Pipeline
# ----------------------------

model = Pipeline([

    ("tfidf", TfidfVectorizer()),

    ("classifier", LogisticRegression(max_iter=1000))

])


# ----------------------------
# Train
# ----------------------------

model.fit(X_train, y_train)


# ----------------------------
# Evaluate
# ----------------------------

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))


# ----------------------------
# Save Model
# ----------------------------

os.makedirs(

    os.path.join(project_dir, "models"),

    exist_ok=True

)

joblib.dump(

    model,

    os.path.join(project_dir, "models", "alertaid_model.pkl")

)

print("\nModel Saved Successfully!")