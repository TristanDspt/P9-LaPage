import plotly.graph_objects as go
import pandas as pd


def make_top_flop(df, choix):
    top_flop = df.groupby('id_prod')['price'].sum().reset_index().sort_values(by='price', ascending=False)
    if choix == 'top':
        df_trace = top_flop.head(5)
        name = "Top 5"
    else:
        df_trace = top_flop.tail(5)
        name = "Flop 5"

    fig = go.Figure()

    fig.add_trace(go.Bar(
    name=name,
    x=df_trace['id_prod'],
    y=df_trace['price'],
    hovertemplate="%{y:,.0f} €",
    marker_color=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
    ))

    # Habillage
    fig.update_layout(
        showlegend=False,
        height=600,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=40, b=25, l=25, r=25),
        title=f"{name} ventes (CA par produits)"
    )

    return fig


def make_ca(df, periode, window):
    if periode == 'Mois':
        freq = 'ME'
    else:
        freq = 'D'

    df = df.groupby(pd.Grouper(freq=freq))['price'].sum().to_frame()
    df['moy_mobile'] = round(df['price'].rolling(window=window).mean(), 2)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['price'],
        name="CA",
        mode='lines+markers',
        marker=dict(size=4),
        line=dict(color="#003f5c"),
        hovertemplate="%{y:,.0f} €"
    ))

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['moy_mobile'],
        name="Moyenne mobile",
        mode='lines+markers',
        marker=dict(size=5),
        line=dict(color='#ffa600'),
        hovertemplate="%{y:,.0f} €"
    ))

    # Habillage
    fig.update_layout(
        xaxis=dict(tickformat="%b %Y",),
        legend=dict(orientation='h', y=1.1, x=0.5, xanchor='center'),
        height=400,
        width=800,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=50, b=50, l=50, r=50),
        title="Evolution du chiffre d'affaire"
    )

    return fig


def make_bar_categ(df):
    df = df.groupby('categ', observed=True)['price'].sum().reset_index()
    total = df['price'].sum()
    df['pct'] = df['price'] / total * 100

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name="CA catégorie",
        x=df['categ'],
        y=df['price'],
        customdata=df['pct'],
        hovertemplate="%{y:,.0f} € (%{customdata:.1f}%)",
        marker_color=['#1B2A4A', '#0D6E8A', '#E8A020']
    ))

    # Habillage
    fig.update_layout(
        height=600,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=50, b=50, l=40, r=40),
        title="Repartition CA par Catégories"
    )

    return fig


def make_donuts_categ(df):
    df = df.groupby('categ', observed=True)['id_prod'].count().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=df['categ'],
        values=df['id_prod'],
        hole=0.65,
        hovertemplate="%{value:,.0f}<extra></extra>",
        marker=dict(colors=['#1B2A4A', '#0D6E8A', '#E8A020']),
        textinfo='label+percent'
    ))
    fig.update_layout(
        separators=". ",
        height=600,
        margin=dict(t=50, b=15, l=15, r=15),
        showlegend=False,
        title="Répartition du Catalogue par Catégorie"
    )

    return fig