import streamlit as st

st.header('Hola Mundo StreamLit 🌎!, con el Poder de Python')
if st.button('Globos?'):
    st.balloons()

# Leer el archivo
file_path = 'S_RE005.DAT'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Procesar el contenido del archivo
data = []
for line in lines:
    parts = line.strip().split(':')
    if len(parts) == 7:
        code, description, group, val1, val2, val3, val4 = parts
        data.append([code, description, group, val1, val2, val3, val4])

# Crear un DataFrame de pandas
df = pd.DataFrame(data, columns=['Code', 'Description', 'Group', 'Value1', 'Value2', 'Value3', 'Value4'])

# Mostrar el DataFrame en Streamlit
st.title('Tabla de Datos del Archivo s_reg005.dat')
st.dataframe(df)    
