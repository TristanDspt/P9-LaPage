import pandas as pd

def get_kpi(df):

    ca = df.price.sum()
    catalogue = df.id_prod.nunique()

    df_clients = df.groupby(pd.Grouper(freq='MS'))['client_id'].nunique().rename('clients_unique').reset_index()
    moy_unique = df_clients.clients_unique.mean()

    best_categ_name = df.groupby('categ', observed=True)['price'].sum().idxmax()
    best_categ_value = df.groupby('categ', observed=True)['price'].sum().max()

    df_ventes = df.groupby(pd.Grouper(freq='MS'))['session_id'].nunique().rename('ventes_mois').reset_index()
    moy_ventes = df_ventes.ventes_mois.mean()

    best_pdt_name = df.groupby('id_prod')['price'].sum().idxmax()
    best_pdt_value = df.groupby('id_prod')['price'].sum().max()

    return {
        "ca": ca,
        "catalogue": catalogue,
        "moy_unique": moy_unique,
        "best_categ_name": best_categ_name,
        "best_categ_value": best_categ_value,
        "moy_ventes": moy_ventes,
        "best_pdt_name": best_pdt_name,
        "best_pdt_value": best_pdt_value
    }