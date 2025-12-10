import streamlit as st
import numpy as np
import joblib

# Charger le modèle
model = joblib.load("model_no2_rf.pkl")

st.set_page_config(page_title="Prévision NO₂ – New Delhi", page_icon="🌍")

st.title("🌍 Prévision de la pollution à New Delhi")
st.markdown(
"""
Cette application permet d’anticiper la **qualité de l’air (NO₂) à +6 heures**
afin d’aider les citoyens à **adapter leurs activités** en cas de pollution.
"""
)

# =========================
# MODE D’UTILISATION
# =========================
mode = st.radio(
    "Mode d’utilisation :",
    ["🟢 Citoyen (simplifié)", "🔵 Expert (démo technique)"]
)

st.divider()

# =========================
# MODE CITOYEN
# =========================
if mode == "🟢 Citoyen (simplifié)":

    st.header("✅ Utilisation simplifiée")

    st.markdown("Entrez uniquement les informations que vous connaissez.")
    hour = st.slider("Heure actuelle", 0, 23, 12)
    day = st.slider("Jour du mois", 1, 31, 15)
    month = st.slider("Mois", 1, 12, 6)
    dayofweek = st.slider("Jour de la semaine (0 = lundi)", 0, 6, 3)

    no2_t = st.slider("NO₂ actuel (optionnel)", 0.0, 300.0,  Forty := 40.0)
    no2_t1 = no2_t
    no2_t6 = no2_t

    # -----------------------
    # VALEURS MÉTÉO MOYENNES (AUTOMATIQUES)
    # -----------------------
    temperature = 25.0
    humidity = 50.0
    pressure = 1013.0
    wind = 5.0
    precip = 0.0

    if st.button("🔮 Prédire la qualité de l’air dans 6 heures"):

        X = np.array([[temperature, humidity, pressure, wind, precip,
                       hour, day, month, dayofweek,
                       no2_t, no2_t1, no2_t6]])

        prediction = model.predict(X)[0]

        st.success(f"✅ NO₂ prévu à +6h : **{prediction:.2f} µg/m³**")

        if prediction < 40:
            st.markdown("🟢 **Qualité de l’air : Bonne** ✅")
            st.markdown("➡️ Activités extérieures sans restriction.")
        elif prediction < 80:
            st.markdown("🟠 **Qualité de l’air : Moyenne** ⚠️")
            st.markdown("➡️ Activités modérées recommandées.")
        else:
            st.markdown("🔴 **Qualité de l’air : Mauvaise** ❌")
            st.markdown("➡️ Évitez le sport et les efforts prolongés à l’extérieur.")

# =========================
# MODE EXPERT
# =========================
else:

    st.header("🔬 Mode expert – Paramètres complets")

    temperature = st.slider("Température (°C)", -5.0, 50.0, 25.0)
    humidity = st.slider("Humidité relative (%)", 0, 100, 50)
    pressure = st.slider("Pression (hPa)", 950, 1050, 1013)
    wind = st.slider("Vitesse du vent (km/h)", 0.0, 30.0, 5.0)
    precip = st.slider("Précipitations (mm)", 0.0, 20.0, 0.0)

    hour = st.slider("Heure", 0, 23, 12)
    day = st.slider("Jour", 1, 31, 15)
    month = st.slider("Mois", 1, 12, 6)
    dayofweek = st.slider("Jour de la semaine (0 = lundi)", 0, 6, 3)

    no2_t = st.slider("NO₂ actuel", 0.0, 300.0, 40.0)
    no2_t1 = st.slider("NO₂ t-1", 0.0, 300.0, 38.0)
    no2_t6 = st.slider("NO₂ t-6", 0.0, 300.0, 35.0)

    if st.button("🔮 Prédire le NO₂ à +6h (mode expert)"):

        X = np.array([[temperature, humidity, pressure, wind, precip,
                       hour, day, month, dayofweek,
                       no2_t, no2_t1, no2_t6]])

        prediction = model.predict(X)[0]

        st.success(f"✅ NO₂ prédit à +6h : **{prediction:.2f} µg/m³**")

        if prediction < 40:
            st.markdown("🟢 **Qualité de l’air : Bonne**")
        elif prediction < 80:
            st.markdown("🟠 **Qualité de l’air : Moyenne**")
        else:
            st.markdown("🔴 **Qualité de l’air : Mauvaise (Attention !)**")
