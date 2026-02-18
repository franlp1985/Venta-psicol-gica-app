import streamlit as st

st.title("💰 VentaPsicologica AI")
st.write("---")

clave = st.sidebar.text_input("Clave Premium", type="password")

if clave == "pincha2026":
    st.success("Acceso Confirmado. ¡A cerrar ventas, Fran!")
    texto = st.text_area("¿Qué te puso el cliente?")
    if st.button("Obtener Respuesta"):
        if "caro" in texto.lower():
            st.write("👉 Decile: 'Entiendo, pero el valor de perder ventas es más caro que este curso.'")
        else:
            st.write("👉 Decile: '¿Qué te parece si arrancamos hoy y ya te paso el acceso?'")
else:
    st.warning("Poné la clave para usar la app.")
