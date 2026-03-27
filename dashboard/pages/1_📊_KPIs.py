import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.data_loader import get_csv, profil_client
from src.statistics import get_kpi
from src.ui import afficher_metriques, afficher_top_flop


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
kpis = get_kpi(df_filtre)


# --- 5. INTERFACE GRAPHIQUE ---

st.markdown("<h1 style='text-align: center;'>📊 KPI's</h1>", unsafe_allow_html=True)

titres = {
    "Global": "BtoB & BtoC",
    "BtoC": "Clients BtoC",
    "BtoB": "Clients BtoB"
}

st.markdown(f"<h2 style='text-align: center;'>{titres[choix]}</h2>", unsafe_allow_html=True)
st.divider()
afficher_metriques(kpis)
st.divider()
afficher_top_flop(df_filtre)