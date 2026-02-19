import streamlit as st
import random

# Configuración profesional
st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)
st.write("---")

# --- MOTOR DE PSICOLOGÍA APLICADA ---
def generar_estrategia(texto_cliente):
    t = texto_cliente.lower()
    
    # 1. DETECCIÓN DE DESGASTE / USO (Ej: El auto tiene muchos KM)
    if any(x in t for x in ["km", "kilometro", "uso", "viejo", "gastado", "antiguo", "años"]):
        intros = ["Entiendo que el rodaje sea un punto que mires, ", "Es lógico que te fijes en el desgaste, ", "Comprendo tu duda sobre el uso previo, "]
        cuerpos = [
            "pero lo que realmente importa es cómo se mantuvo, no cuánto caminó.",
            "sin embargo, este modelo está rindiendo por encima del promedio por el cuidado que tuvo.",
            "pero recordá que un buen mantenimiento vale más que un número bajo en el tablero."
        ]
        cierres = ["¿Querés que lo revise tu mecánico?", "¿Te gustaría probarlo para sentir la potencia?", "¿Te paso el historial de servicios?"]
    
    # 2. DETECCIÓN DE PRECIO / VALOR
    elif any(x in t for x in ["caro", "plata", "precio", "dinero", "presupuesto", "costo"]):
        intros = ["Entiendo que el presupuesto sea clave, ", "Comprendo que el precio te haga dudar, ", "Es un monto que hay que evaluar bien, "]
        cuerpos = [
            "pero lo barato termina saliendo caro si no te da la seguridad que buscás.",
            "sin embargo, la inversión se justifica con la durabilidad que te garantizo.",
            "pero pensá en cuánto te vas a ahorrar mañana por comprar calidad hoy."
        ]
        cierres = ["¿Querés ver un plan de pagos?", "¿Te sirve si te hago una atención por hoy?", "¿Preferís tarjeta o transferencia?"]
    
    # 3. DETECCIÓN DE POSTERGACIÓN (Lo voy a pensar)
    elif any(x in t for x in ["pensar", "mañana", "luego", "después", "aviso"]):
        intros = ["Dale, consultalo tranquilo, ", "Entiendo que quieras procesarlo, ", "Claro, tomate tu tiempo, "]
        cuerpos = [
            "pero recordá que las oportunidades no se pierden, solo cambian de manos.",
            "sin embargo, las dudas se sacan con la experiencia, no con el tiempo.",
            "pero ojo que el stock se mueve rápido y no quiero que te quedes afuera."
        ]
        cierres = ["¿Qué te falta para estar 100% convencido?", "¿Te lo reservo por un par de horas?", "¿Querés que te saque la última duda ahora?"]
    
    # 4. RESPUESTA POR DEFECTO (Si no detecta categoría)
    else:
        return "Te entiendo perfectamente. Decime, ¿qué es lo que más te genera duda ahora? Así te doy una respuesta exacta para lo que necesitás."

    # Retornamos la combinación única
    return f"{random.choice(intros)}{random.choice(cuerpos)} {random.choice(cierres)}"

# --- INTERFAZ ---
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    st.success("¡Motor Psicológico Activo!")
    
    # El secreto está en este 'key'. Si cambia el texto, Streamlit sabe que debe refrescar.
    chat = st.text_area("¿Qué excusa te puso el cliente?", height=150, placeholder="Ej: Es muy caro / Tiene muchos km...")

    # Usamos un contenedor para que la respuesta se limpie al cambiar el texto
    placeholder = st.empty()

    if st.button("🚀 GENERAR RESPUESTA MAESTRA"):
        if not chat:
            st.warning("Che, pegá primero lo que te puso el cliente.")
        else:
            with st.spinner("Analizando psicología del cliente..."):
                resultado = generar_estrategia(chat)
                placeholder.info(resultado)
                st.balloons()
else:
    st.info("Poné tu clave 'pincha2026'.")

if st.button("🗑️ Limpiar Todo"):
    st.rerun()
