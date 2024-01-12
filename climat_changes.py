import pandas as pd
import plotly.express as px
import streamlit as st

# Read the data
@st.cache
def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name='Data', skiprows=3)
    # We'll only keep columns from 2000 to 2021 for consistency with your previous code
    # Ensure that the years are correctly labeled in your Excel sheet
    columns_to_keep = ["Country Name"] + [str(year) for year in range(2000, 2022)]
    electricity_data = df[columns_to_keep]
    electricity_data = electricity_data.rename(columns={"Country Name": "Country"})
    # Melt the dataframe to have a long-form dataframe suitable for line plots with Plotly
    return electricity_data.melt(id_vars=["Country"], var_name="Year", value_name="Electricity Production from Oil")

# Replace 'file_path' with the path to your actual data file
file_path = '/Users/caterinasapuppo/Desktop/API_EG.ELC.PETR.ZS_DS2_en_excel_v2_6299411.xls'
electricity_data_melted = load_data(file_path)

# Sidebar for country selection
country = st.sidebar.selectbox('Select a Country', electricity_data_melted['Country'].unique())

# Filter data based on selection
filtered_data = electricity_data_melted[electricity_data_melted['Country'] == country]

# Plotting
fig = px.line(filtered_data, 
              x="Year", 
              y="Electricity Production from Oil", 
              title=f"Electricity Production from Oil Sources (%) for {country} from 2000 to 2021",
              markers=True)

# Set line and axes properties
fig.update_traces(line=dict(color='black', width=2))
fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True, title='')
fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True, title='')
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)
fig.update_layout(autosize=False, width=800, height=600, 
                  plot_bgcolor='white', 
                  margin=dict(l=20, r=20, t=50, b=20),
                  title_font=dict(color='darkgrey'), 
                  font=dict(color='black'))

# Display the plot
st.plotly_chart(fig)
