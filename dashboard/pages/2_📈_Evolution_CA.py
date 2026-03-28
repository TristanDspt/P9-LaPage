import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from components.data_loader import get_csv, profil_client
from components.ui import afficher_ca, afficher_bar_categ, afficher_donuts_categ

# --- 1. CONFIGURATION PAGE ---
st.set_page_config(page_title="KPI's", page_icon="📊", layout="wide")

# Centrage des métriques via CSS
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    [data-testid="stMetricLabel"] {
        justify-content: center;
        width: 100%;
        min-height: 2.5rem;
        display: flex;
        align-items: flex-end;
    }
    [data-testid="stMetricValue"] {
        width: 100%;
    }
    [data-testid="stMetricDelta"] {
    justify-content: center;
    width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)


# --- 2. CHARGEMENT DU CSV ---

df = get_csv()


# --- 3. SIDEBAR ---

with st.sidebar:
    st.title("⚙️ Menu")

    # Choix du focus
    choix = st.sidebar.radio("Menu", ["Global", "BtoC", "BtoB"], label_visibility="collapsed")

# --- 4. CALCULS ---

df_filtre = profil_client(df, choix)


# --- 5. INTERFACE GRAPHIQUE ---

st.markdown("<h1 style='text-align: center;'>📈 Evolution Chiffe d'Affaire</h1>", unsafe_allow_html=True)

titres = {
    "Global": "BtoB & BtoC",
    "BtoC": "Clients BtoC",
    "BtoB": "Clients BtoB"
}

st.markdown(f"<h2 style='text-align: center;'>{titres[choix]}</h2>", unsafe_allow_html=True)
st.divider()

_, col1, col2, _ = st.columns(4)
with col1:
    periode = st.selectbox("Vue", ['Mois', 'Jour'], help="Choix entre CA mensuel et CA journalier")
with col2:
    window = st.number_input("Moyenne Mobile", min_value=1, value=3, step=1, help="Choix de la valeur de la moyenne mobile")

afficher_ca(df_filtre, periode, window)
st.divider()

col3, col4 = st.columns(2)

with col3:
    afficher_bar_categ(df_filtre)
with col4:
    afficher_donuts_categ(df_filtre)
