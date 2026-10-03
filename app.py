import streamlit as st
from utils.retrieval import search_disaster

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AlertAid",
    page_icon="🚨",
    layout="centered"
)

# -------------------------
# Session State
# -------------------------

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

if "prediction" not in st.session_state:
    st.session_state.prediction = ""

if "confidence" not in st.session_state:
    st.session_state.confidence = 0

# -------------------------
# Title
# -------------------------

st.title("🚨 AlertAid")
st.write("### Machine Learning-Based Disaster Detection & Emergency Assistance")

st.markdown("### 📝 Describe the Emergency")

query = st.text_area(
    "",
    placeholder="Example: Heavy rainfall has caused flooding in my area..."
)

st.markdown("#### 💡 Example Descriptions")

st.markdown("""
- Heavy rainfall has flooded my house.
- Strong earthquake has damaged nearby buildings.
- Smoke is rising from the nearby forest.
- Cyclone warning has been issued in my area.
""")

# -------------------------
# Analyze Button
# -------------------------

if st.button("🔍 Analyze Situation"):

    if query.strip() == "":

        st.warning("Please enter an emergency description.")

    else:

        with st.spinner("Analyzing emergency..."):

            prediction, confidence, _, _, _, _ = search_disaster(query)

        st.session_state.analyzed = True
        st.session_state.prediction = prediction
        st.session_state.confidence = confidence

# -------------------------
# Show Prediction
# -------------------------

if st.session_state.analyzed:

    st.success("Disaster Identified Successfully!")

    st.subheader("🚨 Predicted Disaster")
    st.info(st.session_state.prediction)

    st.subheader("🎯 Confidence")

    st.progress(int(st.session_state.confidence))
    st.write(f"**{st.session_state.confidence:.2f}%**")

    st.divider()

    # -------------------------
    # Location
    # -------------------------

    states = {

        "Assam": [
            "Cachar",
            "Barpeta",
            "Dibrugarh",
            "Jorhat",
            "Nagaon"
        ],

        "Odisha": [
            "Puri",
            "Kendrapara",
            "Jagatsinghpur",
            "Ganjam",
            "Balasore"
        ],

        "Uttarakhand": [
            "Chamoli",
            "Rudraprayag",
            "Uttarkashi",
            "Dehradun",
            "Pithoragarh"
        ],

        "Himachal Pradesh": [
            "Kullu",
            "Mandi",
            "Kangra",
            "Chamba",
            "Shimla"
        ],

        "West Bengal": [
            "South 24 Parganas",
            "North 24 Parganas",
            "Purba Bardhaman",
            "Howrah",
            "Kolkata"
        ]
    }

    st.subheader("📍 Select Your Location")

    state = st.selectbox(
        "State",
        list(states.keys())
    )

    district = st.selectbox(
        "District",
        states[state]
    )

    # -------------------------
    # Second Button
    # -------------------------

    if st.button("📋 Get Emergency Information"):

        with st.spinner("Fetching emergency information..."):

            (
                prediction,
                confidence,
                guideline,
                contact,
                hospitals,
                shelters

            ) = search_disaster(
                query,
                state,
                district
            )

        st.divider()

        # -------------------------
        # Guidelines
        # -------------------------

        st.header("📋 Safety Guidelines")

        for i in range(1, 6):
            st.write(f"✅ {guideline[f'Guideline{i}']}")

        st.divider()

        # -------------------------
        # Contacts
        # -------------------------

        st.header("📞 Emergency Contacts")

        col1, col2 = st.columns(2)

        with col1:

            st.metric("Police", contact["Police"])
            st.metric("Ambulance", contact["Ambulance"])

        with col2:

            st.metric("Fire", contact["Fire"])
            st.metric("Disaster Helpline", contact["DisasterHelpline"])

        st.divider()

        # -------------------------
        # Hospitals
        # -------------------------

        st.header("🏥 Nearby Hospitals")

        st.dataframe(
            hospitals,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # -------------------------
        # Shelters
        # -------------------------

        st.header("🏠 Nearby Shelters")

        st.dataframe(
            shelters,
            use_container_width=True,
            hide_index=True
        )

        st.success("✅ Stay Safe. Follow official instructions.")

        #to run - python -m streamlit run app.py