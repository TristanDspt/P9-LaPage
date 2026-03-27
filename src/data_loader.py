import pandas as pd
import streamlit as st

@st.cache_data
def get_csv():

    df = pd.read_csv("data/processed/final.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['categ'] = df['categ'].astype('category')
    df['sex'] = df['sex'].astype('category')
    df = df.set_index('date')

    return df

def profil_client(df, choix):

    if choix != 'Global':
        df = df.query("segment == @choix")

    return df