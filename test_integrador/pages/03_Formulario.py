import streamlit as st
import datetime
import csv

def ExisteMail():
    ruta = "./usuarios.csv"
    fieldnames = st.session_state.info_usuario.keys()
    with open(ruta, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)
        for fila in reader:
            if fila["Mail"] == st.session_state.info_usuario["Mail"]:
                return True
    return False

def GuardarArchivo(dic):
    ruta = "./usuarios.csv"
    fieldnames = dic.keys()
    with open(ruta, "a", newline='') as file:
        file.write("\n")
        file_dic = csv.DictWriter(file, fieldnames=fieldnames)
        file_dic.writerow(dic)
    return None

st.session_state.info_usuario = {}
st.set_page_config(
    page_title="Formulario",
    page_icon="📝"
)
titulo_paginas = ["Formulario","Datos del usuario"]
tab1,tab2 = st.tabs(titulo_paginas)

#with tab1:
#    st.header("Formulario")
#    st.subheader("Ingrese los siguiente datos.")
#    with st.form as formulario:
#        st.text_input("Ingrese su nombre: ")
#        st.text_input("Ingrese su mail: ")
#        st.date_input("Ingrese su fecha de nacimiento: ")
#        genero = st.selectbox("Selecciona tu genero",["Masculino","Femenino","Otro"])
     
with tab1:
    with st.form("mi_formulario"):
        st.session_state.info_usuario = {}
        st.header("Formulario")
        st.subheader("Ingrese los siguientes datos.")
        st.session_state.info_usuario["Nombre"] = st.text_input("Ingrese su nombre:")
        st.session_state.info_usuario["Mail"] = st.text_input("Ingrese su mail:")
        st.session_state.info_usuario["Fecha de nacimiento"] = st.text_input("Ingrese su fecha de nacimiento:",placeholder="XX/XX/XX")
        st.session_state.info_usuario["Genero"]= st.selectbox("Selecciona tu género", ["Masculino", "Femenino", "Otro"],placeholder="--Selecciona un genero--")
        if not ExisteMail():
            st.session_state.submit_button = st.form_submit_button(label='Submit')   
        else:
            st.error("!El mail ya se encuentra registrado!")

        
#Nombre de usuario
#- Nombre Completo
#- Mail
#- Fecha de nacimiento
#- Género
#
with tab2:
   if (st.session_state.submit_button) and ExisteMail():
       st.header("Resultados del usuario")
       st.subheader("Resultados del último envío:")
       st.write("Nombre:", st.session_state.info_usuario["Nombre"])
       st.write("Email:", st.session_state.info_usuario["Mail"])
       st.write("Fecha de nacimiento:", st.session_state.info_usuario["Fecha de nacimiento"])
       st.write("Género:", st.session_state.info_usuario["Genero"])
       GuardarArchivo(st.session_state.info_usuario)
   else:
       print("Nada")