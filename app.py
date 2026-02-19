import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Bien ahí, Fran! Conectado.")
    
    producto = st.text_input("¿Qué estás ofreciendo?", placeholder="Ej: Un departamento, un seguro...")
    chat_cliente = st.text_area("¿Qué excusa te puso el cliente?", height=120)

    if st.button("🚀 GENERAR RESPUESTA GANADORA"):
        if not chat_cliente or not producto:
            st.warning("Che, no te olvides de poner qué vendés y qué te dijeron.")
        else:
            txt = chat_cliente.lower()
            st.subheader("🎯 Tu estrategia de cierre:")

            # --- BANCO DE RESPUESTAS (Mucho más amplio para que no se repita) ---
            opciones = {
                "precio": [
                    f"Entiendo que el precio sea un tema, pero pensá en el retorno: este {producto} se paga solo con los resultados que te va a dar. ¿Preferís ahorrar hoy o ganar mañana?",
                    f"Si el dinero no fuera un problema, ¿el {producto} sería para vos? Te pregunto para entender si es un tema de valor o de presupuesto.",
                    f"Este {producto} no es un gasto, es una inversión en tu tranquilidad/negocio. ¿Querés que veamos un plan de cuotas?"
                ],
                "tiempo": [
                    f"Claro, tomate tu tiempo. Solo te aviso que la prioridad por este {producto} vuela y no quiero que te quedes sin el tuyo por dudar. ¿Te reservo el lugar?",
                    f"El mejor momento para tener tu {producto} era ayer, el segundo mejor es hoy. ¿Qué es lo que te hace dudar para arrancar ya?",
                    f"Te entiendo, pero recordá que el precio del {producto} puede subir si esperamos mucho. ¿Querés aprovechar la oferta de hoy?"
                ],
                "duda": [
                    f"Totalmente de acuerdo. ¿Qué información te falta para que estés 100% convencido de que este {producto} es para vos?",
                    f"¿Hay algo específico que no te cierre? Porque el {producto} está diseñado justamente para solucionar lo que me contabas.",
                    f"Hagamos algo: probá el {producto} y si no es lo que esperabas, lo charlamos. ¿Te parece bien?"
                ]
            }

            # Lógica de selección más fina
            if any(x in txt for x in ["caro", "plata", "dinero", "precio", "pagar", "costo"]):
                res = random.choice(opciones["precio"])
            elif any(x in txt for x in ["pensar", "mañana", "luego", "después", "tiempo", "semana"]):
                res = random.choice(opciones["tiempo"])
            else:
                res = random.choice(opciones["duda"])

            st.write(f"👉 **Copiá esto:** {res}")
            st.balloons() # ¡Para festejar el cierre!

    if st.button("🗑️ Nueva Consulta (Limpiar)"):
        st.rerun()

else:
    st.info("Poné la clave 'pincha2026' a la izquierda para activar la IA.")
