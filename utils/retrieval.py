import os
import joblib
import pandas as pd

from utils.preprocess import preprocess

# -------------------------
# Paths
# -------------------------

current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)

# -------------------------
# Load ML Model
# -------------------------

model = joblib.load(
    os.path.join(project_dir, "models", "alertaid_model.pkl")
)

# -------------------------
# Load Datasets
# -------------------------
# print("PROJECT DIR:", project_dir)
# print("Guidelines:", os.path.join(project_dir, "data", "disaster_guidelines.csv"))
# print("Hospitals:", os.path.join(project_dir, "data", "hospitals.csv"))
# print("Shelters:", os.path.join(project_dir, "data", "shelters.csv"))
guidelines_df = pd.read_csv(
    os.path.join(project_dir, "data", "disaster_guidelines.csv")
)

contacts_df = pd.read_csv(
    os.path.join(project_dir, "data", "emergency_contacts.csv")
)

hospitals_df = pd.read_csv(
    os.path.join(project_dir, "data", "hospitals.csv")
)

shelters_df = pd.read_csv(
    os.path.join(project_dir, "data", "shelters.csv")
)

# -------------------------
# Search Function
# -------------------------

def search_disaster(query, state="", district=""):

    # Preprocess user input
    processed_query = preprocess(query)

    # Predict disaster
    prediction = model.predict([processed_query])[0]

    # Prediction confidence
    confidence = model.predict_proba([processed_query]).max() * 100

    # -------------------------
    # Dataset B1 - Guidelines
    # -------------------------

    guideline = guidelines_df[
        guidelines_df["Disaster"] == prediction
    ].iloc[0]

    # Default values
    contact = None
    hospitals = pd.DataFrame()
    shelters = pd.DataFrame()

    # -------------------------
    # Dataset B2, B3, B4
    # -------------------------

    if state and district:

        contact = contacts_df[
            (contacts_df["State"] == state) &
            (contacts_df["District"] == district)
        ].iloc[0]

        hospitals = hospitals_df[
            hospitals_df["District"] == district
        ]

        shelters = shelters_df[
            shelters_df["District"] == district
        ]

    # -------------------------
    # Return Results
    # -------------------------

    return (
        prediction,
        confidence,
        guideline,
        contact,
        hospitals,
        shelters
    )