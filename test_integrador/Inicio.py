import streamlit as st
st.set_page_config(
    page_title="Inicio",
    page_icon="🏠"
)
titulos_pestanas = ['Tema A', 'Tema B', 'Tema C']
pestaña1, pestaña2, pestaña3 = st.tabs(titulos_pestanas)

# Agregar contenido a cada pestaña
with pestaña1:
    st.header('Tema A')
    st.write('Contenido del tema A')

with pestaña2:
    st.header('Tema B')
    st.write('Contenido del tema B')

with pestaña3:
    st.header('Tema C')
    st.write('Contenido del tema C')