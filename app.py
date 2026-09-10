import streamlit as st

# Pagina-instellingen
st.set_page_config(
    page_title="De Droomballon",
    page_icon="🎈",
    layout="wide"
)

# Algemene CSS voor grote kleuter-vriendelijke knoppen
st.markdown("""
    <style>
    .stButton>button {
        font-size: 20px !important;
        padding: 15px 25px !important;
        border-radius: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎈 Basisschool De Droomballon")
st.write("Samen met **Wiebel** en **Pola** leren we de afspraken op de speelplaats!")

# Navigatie aan de zijkant
zone = st.sidebar.radio(
    "Kies een speelplaats:",
    ["Hoofdmenu", "Peuterspeelplaats", "Kleuterspeelplaats", "L1234 & L56"]
)

if zone == "Hoofdmenu":
    st.subheader("Welkom! Kies een zone in het menu links om te beginnen.")

elif zone == "Kleuterspeelplaats":
    st.header("🛝 De Kleuterspeelplaats")
    
    tab1, tab2 = st.tabs(["🛞 Het Herstelwiel", "🔔 De Bel & Opruimen"])
    
    with tab1:
        st.subheader("Wat doe je bij een probleem op de speelplaats?")
        st.info("Oefen mee met Wiebel en Pola!")
        
        # Scenario selectie
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
            st.write("### 🤝 Je bent per ongeluk tegen iemand aan gelopen. Wat kies je op het Herstelwiel?")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💬 Zeg SORRY"):
                    st.success("Super! Een eerlijke 'sorry' helpt meteen.")
            with col2:
                if st.button("✋ High-five of Knuffel"):
                    st.success("Mooi zo! Maak het weer goed met elkaar.")
            with col3:
                if st.button("😡 Boos weglopen"):
                    st.error("Probeer het liever goed te maken met het Herstelwiel!")

        elif scenario == "Je bent heel boos":
            st.write("### 🧘 Je bent heel erg boos. Hoe koel je af?"):
            if st.button("🔢 Ik tel tot 10 en koel af"):
                st.balloons()
                st.success("1... 2... 3... 4... 5... 6... 7... 8... 9... 10! Wat een goeie reflex!")

    with tab2:
        st.subheader("Binnenkort: Spelletjes over de bel en opruimen!")
