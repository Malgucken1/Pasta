import streamlit as st
from PIL import Image

# --- SEITENKONFIGURATION ---
st.set_page_config(
    page_title="Basketball Essentials & Empfehlungen",
    page_icon="🏀",
    layout="centered"
)

# --- HEADER UND BILD ---
col1, col2 = st.columns([1, 2])

with col1:
    try:
        image = Image.open("KFB3.jpg")
        st.image(image)
    except FileNotFoundError:
        st.error("Bild 'KFB3.jpg' nicht gefunden.")

with col2:
    st.title("🏀 Basketball Essentials")
    st.caption("Meine persönlichen Empfehlungen rund ums Training, Coaching & Teamplay")

st.markdown("---")

# --- EINLEITUNG ---
st.markdown(
    """
    Willkommen auf meiner kleinen Empfehlungsseite rund um Basketball-Training, Coaching und Teamausrüstung.  
    Ich teile hier einige Produkte, die ich selbst nutze oder für sinnvoll halte – egal ob du Trainer, Spieler oder einfach Fan bist.  
    """
)

st.info(
    """
    **Transparenzhinweis:**  
    Einige Links auf dieser Seite sind sogenannte *Affiliate-Links*.  
    Wenn du über diese Links bei Amazon einkaufst, erhalte ich eine kleine Provision.  
    Für dich entstehen dabei **keine Mehrkosten**.  
    Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.
    """
)

st.markdown("---")

# --- EMPFEHLUNGEN ---
st.header("🏋️‍♂️ Training & Ausrüstung")

st.markdown(
    """
    **1. Taktiktafel für Trainer**  
    Eine gute Taktiktafel ist Gold wert – besonders im Jugendtraining oder bei Auswärtsspielen.  
    [➡️ Jetzt ansehen auf Amazon](https://www.amazon.de/dp/B0BMMT9Q5P?tag=affiliatesche-21)
    """
)

st.markdown(
    """
    **2. Offizieller Wettkampfball**  
    Der *Molten BG4500* ist mein persönlicher Favorit – perfektes Grip, robust und FIBA-approved.  
    [➡️ Zum Molten BG4500 auf Amazon](https://www.amazon.de/dp/B07V6P6XZ8?tag=affiliatesche-21)
    """
)

st.markdown(
    """
    **3. Sporttasche mit Nassfach**  
    Ideal für Turniere und Auswärtsspiele – hält Schmutzwäsche getrennt vom Rest.  
    [➡️ Zur Sporttasche auf Amazon](https://www.amazon.de/dp/B08M9HPF61?tag=affiliatesche-21)
    """
)

st.markdown("---")

st.header("💡 Tipps für Basketball-Teams")

st.markdown(
    """
    - 🧺 **Regelmäßig die Ausrüstung checken:** Viele Teams vernachlässigen Bälle, Pumpen oder Erste-Hilfe-Sets.  
    - 📱 **Digitale Trainingsplanung:** Nutzt Tools wie Trello oder Google Sheets, um Anwesenheit & Übungen zu koordinieren.  
    - 🏆 **Teamgeist vor Technik:** Investiere in Dinge, die Motivation und Zusammenhalt fördern.
    """
)

st.markdown("---")

# --- FOOTER / IMPRESSUM ---
st.info(
    """
    **Impressum (§ 5 TMG):**  
    Betreiber dieser Website:  
    **Niklas Schelkle**  
    Spichernstraße 9  
    24116 Kiel  
    Deutschland  
    📧 E-Mail: [niklasschelkle@gmail.com](mailto:niklasschelkle@gmail.com)

    **Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV:**  
    Niklas Schelkle  

    **Affiliate-Hinweis:**  
    Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.  
    Für dich entstehen keine Mehrkosten.  

    **Datenschutz:**  
    Diese Seite verwendet keine Cookies oder Tracking außerhalb der von Amazon gesetzten Cookies,  
    die für die Zuordnung von Einkäufen erforderlich sind.  
    Weitere Informationen findest du in der [Amazon-Datenschutzerklärung](https://www.amazon.de/gp/help/customer/display.html?nodeId=201909010).

    **Haftungsausschluss:**  
    Trotz sorgfältiger inhaltlicher Kontrolle übernehme ich keine Haftung  
    für die Inhalte externer Links. Für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.
    """
)

st.markdown("---")
st.caption("© 2025 Niklas Schelkle – Alle Rechte vorbehalten.")

