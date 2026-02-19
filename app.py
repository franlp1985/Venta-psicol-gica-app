import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")
st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)

# --- BANCO DE DATOS (PSICOLOGÍA PURA) ---
empatias = ["Te entiendo perfectamente, ", "Comprendo que quieras estar seguro, ", "Es una decisión importante, ", "Claro, mucha gente me dice lo mismo, ", "Entiendo tu postura, "]

# 1. CATEGORÍA: LO VOY A PENSAR (Miedo a decidir)
n_pensar = [
    "pero el éxito ama la velocidad y las oportunidades no esperan a que estemos listos.",
    "sin embargo, a veces 'pensarlo' es solo una forma de postergar la solución que necesitás hoy.",
    "pero ojo que el cerebro nos engaña para no salir de la zona de confort. ¿Qué es lo que realmente te frena?",
    "aunque pensarlo no va a resolver el problema, tomar acción ahora sí lo va a hacer.",
    "pero mientras lo pensás, el stock sigue bajando y no te quiero fallar si después no tengo."
]

# 2. CATEGORÍA: PRECIO
n_precio = [
    "pero el precio es lo que pagás hoy, y el valor es lo que disfrutás todos los días.",
    "sin embargo, lo barato suele salir caro porque no soluciona el problema de fondo.",
    "pero si el dinero no fuera el problema... ¿arrancaríamos ahora mismo?",
    "aunque parezca una inversión, se paga sola con los resultados que te va a dar.",
    "pero recordá que estás invirtiendo en tu tranquilidad, no gastando plata."
]

# 3. CATEGORÍA: CALIDAD
n_calidad = [
    "pero justamente mi garantía es que el material es de primera y no se deforma.",
    "sin embargo, la calidad se nota en los detalles que no se ven a simple vista.",
    "pero te aseguro que esto dura el triple que cualquier opción más barata.",
    "aunque parezca igual a otros, la durabilidad de este producto es lo que nos diferencia.",
    "pero te invito a que lo pruebes; si no es la calidad que esperás, nos hacemos cargo."
]

cierres = [
    "¿Qué te falta para que estemos 100% convencidos y arranquemos?",
    "¿Querés que te reserve uno por un par de horas así no perdés el lugar?",
    "¿Preferís que te pase los datos de pago ahora o mañana temprano?",
    "¿Te sirve si te hago una atención especial para que te decidas hoy mismo?",
    "¿Te parece si coordinamos ahora y ya te olvidás de este tema?"
]

# --- LÓGICA ---
if 'contador' not in st.session_state: st.session_state.contador = 0

st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Clave", type="password")

if clave == "pincha2026":
    st.success("¡Motor Activo, Fran!")
    chat = st.text_area("¿Qué te puso el cliente?", key="input_chat")

    if st.button("🚀 GENERAR RESPUESTA GANADORA"):
        if not chat:
            st.warning("Pegá el mensaje del cliente.")
        else:
            st.session_state.contador += 1
            txt = chat.lower()
            inicio = random.choice(empatias)
            cierre = random.choice(cierres)
            
            # DETECCIÓN DE CATEGORÍA
            if any(x in txt for x in ["pensar", "después", "mañana", "luego", "tiempo", "aviso"]):
                nucleo = random.choice(n_pensar)
            elif any(x in txt for x in ["caro", "plata", "precio", "dinero", "presupuesto"]):
                nucleo = random.choice(n_precio)
            elif any(x in txt for x in ["mala", "calidad", "trucho", "malo", "material"]):
                nucleo = random.choice(n_calidad)
            else:
                nucleo = "pero justamente mi idea es ayudarte a que tomes la mejor decisión para vos hoy mismo."

            res_final = f"{inicio}{nucleo} {cierre}"
            st.subheader(f"🎯 Respuesta sugerida N°{random.randint(100, 999)}:")
            st.info(res_final)
            st.balloons()
else:
    st.info("Poné la clave.")
