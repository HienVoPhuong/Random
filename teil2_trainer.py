import streamlit as st
import random
import time

# ------------- PAGE CONFIG -------------
st.set_page_config(page_title="A1 Sprechen – Teil 2 Trainer", page_icon="🗣️", layout="centered")

# ------------- CSS STYLE -------------
st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5em 1.5em;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #135589;
    }
    .timer {
        font-size: 48px;
        color: #ff4b4b;
        font-weight: bold;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ------------- DATA -------------
themen = [
    {"Einheit": "1. Sommerkurs in Leipzig", "Stichwörter": ["kennen lernen", "kommen", "wohnen", "Sprachen lernen", "Deutsch", "am Wochenende"]},
    {"Einheit": "2. Möller oder Müller?", "Stichwörter": ["Nachname", "Wie alt", "verheiratet", "Adresse", "Handynummer", "Kinder haben"]},
    {"Einheit": "3. Arbeiten im Café", "Stichwörter": ["bestellen", "bezahlen", "Kaffee", "Kreditkarte", "trinken", "kosten"]},
    {"Einheit": "4. Lecker essen!", "Stichwörter": ["nehmen", "vegetarisch", "Hauptgericht", "Foodblogger", "fotografieren", "Internet"]},
    {"Einheit": "5. Hast du Zeit?", "Stichwörter": ["Wie spät", "am Morgen", "Wochenende", "aufstehen", "Geburtstagsparty", "einkaufen"]},
    {"Einheit": "6. Meine Stadt", "Stichwörter": ["besichtigen", "im Zentrum", "Sehenswürdigkeiten", "mit dem Bus", "zur Uni", "Wann"]},
    {"Einheit": "7. Der neue Job", "Stichwörter": ["erste Etage", "Erdgeschoss", "Bibliothek", "Papierkorb", "Drucker", "Kantine"]},
    {"Einheit": "8. Freizeit und Hobbys", "Stichwörter": ["Sport", "Freunde treffen", "Seminar", "studieren", "Wochenende", "Prüfung"]},
    {"Einheit": "9. Zuhause", "Stichwörter": ["Studentenwohnheim", "Balkon", "Zimmer", "Fernseher", "Küche", "Wie finden"]},
    {"Einheit": "10. Familie Schumann", "Stichwörter": ["Wie viele", "von Beruf", "Eltern", "Geschwister", "Wann", "2005"]},
    {"Einheit": "11. Viel Arbeit", "Stichwörter": ["arbeiten", "Schichtdienst", "Programmierer", "Baustelle", "Homeoffice", "Seniorenheim"]},
    {"Einheit": "12. Essen und Trinken", "Stichwörter": ["einkaufen", "ein Liter Milch", "Lieblingsessen", "kochen", "Markt", "Obst und Gemüse"]},
    {"Einheit": "13. Fit und gesund", "Stichwörter": ["Sport", "Kopfschmerzen", "wehtun", "zum Arzt gehen", "Tabletten", "Wann"]},
    {"Einheit": "14. Voll im Trend", "Stichwörter": ["Kleidung", "Lieblingsfarbe", "zur Uni", "Größe", "Pullover", "kosten"]},
    {"Einheit": "15. Jahreszeiten und Feste", "Stichwörter": ["Wetter", "Sommer", "Winter", "schwimmen", "Ski fahren", "Wie"]},
    {"Einheit": "16. Ab in den Urlaub", "Stichwörter": ["Urlaub", "Museum", "Radtour", "Wohin", "Meer", "nächstes Jahr"]}
]

# ------------- HEADER -------------
st.title("🗣️ A1 Sprechen – Teil 2 Trainer")
st.subheader("🎯 Luyện tập với chủ đề & từ khóa ngẫu nhiên")

# ------------- RANDOM THEMA BUTTON -------------
if st.button("🎲 Random Thema"):
    thema = random.choice(themen)
    st.success(f"**Thema:** {thema['Einheit']}")
    st.markdown("**🗝️ Stichwörter:**")
    for wort in thema["Stichwörter"]:
        st.markdown(f"- {wort}")

    # TIMER
    if st.button("⏱️ Bắt đầu đếm ngược 60 giây"):
        for i in range(60, -1, -1):
            st.markdown(f'<div class="timer">{i} Sekunden</div>', unsafe_allow_html=True)
            time.sleep(1)
            st.experimental_rerun()

else:
    st.info("Nhấn nút trên để bắt đầu luyện tập 🎤")
