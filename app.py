import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# --- BANCO DE DATOS PSICOLÓGICOS (Aquí está el poder) ---
# Empatía
empatias = ["Te entiendo perfectamente, ", "Comprendo tu punto, ", "Es totalmente lógico lo que planteás, ", "Claro, mucha gente me dice lo mismo al principio, ", "Entiendo tu postura, de hecho es muy común, "]

# Núcleo Psicológico (Objeción: Dinero)
n_precio = [
    "pero recordá que lo barato a la larga sale caro porque no soluciona el problema de fondo.",
    "sin embargo, pensá en cuánto te está costando hoy no tener una solución real.",
    "pero si dividís la inversión por el tiempo que te va a servir, es menos que un café por día.",
    "aunque más que un gasto, esto es la herramienta que va a hacer que el dinero deje de ser un problema.",
    "pero el valor que te llevás supera ampliamente el monto que ves en la pantalla."
]

# Núcleo Psicológico (Objeción: Tiempo)
n_tiempo = [
    "pero el éxito ama la velocidad y mientras más lo pensás, más ventaja le das a la competencia.",
    "sin embargo, las oportunidades no se pierden, solo cambian de manos si no te decidís ahora.",
    "pero pensarlo no va a resolver la situación que tenés hoy, actuar sí lo va a hacer.",
    "aunque el mejor momento para arrancar era ayer, el segundo mejor es ahora mismo.",
    "pero ojo que el cerebro nos engaña con el 'mañana' para que no hagamos los cambios necesarios."
]

# Llamados a la acción (Cierres)
cierres = [
    "¿Querés que te pase los datos y ya te asegurás tu lugar?",
    "¿Te parece bien si cerramos ahora y ya te olvidás de este tema?",
    "¿Qué te falta para que estemos 100% convencidos y arranquemos?",
    "¿Preferís pagar con tarjeta o transferencia así ya te lo reservo?",
    "¿Te mando el link ahora o preferís que lo hablemos en 5 minutos por teléfono?"
]

# --- LÓGICA DE LA APP ---
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    st.success("¡Motor Infinito Activado!")
    chat = st.text_area("¿Qué te puso el cliente?")

    if st.button("🚀 GENERAR RESPUESTA MAESTRA"):
        if not chat:
            st.warning("Pegá el mensaje del cliente.")
        else:
            txt = chat.lower()
            # Seleccionamos las partes
            inicio = random.choice(empatias)
            cierre = random.choice(cierres)
            
            if any(x in txt for x in ["caro", "precio", "plata", "dinero", "presupuesto"]):
                nucleo = random.choice(n_precio)
            elif any(x in txt for x in ["pensar", "luego", "mañana", "después", "tiempo"]):
                nucleo = random.choice(n_tiempo)
            else:
                nucleo = "pero justamente mi idea es ayudarte a que esto sea una solución definitiva para vos."

            # Armamos la respuesta combinada
            respuesta_final = f"{inicio}{nucleo} {cierre}"
            
            st.subheader("🎯 Respuesta Sugerida:")
            st.info(respuesta_final)
            st.balloons()

    if st.button("🗑️ Nueva Consulta"):
        st.rerun()
else:
    st.info("Poné la clave.")
