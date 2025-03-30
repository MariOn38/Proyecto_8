#Carga de librerías
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Carga de datos
df_company = pd.read_csv('moved_project_sql_result_01.csv')
df_chicago = pd.read_csv('moved_project_sql_result_04.csv')

#Título 
st.header('Análisis de vecindarios y empresas de taxis')

neighborhoods_button = st.button('Mostar gráfica de vecindarios')

if neighborhoods_button:
    st.write('Creando una gráfica de barras de los vecinadarios con más viajes')

neighborhoods = df_chicago.sort_values(by='average_trips', ascending=False).head(10) #Creación de botón
fig, ax = plt.subplots()
neighborhoods.plot(
    kind='bar',
    x='dropoff_location_name',
    y='average_trips',
    legend=False,
    xlabel='Vecindarios',
    ylabel='Promedios de viajes',
    title='Top 10 de principales vecindarios por número de finalizaciones',
    color='darkred',
    ax=ax
    )
st.pyplot(fig)

companies_button = st.button('Mostrar gráfico de las empresas de taxis')

if companies_button:
    st.write('Creando una gráfica de barras para las empresas de taxis con más viajes realizados')
    
companies = df_company.sort_values(by='trips_amount', ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
companies.plot(
    kind='bar',
    x='company_name',
    y='trips_amount',
    legend=False,
    xlabel='Empresas de taxi',
    ylabel='Número de viajes',
    title='Distribución de empresas de taxis según el número de viajes realizados',
    color='darkblue',
    ax=ax
    )
st.pyplot(fig)