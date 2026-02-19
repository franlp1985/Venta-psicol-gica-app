import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)

# --- BANCO DE DATOS ---
empatias = ["Te entiendo perfectamente, ", "Comprendo lo que decís, ", "Es una duda lógica, ", "Claro, hoy en día hay que ser cuidadoso, ", "Entiendo tu punto de vista, ", "Es totalmente comprensible tu postura, "]

n_calidad = [
    "pero lo que no se ve a simple vista es la durabilidad del material que usamos.",
    "sin embargo, la terminación está pensada para que no pierda la forma con el uso.",
    "pero mi garantía es que esto te va a durar el doble que cualquier opción barata.",
    "aunque parezca sencillo, el proceso de fabricación resiste el uso intenso.",
    "pero te invito a que lo pruebes; si la calidad no es la esperada, nos hacemos cargo.",
    "pero fijate que el refuerzo de las costuras es lo que hace la diferencia real."
]

n_precio = [
    "pero el precio es lo que pagás hoy y el valor es lo que te llevás a largo plazo.",
    "aunque parezca una inversión alta, pensá en lo que ahorrás al no tener que reponerlo pronto.",
    "pero si buscás algo que solucione el problema, la calidad tiene un costo justificado.",
    "sin embargo, tenemos opciones para que el monto no sea un obstáculo para vos.",
    "pero lo barato termina saliendo caro cuando tenés que comprarlo dos veces.",
    "pero recordá que estás pagando por un resultado, no solo por un objeto."
]

cierres = [
    "¿Querés que te pase un video del detalle para que te quedes tranquilo?",
    "¿Te gustaría probar uno y comprobarlo por vos mismo?",
    "¿Te parece si coordinamos el envío y lo ves en persona?",
    "¿Qué es lo que más te hace dudar para que arranquemos?",
    "¿Te sirve si te hago una atención especial para que lo pruebes hoy?",
    "¿Preferís que te mande fotos reales de otros clientes usándolo?"
]

# --- INICIALIZAR MEMORIA ---
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# --- ACCESO ---
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    st.success("¡Motor Activo!")
    chat = st.text_area("¿Qué te puso el cliente?", key="input_chat")

    # Al cambiar el 'key' con un contador, forzamos a Streamlit a no repetir
    if st.button("🚀 GENERAR RESPUESTA ÚNICA"):
        if not chat:
            st.warning("Pegá el mensaje del cliente.")
        else:
            st.session_state.contador += 1 # Esto cambia el estado interno en cada clic
            
            txt = chat.lower()
            
            # Selección forzada al azar
            inicio = random.choice(empatias)
            cierre = random.choice(cierres)
            
            if any(x in txt for x in ["mala", "calidad", "trucho", "tela", "material", "malo"]):
                nucleo = random.choice(n_calidad)
            elif any(x in txt for x in ["caro", "plata", "dinero", "precio", "costo"]):
                nucleo = random.choice(n_precio)
            else:
                nucleo = "pero justamente mi objetivo es que esto sea una solución para vos."

            respuesta_final = f"{inicio}{nucleo} {cierre}"
            
            # Mostramos un ID de respuesta para que veas que cambia
            st.subheader(f"🎯 Respuesta sugerida N°{random.randint(100, 999)}:")
            st.info(respuesta_final)
            st.balloons()
else:
    st.info("Poné la clave.")

if st.button("🗑️ Limpiar Pantalla"):
    st.rerun()
