import streamlit as st
import random
import time

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

# --- BANCO DE RESPUESTAS POR PROBLEMÁTICA REAL ---
# Aquí separamos bien los tantos para que no se mezclen
biblioteca = {
    "calidad_producto": [
        "Entiendo que dudes de la calidad, hoy hay mucha porquería dando vueltas. Pero la tela de estas prendas está probada para no deformarse. ¿Querés que te pase un video del detalle?",
        "Es lógico que desconfíes si no tocás el material. Pero mi garantía es que esto dura el triple que lo barato. ¿Te sirve si te mando fotos de las costuras?",
        "Comprendo tu punto. Lo que no se ve a simple vista es el refuerzo que tiene el material. ¿Qué es lo que más te hace dudar de la calidad?"
    ],
    "desgaste_tecnico": [
        "Entiendo que los kilómetros te hagan ruido, pero lo que importa es el mantenimiento real. ¿Querés que lo vea tu mecánico de confianza?",
        "Es lógico fijarse en el uso, pero este motor rinde el doble por el cuidado que tuvo. ¿Te gustaría probarlo y sentir cómo responde?",
        "Comprendo la duda, pero un buen mantenimiento vale más que un número bajo en el tablero. ¿Te paso el historial de servicios completo?"
    ],
    "precio": [
        "Entiendo que el precio sea un punto a evaluar, pero lo barato sale caro si no soluciona el problema. ¿Vemos un plan de pagos?",
        "El valor se recuerda mucho después de que el precio se olvida. ¿Te sirve si te hago una atención especial por hoy?",
        "Si el dinero no fuera el problema... ¿lo llevarías ahora mismo? Te pregunto para ver cómo ayudarte con el pago."
    ],
    "postergacion": [
        "Dale, consultalo tranquilo, pero recordá que las oportunidades no se pierden, solo cambian de manos. ¿Te lo reservo por 2 horas?",
        "Entiendo que quieras procesarlo, pero las dudas se sacan con la experiencia, no con el tiempo. ¿Qué te falta para decidirte?",
        "Claro, tomate tu tiempo, pero ojo que el stock vuela y no quiero que te quedes afuera. ¿Querés sacarte la última duda ahora?"
    ]
}

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)

st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    # El secreto para que no se cuelgue es que el texto se limpie internamente
    chat = st.text_area("¿Qué te dijo el cliente?", height=150, key="input_usuario")

    # Botón con "disparador" para que no se guarde en memoria
    if st.button("🚀 GENERAR RESPUESTA", key=f"btn_{time.time()}"):
        if not chat:
            st.warning("Che, Fran, pegá el mensaje primero.")
        else:
            t = chat.lower()
            
            # --- LÓGICA DE DETECCIÓN ESTRICTA ---
            # 1. Detectar Calidad (Remeras, tela, etc.)
            if any(x in t for x in ["calidad", "mala", "tela", "trucho", "material", "rompe", "prenda"]):
                categoria = "calidad_producto"
            
            # 2. Detectar Desgaste (Autos, KM, etc.)
            elif any(x in t for x in ["km", "kilómetro", "kilometro", "motor", "uso", "años", "rodado"]):
                categoria = "desgaste_tecnico"
            
            # 3. Detectar Precio
            elif any(x in t for x in ["caro", "precio", "plata", "dinero", "presupuesto", "carisimo"]):
                categoria = "precio"
            
            # 4. Detectar Postergación
            elif any(x in t for x in ["pensar", "mañana", "luego", "después", "aviso"]):
                categoria = "postergacion"
            
            # 5. General
            else:
                categoria = "postergacion" # Por defecto usamos cierre de duda

            # Seleccionamos la respuesta de la bolsa correcta
            respuesta = random.choice(biblioteca[categoria])
            
            st.write("---")
            st.subheader("🎯 Estrategia Sugerida:")
            st.info(respuesta)
            st.balloons()
else:
    st.info("Poné la clave 'pincha2026'.")

if st.button("🗑️ Resetear Cerebro"):
    st.rerun()
