# 🚨 AlertAid — Disaster Detection & Emergency Information

AlertAid is a machine learning-based web application developed as part of the **Online Summer Internship Program at JIIT, Noida**.

The application analyzes a user's description of an emergency, predicts the possible disaster category, and retrieves relevant safety guidelines and location-based emergency information.

## ✨ Features

* **Disaster classification:** Predicts a disaster category from a text description.
* **Confidence display:** Shows the model's prediction confidence.
* **Safety guidelines:** Retrieves guidelines relevant to the predicted disaster.
* **Location-based information:** Allows users to select a state and district.
* **Emergency resources:** Displays available emergency contacts, hospitals, and shelters.

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Web application interface
* **Pandas** — Dataset handling and filtering
* **Scikit-learn** — Machine learning pipeline and classification
* **NLTK** — Text preprocessing
* **TF-IDF** — Text feature extraction
* **Logistic Regression** — Disaster classification model
* **Joblib** — Saving and loading the trained model
* **CSV datasets** — Disaster guidelines and emergency resource information

## ⚙️ How It Works

1. The user enters a description of an emergency situation.
2. The text is preprocessed and passed to the trained machine learning pipeline.
3. The model predicts a disaster category and provides a confidence score.
4. The user selects a state and district.
5. AlertAid retrieves relevant safety guidelines and available emergency information from its datasets.

## 📁 Project Structure

```text
AlertAid/
├── app.py
├── data/
│   ├── disaster_guidelines.csv
│   ├── emergency_contacts.csv
│   ├── hospitals.csv
│   ├── shelters.csv
│   └── train.csv
├── generator/
├── models/
│   └── alertaid_model.pkl
├── utils/
│   ├── preprocess.py
│   ├── retrieval.py
│   └── train_model.py
├── generate_dataset.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python 3
* pip

### Installation

Clone the repository:

```bash
git clone https://github.com/garzoo913-create/AlertAid.git
cd AlertAid
```

Install the required libraries:

```bash
pip install streamlit pandas scikit-learn nltk joblib
```

### Run the Application

```bash
streamlit run app.py
```

The application should open in your browser at the local address shown in the terminal.

## 🎓 Learning Outcomes

Through this project, I gained practical experience with:

* Building a text classification pipeline
* Preprocessing text for machine learning
* Working with structured datasets using Pandas
* Integrating a trained model into a Streamlit application
* Retrieving information based on predicted categories and user-selected locations
* Debugging and organizing a Python project

## ⚠️ Disclaimer

AlertAid is an educational project and is **not a substitute for official emergency services or verified real-time disaster alerts**. Its predictions and retrieved information may be incomplete or inaccurate. In an actual emergency, follow official local authorities' instructions and contact appropriate emergency services.

## 👩‍💻 Author

**Garzoo**

GitHub: [@garzoo913-create](https://github.com/garzoo913-create)

---

Developed as part of the Online Summer Internship Program at JIIT, Noida.
