import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)

# --- LAS RESPUESTAS (PSICOLOGÍA PURA) ---
def obtener_respuesta(mensaje):
    t = mensaje.lower()
    
    # 1. CASO CALIDAD (Remeras, telas, material)
    if any(x in t for x in ["calidad", "mala", "tela", "trucho", "material", "rompe", "feo"]):
        return random.choice([
            "Entiendo que dudes de la calidad hoy en día. Pero la tela de estas prendas está probada para no deformarse. ¿Querés que te pase un video del detalle?",
            "Es lógico desconfiar si no tocás el material. Mi garantía es que esto dura el triple que lo barato. ¿Te sirve si te mando fotos de las costuras?",
            "Comprendo tu punto. Lo que no se ve es el refuerzo que tiene el material. ¿Qué es lo que más te hace dudar de la calidad?"
        ])
    
    # 2. CASO DESGASTE (Autos, KM, años)
    elif any(x in t for x in ["km", "kilometro", "kilómetro", "motor", "uso", "años", "rodado"]):
        return random.choice([
            "Entiendo que los kilómetros te hagan ruido, pero lo que importa es el mantenimiento real. ¿Querés que lo vea tu mecánico de confianza?",
            "Es lógico fijarse en el uso, pero este motor rinde el doble por el cuidado que tuvo. ¿Te gustaría probarlo y sentir cómo responde?",
            "Comprendo la duda, pero un buen mantenimiento vale más que un número bajo en el tablero. ¿Te paso el historial de servicios?"
        ])
    
    # 3. CASO PRECIO
    elif any(x in t for x in ["caro", "precio", "plata", "dinero", "presupuesto"]):
        return random.choice([
            "Entiendo que el precio sea un punto a evaluar, pero lo barato sale caro si no soluciona el problema. ¿Vemos un plan de pagos?",
            "El valor se recuerda mucho después de que el precio se olvida. ¿Te sirve si te hago una atención especial por hoy?",
            "Si el dinero no fuera el problema... ¿lo llevarías ahora mismo? Te pregunto para ver cómo ayudarte con el pago."
        ])
    
    # 4. CASO PENSAR / POSTERGAR
    elif any(x in t for x in ["pensar", "mañana", "luego", "después", "aviso"]):
        return random.choice([
            "Dale, consultalo tranquilo, pero recordá que las oportunidades no se pierden, solo cambian de manos. ¿Te lo reservo por 2 horas?",
            "Entiendo que quieras procesarlo, pero las dudas se sacan con la experiencia, no con el tiempo. ¿Qué te falta para decidirte?",
            "Claro, tomate tu tiempo, pero ojo que el stock vuela y no quiero que te quedes afuera. ¿Querés sacarte la última duda ahora?"
        ])
    
    # 5. GENERAL
    else:
        return "Te entiendo perfectamente. Decime, ¿qué es lo que más te genera duda ahora? Así le buscamos la vuelta juntos."

# --- INTERFAZ ---
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    chat = st.text_area("¿Qué te dijo el cliente?", height=150)

    if st.button("🚀 GENERAR RESPUESTA"):
        if chat:
            resultado = obtener_respuesta(chat)
            st.write("---")
            st.subheader("🎯 Estrategia Sugerida:")
            st.info(resultado)
            st.balloons()
        else:
            st.warning("Pegá el mensaje del cliente primero.")
else:
    st.info("Poné la clave 'pincha2026' para activar el sistema.")
