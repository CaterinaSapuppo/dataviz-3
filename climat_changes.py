import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# Funzione per caricare i dati
@st.cache
def load_data(file_path):
    df = pd.read_excel(file_path, skiprows=3)
    df_melted = df.melt(id_vars=["Country Name"], var_name="Year", value_name="Percentage")
    df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
    df_melted.dropna(subset=['Percentage'], inplace=True)
    return df_melted

# Funzione di tracciamento
def plot_data(country, df_melted):
    country_data = df_melted[df_melted['Country Name'] == country]
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(country_data['Year'], country_data['Percentage'], color='black')
    plt.xticks(np.arange(start=min(df_melted['Year']), stop=max(df_melted['Year']) + 1, step=5))
    plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.PercentFormatter())
    plt.tick_params(axis='both', which='major', length=0)
    plt.title(f'Electricity Production from Oil Sources in {country}')
    return fig

# Main function
def main():
    st.title("Data Visualization App")
    
    # Carica i dati
    file_path = 'dati electricity from oil sources.xlsx'  # Aggiorna con il nome effettivo del tuo file
    df_melted = load_data(file_path)
    countries_with_data = df_melted['Country Name'].unique()

    # Selezione del paese
    country = st.selectbox("Choose a Country", countries_with_data)
    
    # Visualizza il grafico
    if country:
        fig = plot_data(country, df_melted)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
