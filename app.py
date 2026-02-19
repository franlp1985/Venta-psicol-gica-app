import streamlit as st
import random
import time

# Configuración de página
st.set_page_config(page_title="VentaPsicologica AI v3.0", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica Pro</h1>", unsafe_allow_html=True)
st.write("---")

# --- MOTOR DE INTELIGENCIA BASADO EN EL CURSO ---
# Estas listas tienen que ser grandes para que las combinaciones sean miles
expert_tips = {
    "precio": {
        "intro": ["Entiendo que el precio sea un punto a evaluar, ", "Comprendo el tema del presupuesto, ", "Es lógico cuidar la inversión, ", "Claro, el valor monetario es importante, "],
        "cuerpo": [
            "pero lo barato sale caro si no soluciona el problema de raíz.",
            "sin embargo, la pregunta es: ¿cuánto te cuesta hoy NO tener este resultado?",
            "pero recordá que la calidad se recuerda mucho después de que el precio se olvida.",
            "aunque parezca un número alto, si lo dividís por el tiempo de uso es ínfimo.",
            "pero pensá en esto como una herramienta de ahorro a futuro, no como un gasto."
        ],
        "cierre": ["¿Querés que veamos un plan de pagos?", "¿Preferís tarjeta o transferencia?", "¿Te sirve si te hago una atención por hoy?"]
    },
    "pensar": {
        "intro": ["Dale, consultalo tranquilo, ", "Entiendo que quieras procesarlo, ", "Claro, es una decisión que hay que tomar seguro, ", "Perfecto, tomate tu tiempo, "],
        "cuerpo": [
            "pero el éxito ama la velocidad y las oportunidades cambian de manos rápido.",
            "sin embargo, a veces 'pensarlo' es solo el miedo a dar el salto al éxito.",
            "pero ojo que mientras lo pensás, el problema que tenés hoy sigue creciendo.",
            "aunque recordá que el stock es limitado y no quiero que te quedes afuera.",
            "pero la duda es el enemigo número uno de los resultados."
        ],
        "cierre": ["¿Qué te falta para estar 100% convencido?", "¿Te reservo el cupo por 2 horas?", "¿Querés que te llame y nos sacamos las dudas?"]
    },
    "calidad": {
        "intro": ["Te entiendo, hoy hay mucha desconfianza, ", "Es normal dudar de la calidad hoy en día, ", "Comprendo que busques algo duradero, ", "Es lógico que quieras lo mejor, "],
        "cuerpo": [
            "pero justamente mi garantía es que los materiales son de alta gama.",
            "sin embargo, la terminación técnica es lo que nos diferencia de la competencia.",
            "pero te aseguro que este producto está diseñado para uso intensivo.",
            "aunque si ves el detalle de las costuras/material te vas a dar cuenta solo.",
            "pero prefiero explicar el precio una vez que pedir disculpas por la calidad siempre."
        ],
        "cierre": ["¿Querés un video del detalle?", "¿Te mando fotos de otros clientes?", "¿Preferís pasar a verlo o te mando una muestra?"]
    }
}

# --- LOGICA DE LA APP ---
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Cerebro de 170 páginas cargado!")
    
    # El cuadro de texto para el cliente
    chat_cliente = st.text_area("¿Qué excusa te puso el cliente?", height=150, placeholder="Ej: Es muy caro / Lo voy a pensar / Se ve malo...")

    if st.button("🚀 GENERAR RESPUESTA ÚNICA"):
        if not chat_cliente:
            st.warning("Che, pegá primero lo que te puso el cliente.")
        else:
            # RESET DE AZAR CADA VEZ QUE APRETA EL BOTON
            random.seed(time.time())
            txt = chat_cliente.lower()
            
            # Clasificación inteligente de la problemática
            cat = "general"
            if any(x in txt for x in ["caro", "plata", "precio", "dinero", "presupuesto", "costo", "carisimo"]):
                cat = "precio"
            elif any(x in txt for x in ["pensar", "mañana", "luego", "después", "aviso", "consultar", "viendo"]):
                cat = "pensar"
            elif any(x in txt for x in ["mala", "calidad", "malo", "feo", "trucho", "rompe", "material", "tela"]):
                cat = "calidad"

            if cat in expert_tips:
                # Armamos la respuesta combinando piezas al azar
                opciones = expert_tips[cat]
                res = f"{random.choice(opciones['intro'])}{random.choice(opciones['cuerpo'])} {random.choice(opciones['cierre'])}"
            else:
                res = "Te entiendo perfectamente. Decime, ¿qué es lo que más te hace dudar ahora? Mi idea es darte una solución que te sirva de verdad. ¿Le buscamos la vuelta?"

            # Mostrar resultado con estilo
            st.subheader("🎯 Respuesta sugerida:")
            st.info(res)
            # Un numerito para que Fran vea que la respuesta cambió
            st.caption(f"ID de Estrategia: {random.randint(1000, 9999)}")
            st.balloons()

    if st.button("🗑️ Limpiar y Nueva Consulta"):
        st.rerun()

else:
    st.info("Poné tu clave 'pincha2026' a la izquierda.")
