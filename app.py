import streamlit as st

# Pagina-instellingen
st.set_page_config(
    page_title="De Droomballon - Speelplaats Afspraken",
    page_icon="🎈",
    layout="wide"
)

# Titel & Welkom
st.title("🎈 Welkom op Basisschool De Droomballon!")
st.write("Samen met **Wiebel** en **Pola** leren we de afspraken op de speelplaats.")

# Zijbalk navigatie voor zones
st.sidebar.title("Kies een speelplaats 🏫")
zone = st.sidebar.radio(
    "Waar wil je spelen?",
    ["Hoofdmenu", "Peuterspeelplaats", "Kleuterspeelplaats", "L1234 & L56"]
)

# Pagina inhoud afhankelijk van gekozen zone
if zone == "Hoofdmenu":
    st.subheader("Kies een speelzone in het menu aan de linkerkant!")
    # Hier plaatsen we later de interactieve plattegrond

elif zone == "Kleuterspeelplaats":
    st.header("🛝 De Kleuterspeelplaats")
    st.write("Kies een spelletje om de afspraken te oefenen:")
    
    tab1, tab2 = st.tabs(["🛞 Herstelwiel", "🔔 De Bel & Opruimen"])
    
    with tab1:
        st.subheader("Wat doe je bij een probleem?")
        # Hier bouwen we het herstelwiel-scenario
        
    with tab2:
        st.subheader("Wat doe je als de bel gaat?")
        # Hier bouwen we het reactiespel
