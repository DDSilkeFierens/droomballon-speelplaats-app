import streamlit as st
import os

# Pagina-instellingen
st.set_page_config(
    page_title="De Droomballon",
    page_icon="🎈",
    layout="wide"
)

# Kleuter-vriendelijke styling
st.markdown("""
    <style>
    .stButton>button {
        font-size: 20px !important;
        padding: 15px 25px !important;
        border-radius: 15px !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎈 Basisschool De Droomballon")

# Afbeelding van Wiebel en Pola tonen als deze geüpload is
if os.path.exists("personages.png"):
    st.image("personages.png", width=250)

st.write("Samen met **Wiebel** en **Pola** leren we de afspraken op de speelplaats!")

# Navigatie zijkant
zone = st.sidebar.radio(
    "Kies een speelplaats:",
    ["Hoofdmenu", "Peuterspeelplaats", "Kleuterspeelplaats", "L1234 & L56"]
)

if zone == "Hoofdmenu":
    st.subheader("Welkom! Kies een zone in het menu links om te beginnen.")

elif zone == "Kleuterspeelplaats":
    st.header("🛝 De Kleuterspeelplaats")
    
    tab1, tab2 = st.tabs(["🛞 Het Herstelwiel", "🔔 De Bel & Opruimen"])
    
    # TAB 1: Herstelwiel
    with tab1:
        st.subheader("Wat doe je bij een probleem op de speelplaats?")
        
        scenario = st.selectbox(
            "Kies een situatie:",
            ["Iemand pakt je speelgoed af", "Er is een botsing geweest", "Je bent heel boos"]
        )
        
        st.write("---")
        
        if scenario == "Iemand pakt je speelgoed af":
            st.write("### 🛑 Er pakt iemand zomaar je fiets af! Wat doe je?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔴 Ik zeg STOP!"):
                    st.success("Goed zo! Zeg duidelijk STOP als je iets niet fijn vindt.")
            with col2:
                if st.button("🙋‍♂️ Ik roep 'Juuuf?'"):
                    st.success("Prima! Als het niet lukt, zoek je hulp bij de juf of meester.")

        elif scenario == "Er is een botsing geweest":
            st.write("### 🤝 Je bent per ongeluk tegen iemand aan gelopen. Wat doe je?")
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💬 Zeg SORRY"):
                    st.success("Super! Een eerlijke 'sorry' helpt meteen.")
            with col2:
                if st.button("✋ High-five / Knuffel"):
                    st.success("Mooi zo! Maak het weer goed met elkaar.")
            with col3:
                if st.button("😡 Boos weglopen"):
                    st.error("Probeer het liever goed te maken met het Herstelwiel!")

        elif scenario == "Je bent heel boos":
            st.write("### 🧘 Je bent heel erg boos. Hoe koel je af?")
            if st.button("🔢 Ik tel tot 10 en koel af"):
                st.balloons()
                st.success("1... 2... 3... 4... 5... 6... 7... 8... 9... 10! Rustig worden helpt!")

    # TAB 2: De Bel & Opruimen
    with tab2:
        st.subheader("Wat doe je op de speelplaats?")
        
        oefening = st.radio("Kies een oefening:", ["🔔 De Bel gaat!", "🧸 Opruimen"])
        
        st.write("---")
        
        if oefening == "🔔 De Bel gaat!":
            st.write("### 🔔 Riiiiing! De 2e bel gaat op de speelplaats. Wat doe je?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🚶 Netjes in de rij staan"):
                    st.balloons()
                    st.success("Juist! Bij de 2e bel sta je in de rij. Na het liedje ben je stil!")
            with col2:
                if st.button("🛝 Gewoon verder spelen"):
                    st.error("Oeps! Bij de bel moeten we stoppen met spelen en in de rij gaan staan.")

        elif oefening == "🧸 Opruimen":
            st.write("### 🚜 Het is tijd om naar binnen te gaan. Wat doe je met de driewieler en de schepjes?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📦 Alles netjes opruimen"):
                    st.success("Topper! We ruimen samen al het materiaal op.")
            with col2:
                if st.button("🍃 Laten liggen in de zandbak"):
                    st.error("Vergeet niet: we hebben respect voor het materiaal en ruimen alles op!")
