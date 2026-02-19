import streamlit as st
import random
import time

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)

# --- BANCO DE DATOS (Lo que le da el cerebro a la app) ---
empatias = ["Te entiendo perfectamente, ", "Comprendo lo que decís, ", "Es una duda lógica, ", "Claro, hoy en día hay que ser cuidadoso, ", "Entiendo tu punto de vista, "]

n_calidad = [
    "pero justamente lo que no se ve a simple vista es la durabilidad del material que usamos.",
    "sin embargo, te aseguro que la terminación está pensada para que no pierda la forma con el uso.",
    "pero mi garantía es que esto te va a durar el doble que cualquier opción más barata.",
    "aunque parezca sencillo, el proceso de fabricación está pensado para resistir el uso intenso.",
    "pero te invito a que lo pruebes; si la calidad no es lo que esperás, nos hacemos cargo nosotros."
]

n_precio = [
    "pero acordate que el precio es lo que pagás hoy y el valor es lo que te llevás a largo plazo.",
    "aunque parezca una inversión alta, pensá en cuánto te vas a ahorrar al no tener que reponerlo pronto.",
    "pero si buscás algo que realmente te solucione el problema, la calidad tiene un costo justificado.",
    "sin embargo, tenemos opciones para que el monto no sea un obstáculo y puedas tener lo mejor.",
    "pero lo barato termina saliendo caro cuando tenés que comprarlo dos veces por falta de calidad."
]

cierres = [
    "¿Querés que te pase un video del detalle para que te quedes tranquilo?",
    "¿Te gustaría probar uno y comprobarlo por vos mismo?",
    "¿Te parece si coordinamos el envío y lo ves en persona?",
    "¿Qué es lo que más te hace dudar para que arranquemos?",
    "¿Te sirve si te hago una atención especial para que lo compruebes hoy?"
]

# --- LÓGICA DE ACCESO ---
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    st.success("¡Motor de VentaPsicologica Activo!")
    chat = st.text_area("¿Qué te puso el cliente?", key="input_chat")

    # EL TRUCO: Le agregamos un 'random' al botón para que Streamlit no lo guarde en memoria
    if st.button("🚀 GENERAR RESPUESTA NUEVA"):
        if not chat:
            st.warning("Pegá el mensaje del cliente.")
        else:
            txt = chat.lower()
            
            # Elegimos al azar CADA VEZ
            inicio = random.choice(empatias)
            cierre = random.choice(cierres)
            
            if any(x in txt for x in ["mala", "calidad", "trucho", "tela", "material", "malo"]):
                nucleo = random.choice(n_calidad)
            elif any(x in txt for x in ["caro", "plata", "dinero", "precio", "costo"]):
                nucleo = random.choice(n_precio)
            else:
                nucleo = "pero justamente mi objetivo es que te lleves algo que te de satisfacción y no un problema."

            respuesta_final = f"{inicio}{nucleo} {cierre}"
            
            # Mostramos un cartelito de "Pensando..." para que se note el cambio
            with st.spinner('Analizando psicología del cliente...'):
                time.sleep(0.5)
                st.subheader("🎯 Respuesta Sugerida:")
                st.info(respuesta_final)
                st.balloons()
else:
    st.info("Poné la clave.")

if st.button("🗑️ Limpiar Todo"):
    st.rerun()
