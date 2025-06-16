import streamlit as st
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="A1 Teil 2 – Stichwort Trainer", page_icon="🗣️", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .thema {
        font-size: 22px;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 20px;
    }
    .stichwort {
        font-size: 30px;
        color: #ff4b4b;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        font-size: 16px;
        padding: 0.6em 1.5em;
    }
    .stButton>button:hover {
        background-color: #135589;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA: Thema + Stichwörter ----------------
themen_dict = {
    "kennen lernen": ["Wie", "kommen", "wohnen", "Welche", "in Deutschland", "aus Genf"],
    "Sprachen lernen": ["Muttersprache", "sprechen", "Deutsch", "lernen", "am Wochenende", "Welche"],
    "Persönliche Daten": ["Nachname", "Wie alt", "verheiratet", "Adresse", "Handynummer", "Kinder haben"],
    "im Café": ["bestellen", "bezahlen", "Was", "Kaffee", "mit Kreditkarte", "ohne Zucker"],
    "Termin im Café": ["zusammen", "getrennt", "wenig Eis", "trinken", "kosten", "Wann"],
    "Im Restaurant": ["nehmen", "vegetarisch", "mit Familie", "magst du", "Hauptgericht", "oft"],
    "Foodblogger": ["Foodblogger", "fotografieren", "posten", "vegetarisches Essen", "Was", "im Internet"],
    "Termin": ["Wie spät", "am Morgen", "haben", "gehen", "am Wochenende", "Wann"],
    "Tagesabläufe": ["aufstehen", "um 19 Uhr", "oft", "Um wie viel Uhr", "einkaufen", "Frühstück"],
    "Geburtstagsparty": ["Wie viele", "beginnen", "Hose oder Jeans", "Wo", "Geschenke", "zu Hause"],
    "Meine Stadt": ["Welche", "besichtigen", "im Zentrum", "Sehenswürdigkeiten", "mit der U-Bahn", "Spezialitäten"],
    "Unterwegs in der Stadt": ["mit dem Auto oder mit dem Bus", "zur Uni", "zu Fuß", "immer", "kommen", "Wann"],
    "Orientierung im Gebäude": ["Wo", "in der ersten Etage", "im Erdgeschoss", "Bibliothek", "liegen", "Kantine"],
    "im Büro": ["Drucker", "hängen", "stehen", "auf dem Schreibtisch", "Papierkorb", "neben dem Regal"],
    "Freizeit und Hobbys": ["in der Freizeit", "Sport", "Freunde treffen", "mit Familie", "machen", "am Wochenende"],
    "Studium": ["Prüfung", "studieren", "Seminar", "im ersten Semester", "in der Bibliothek", "Was"],
    "Wohnen": ["in der Stadt", "im Studentenwohnheim", "Balkon", "liegen", "groß", "Wie finden"],
    "Zimmer und Möbel": ["Welche Zimmer", "im Schlafzimmer", "in der Küche", "hell", "einen Fernseher", "Was"],
    "Meine Familie": ["Wie viele", "von Beruf", "Wo", "besuchen", "Geschwiste", "zusammen"],
    "Familiengeschichte": ["Wie lange", "Wann", "geheiratet", "Eltern", "2005", "Kinder"],
    "im Beruf": ["beruflich", "arbeiten", "am Wochenende", "im Schichtdienst", "im Homeoffice", "Wer"],
    "Arbeitstätigkeiten": ["Arzt", "Programmierer", "Autos reparieren", "Häuser planen", "auf der Baustelle", "im Seniorenheim"],
    "Einkaufen": ["Obst und Gemüse", "ein Liter Milch", "Wie oft", "einkaufen", "auf dem Markt", "kosten"],
    "Kochen": ["Wann", "Lieblngsessen", "Was", "jeden Tag", "kochen", "brauchen"],
    "Sport": ["Welchen Sport", "Wann", "spielen", "fahren", "im Park", "Am Wochenende"],
    "Gesundheit": ["Kopfschmerzen", "wehtun", "zum Arzt gehen", "Tabletten nehmen", "Wie oft", "Wann"],
    "Kleidung und Farben": ["tragen", "Lieblingsfarbe", "helle oder dunkle T-Shirts", "zur Uni", "Wie", "finden"],
    "Im Kleidergeschäft": ["Welche Größe", "Im Angebot", "finden", "kosten", "In Blau", "Pullover"],
    "Wetter": ["Wetter", "regnen", "schneiein", "Wie", "kalt oder heiß", "Grad"],
    "Jahreszeiten und Aktivitäten": ["im Sommer", "im Winter", "schwimmen gehen", "Ski fahren", "Was", "Sport"],
    "Urlaubsaktivitäten": ["schon mal", "Schlafsack", "eine Radtour machen", "Was", "ins Museum gehen", "Urlaub"],
    "Reisen": ["Wohin", "fliegen", "allein oder mit Familie", "im Juli oder im August", "ans Meer", "nächstes Jahr"]
}

# ---------------- STATE ----------------
if "used" not in st.session_state:
    st.session_state.used = set()

# ---------------- FLATTEN ALL (Thema, Stichwort) ----------------
all_pairs = [(thema, wort) for thema, wlist in themen_dict.items() for wort in wlist]
unused = [pair for pair in all_pairs if f"{pair[0]}|{pair[1]}" not in st.session_state.used]

# ---------------- UI ----------------
st.title("🗣️ A1 Teil 2 – Random Stichwort Trainer ")

if len(unused) == 0:
    st.success("🎉 Bạn đã luyện xong TẤT CẢ Stichwörter!")
    if st.button("🔁 Reset"):
        st.session_state.used = set()
        st.experimental_rerun()
else:
    if st.button("🎯 Random Stichwort mới"):
        thema, wort = random.choice(unused)
        st.session_state.used.add(f"{thema}|{wort}")
        st.markdown(f'<div class="thema">📝 Thema: {thema}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="stichwort">🔑 Stichwort: {wort}</div>', unsafe_allow_html=True)

    st.info(f"✅ Đã luyện: {len(st.session_state.used)} / {len(all_pairs)} Stichwörter")
