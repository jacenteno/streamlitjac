import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Bienevendidos a  🌎 de StreamLit, con el Poder de Python')
if st.button('Globos?'):
    st.balloons()


# Título de la aplicación
st.title('Gráficos con Plotly y Streamlit')

# Leer el archivo .DAT
file_path = 'S_REG005.DAT'

# Supongamos que los datos están separados por comas
df = pd.read_csv(file_path, delimiter=':')

# Mostrar los datos del DataFrame
st.write("Datos del una caja  S_REG005.DAT  18 de Mayo 2024:")
st.write(df)

# Seleccionar columnas para el gráfico
x_axis = st.selectbox("Selecciona la columna para el eje X", df.columns)
y_axis = st.selectbox("Selecciona la columna para el eje Y", df.columns)

# Crear un gráfico de dispersión interactivo con Plotly Express
fig = px.scatter(df, x=x_axis, y=y_axis)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
