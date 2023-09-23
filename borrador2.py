import streamlit as st

# Inicializamos la lista de registros con cuatro personas de ejemplo
agenda = [
    {"nombre": "Juan", "telefono": "123-456-7890"},
    {"nombre": "María", "telefono": "987-654-3210"},
    {"nombre": "Pedro", "telefono": "555-555-5555"},
    {"nombre": "Laura", "telefono": "888-888-8888"},
]

def agregar_registro():
    nombre = st.text_input("Nombre:")
    telefono = st.text_input("Teléfono:")
    if st.button("Agregar"):
        agenda.append({"nombre": nombre, "telefono": telefono})
        st.success("Registro agregado con éxito")

def eliminar_registro():
    st.write("Selecciona un registro para eliminar:")
    selected_index = st.selectbox("Registros:", [registro["nombre"] for registro in agenda])
    if st.button("Eliminar"):
        for registro in agenda:
            if registro["nombre"] == selected_index:
                agenda.remove(registro)
                st.success(f"Registro de {selected_index} eliminado")

def editar_registro():
    st.write("Selecciona un registro para editar:")
    selected_index = st.selectbox("Registros:", [registro["nombre"] for registro in agenda])
    nuevo_nombre = st.text_input("Nuevo nombre:")
    nuevo_telefono = st.text_input("Nuevo teléfono:")
    if st.button("Editar"):
        for registro in agenda:
            if registro["nombre"] == selected_index:
                registro["nombre"] = nuevo_nombre
                registro["telefono"] = nuevo_telefono
                st.success(f"Registro de {selected_index} editado")

def mostrar_registros():
    st.write("Registros existentes:")
    for registro in agenda:
        st.write(f"Nombre: {registro['nombre']}, Teléfono: {registro['telefono']}")

def main():
    st.title("Agenda de Personas")

    opcion = st.selectbox("Seleccione una opción:", ["Agregar Registro", "Eliminar Registro", "Editar Registro", "Mostrar Registros"])

    if opcion == "Agregar Registro":
        agregar_registro()
    elif opcion == "Eliminar Registro":
        eliminar_registro()
    elif opcion == "Editar Registro":
        editar_registro()
    elif opcion == "Mostrar Registros":
        mostrar_registros()

if __name__ == "__main__":
    main()