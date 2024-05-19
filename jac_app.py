import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.stoggle import stoggle
from streamlit_option_menu import option_menu


st.header('Bienvenidos  al Mundo  🌎 de StreamLit, con el poder de Python')
if st.button('Globos?'):
    st.balloons()

stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)


# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected


# 3. CSS style definitions
selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

selected3

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")

# Título de la aplicación
st.title('Gráficos con Plotly y Streamlit')

# Leer el archivo .DAT
file_path = 'S_REG005.DAT'

# Supongamos que los datos están separados por dos puntos (:)
df = pd.read_csv(file_path, delimiter=':', header=None)

# Suponiendo que conocemos las columnas, podemos definirlas
df.columns = ["ID", "Description", "Code1", "Code2", "Opera"]

# Separar el último campo "Opera" en las partes especificadas
pattern = r'(\d{2})([+-]\d{6})([+-]\d{7})([+-]\d{10})'
extracted_data = df['Opera'].str.extract(pattern)

# Eliminar espacios en blanco alrededor de las descripciones
df['Description'] = df['Description'].str.strip()

# Filtrar el DataFrame para eliminar filas con Description en blanco o específicas
exclude_descriptions = ["", "Category", "Diferencias","Diferencia", "RETIRO","Arqueo","Retiros","Retiro","Category ","Remanente"]
#exclude_id = [852,853]
exclude_id_range = range(1, 900)  # El rango va de 852 a 890 inclusive

df = df[~df['Description'].isin(exclude_descriptions) & ~df['ID'].isin(exclude_id_range)]

# Procesar la columna "Opera" para obtener los últimos 11 caracteres, manejar el signo y dividir entre 100
df['Opera'] = df['Opera'].str[-11:]  # Tomar los últimos 11 caracteres
df['Opera'] = df['Opera'].apply(lambda x: float(x) / 100)  # Convertir a float y dividir entre 100

# Seleccionar columnas para el gráfico en el sidebar
x_axis = st.sidebar.selectbox("Selecciona la columna para el eje X", df.columns, index=df.columns.get_loc('Description'))
y_axis = st.sidebar.selectbox("Selecciona la columna para el eje Y", df.columns, index=df.columns.get_loc('Opera'))

# Crear un gráfico de dispersión interactivo con Plotly Express
fig = px.scatter(df, x=x_axis, y=y_axis)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
# Mostrar los datos del DataFrame con las nuevas columnas
st.write("Datos del archivo S_REG005.DAT 18 de Mayo 2024 con columnas extraídas:")
st.write(df)