import streamlit as st
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="A1 Teil 2 – Stichwort Trainer", page_icon="🗣️", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8f9fa;
    }

    .card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.6s ease;
        text-align: center;
    }

    .thema-title {
        font-size: 22px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 8px;
    }

    .stichwort-main {
        font-size: 34px;
        font-weight: bold;
        color: #e74c3c;
        margin-top: 10px;
    }

    .stichwort-last {
        font-size: 20px;
        font-weight: 500;
        color: #7f8c8d;
        margin-top: 5px;
    }

    .stButton>button {
        background-color: #3498db !important;
        color: white !important;
        font-weight: 600;
        font-size: 18px;
        padding: 0.75em 2em;
        border-radius: 10px;
        margin: 20px 0;
        border: none;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .stButton>button:hover:enabled {
        background-color: #2d80b3 !important;
        transform: scale(1.02);
    }

    .stButton>button:disabled {
        background-color: #d6eaf8 !important;
        color: #2c3e50 !important;
        opacity: 0.6;
        cursor: not-allowed;
    }

    .info-box {
        font-size: 16px;
        margin-top: 20px;
        background-color: #f0f3f4;
        padding: 10px 20px;
        border-left: 5px solid #5dade2;
        display: inline-block;
        border-radius: 6px;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
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

# ---------------- STATE INIT ----------------
if "used" not in st.session_state:
    st.session_state.used = set()
if "last_pair" not in st.session_state:
    st.session_state.last_pair = None

# ---------------- FLATTEN PAIRS ----------------
all_pairs = [(thema, wort) for thema, wlist in themen_dict.items() for wort in wlist]
unused = [pair for pair in all_pairs if f"{pair[0]}|{pair[1]}" not in st.session_state.used]

# ---------------- UI ----------------
st.title("🗣️ A1 Teil 2 – Stichwort Trainer")

if len(unused) == 0:
    st.success("🎉 Bạn đã luyện xong TẤT CẢ Stichwörter!")
    if st.button("🔁 Reset"):
        st.session_state.used = set()
        st.session_state.last_pair = None
        st.rerun()
else:
    if st.button("🎯 Random Stichwort mới"):
        thema, wort = random.choice(unused)
        st.session_state.used.add(f"{thema}|{wort}")
        st.session_state.last_pair = (thema, wort)

# ---------------- DISPLAY ----------------
if st.session_state.last_pair:
    thema, wort = st.session_state.last_pair
    st.markdown(f"""
        <div class="card">
            <div class="thema-title">📝 Thema: <strong>{thema}</strong></div>
            <div class="stichwort-main">🔑 Stichwort: {wort}</div>
        </div>
    """, unsafe_allow_html=True)

    if len(st.session_state.used) > 1:
        # Tìm Stichwort trước đó (trừ cái hiện tại)
        last_list = list(st.session_state.used)[:-1]
        if last_list:
            last_str = last_list[-1]
            last_thema, last_wort = last_str.split("|")
            st.markdown(f"""
                <div class="card">
                    <div class="thema-title">🕑 Stichwort trước đó</div>
                    <div class="stichwort-last">{last_thema} – {last_wort}</div>
                </div>
            """, unsafe_allow_html=True)

# ---------------- INFO BOX ----------------
st.markdown(f"""
    <div class="info-box">
        ✅ Đã luyện: {len(st.session_state.used)} / {len(all_pairs)} Stichwörter
    </div>
""", unsafe_allow_html=True)
