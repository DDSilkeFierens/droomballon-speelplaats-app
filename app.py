import streamlit as st
import os

# Pagina-instellingen
st.set_page_config(
    page_title="De Droomballon",
    page_icon="🎈",
    layout="wide"
)

# Vrolijke kleuter-styling: grotere knoppen, afgeronde kaarten en heldere kleuren
st.markdown("""
    <style>
    /* Algemene achtergrond */
    .stApp {
        background-color: #F0F9FF;
    }
    /* Grote speelse knoppen */
    .stButton>button {
        font-size: 24px !important;
        font-weight: bold !important;
        padding: 20px !important;
        border-radius: 20px !important;
        border: 3px solid #3B82F6 !important;
        background-color: #FFFFFF !important;
        color: #1E3A8A !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #DBEAFE !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Titelbalk met figuren
col_h1, col_h2 = st.columns([1, 4])
with col_h1:
    if os.path.exists("personages.png"):
        st.image("personages.png", width=130)
with col_h2:
    st.title("🎈 De Droomballon")
    st.write("### Kies met Wiebel en Pola waar je wil spelen!")

st.write("---")

# Zijkant navigatie met grote pictogram-tekst
zone = st.sidebar.radio(
    "📍 Kies je speelplaats:",
    ["🏠 Welkom", "🛝 Kleuterspeelplaats", "🧸 Peuterspeelplaats"]
)

if zone == "🏠 Welkom":
    st.header("Klik aan de zijkant op de speelplaats! 🛝")
    if os.path.exists("personages.png"):
        st.image("personages.png", width=350)

elif zone == "🛝 Kleuterspeelplaats":
    
    # Keuze tussen de 2 hoofdthema's via grote knoppen in plaats van tekst-tabs
    oefening = st.radio(
        "Wat gaan we oefenen?",
        ["🛑 Het Herstelwiel", "🔔 Bel & Opruimen"],
        horizontal=True
    )

    st.write("---")

    # THEMA 1: HERSTELWIEL (Visuele keuzes)
    if oefening == "🛑 Het Herstelwiel":
        st.header("Wat doe je bij een probleem? 🛑")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### 🛑 Zeg STOP")
            if os.path.exists("stop.png"):
                st.image("stop.png", use_column_width=True)
            if st.button("👉 Kies STOP!"):
                st.success("Goed zo! Zeg duidelijk STOP als je iets niet fijn vindt.")

        with col2:
            st.write("### 🙋‍♂️ Vraag hulp aan de juf")
            if os.path.exists("juuf.png"):
                st.image("juuf.png", use_column_width=True)
            if st.button("👉 Roep 'Juuuf?'"):
                st.success("Prima! Hulp vragen is altijd slim.")

        st.write("---")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.write("### 💬 Zeg SORRY")
            if os.path.exists("sorry.png"):
                st.image("sorry.png", use_column_width=True)
            if st.button("👉 Zeg SORRY"):
                st.balloons()
                st.success("Super! Maak het weer goed.")

        with col4:
            st.write("### 🤝 High-five of Knuffel")
            if os.path.exists("knuffel.png"):
                st.image("knuffel.png", use_column_width=True)
            if st.button("👉 Geef een knuffel"):
                st.balloons()
                st.success("Mooi zo! Samen weer vrienden.")

    # THEMA 2: BEL EN OPRUIMEN
    elif oefening == "🔔 Bel & Opruimen":
        st.header("Wat doe je op de speelplaats? 🧼")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### 🔔 De bel gaat!")
            if os.path.exists("rij.png"):
                st.image("rij.png", use_column_width=True)
            if st.button("👉 In de rij staan"):
                st.balloons()
                st.success("Bij de 2e bel sta je netjes in de rij en ben je stil!")

        with col2:
            st.write("### 📦 Opruimtijd!")
            if os.path.exists("opruimen.png"):
                st.image("opruimen.png", use_column_width=True)
            if st.button("👉 Speelgoed opruimen"):
                st.success("Topper! We ruimen samen alles netjes op.")
