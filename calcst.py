import streamlit as st

st.sidebar.title("Calculadora")

def pedir_valores():
    name = st.text_input("nombre: ")
    n1 = st.number_input("numero 1:")
    n2 = st.number_input("numero 2")

    if st.button("Sumar"):
        st.success(f"Hola {name}")
        st.write(f"{n1} + {n2} = {n1+n2}")

opcion = st.sidebar.selectbox("opciones: ",[
    "Suma","Resta","Multiplicacion","Division","Acerca de"
    ])

match opcion:
    case "Suma":
        st.write("esta es la opcion de suma...")
        pedir_valores()
    case "Resta":
        st.write("esta es la opcion de resta...")
    case "Multiplicacion":
        st.write("esta es la opcion de multiplicacion...")
    case "Division":
        st.write("esta es la opcion de division...")
        st.write("UCOL-FIME-ICI")
        
    