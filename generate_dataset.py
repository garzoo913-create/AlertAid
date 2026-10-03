import pandas as pd
import random
import os

from generator.flood import generate_flood_description
from generator.earthquake import generate_earthquake_description
from generator.landslide import generate_landslide_description
from generator.cyclone import generate_cyclone_description
from generator.forest_fire import generate_forest_fire_description
from generator.heatwave import generate_heatwave_description
from generator.lightning import generate_lightning_description
from generator.avalanche import generate_avalanche_description


NUM_SAMPLES = 1000

dataset = []


# ---------------- Flood ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_flood_description(),

        "Disaster": "Flood"

    })


# ---------------- Earthquake ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_earthquake_description(),

        "Disaster": "Earthquake"

    })


# ---------------- Landslide ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_landslide_description(),

        "Disaster": "Landslide"

    })


# ---------------- Cyclone ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_cyclone_description(),

        "Disaster": "Cyclone"

    })


# ---------------- Forest Fire ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_forest_fire_description(),

        "Disaster": "Forest Fire"

    })


# ---------------- Heatwave ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_heatwave_description(),

        "Disaster": "Heatwave"

    })


# ---------------- Lightning ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_lightning_description(),

        "Disaster": "Lightning"

    })


# ---------------- Avalanche ----------------

for _ in range(NUM_SAMPLES):

    dataset.append({

        "Description": generate_avalanche_description(),

        "Disaster": "Avalanche"

    })


# Shuffle dataset

random.shuffle(dataset)


df = pd.DataFrame(dataset)


# Create data folder if it doesn't exist

os.makedirs("data", exist_ok=True)


df.to_csv("data/dataset_A.csv", index=False)

print("=" * 50)
print("Dataset Generated Successfully!")
print("Total Samples :", len(df))
print("Saved to : data/dataset_A.csv")
print("=" * 50)