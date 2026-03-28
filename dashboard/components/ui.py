import streamlit as st
from components.charts import make_top_flop, make_ca, make_bar_categ, make_donuts_categ

def afficher_metriques(kpis):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Chiffre d'Affaire",
            value=f"{kpis['ca']:,.0f} €".replace(",", " ")
        )
        st.metric(
            label="Références Catalogue",
            value=f"{kpis['catalogue']:,.0f}".replace(",", " ")
        )
    with col2:
        st.metric(
            label="Clients Uniques / mois",
            value=f"{kpis['moy_unique']:,.0f}".replace(",", " ")
        )
        st.metric(
            label="Catégorie Phare",
            value=kpis['best_categ_name'],
            delta=f"{kpis['best_categ_value']:,.0f} €".replace(",", " ")
        )
    with col3:
        st.metric(
            label="Sessions / mois",
            value=f"{kpis['moy_ventes']:,.0f}".replace(",", " ")
        )
        st.metric(
            label="Best Seller",
            value=kpis['best_pdt_name'],
            delta=f"{kpis['best_pdt_value']:,.0f} €".replace(",", " ")
        )

def afficher_top_flop(df):
    col1, col2 = st.columns(2)

    with col1:
        fig = make_top_flop(df, 'top')
        st.plotly_chart(fig, width='stretch')
    with col2:
        fig = make_top_flop(df, 'flop')
        st.plotly_chart(fig, width='stretch')

def afficher_ca(df, periode, window):
    fig = make_ca(df, periode, window)
    st.plotly_chart(fig, width='stretch')

def afficher_bar_categ(df):
    fig = make_bar_categ(df)
    st.plotly_chart(fig, width='stretch')

def afficher_donuts_categ(df):
    fig = make_donuts_categ(df)
    st.plotly_chart(fig, width='stretch')