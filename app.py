import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Conectado, Fran!")
    
    producto = st.text_input("¿Qué estás ofreciendo?", placeholder="Ej: Remeras, un auto...", key="prod")
    chat_cliente = st.text_area("¿Qué te puso el cliente?", height=120, key="chat")

    if st.button("🚀 GENERAR RESPUESTA GANADORA"):
        if not chat_cliente or not producto:
            st.warning("Completá los campos, che.")
        else:
            txt = chat_cliente.lower()
            st.subheader("🎯 Tu estrategia de cierre:")

            # --- Lógica de Detección Avanzada ---
            
            # 1. OBJECIÓN DE CALIDAD (Lo que te pasó recién)
            if any(x in txt for x in ["mala", "calidad", "trucho", "feo", "malo", "rompe"]):
                res = f"Te entiendo, hoy hay mucha porquería dando vueltas. Pero justamente con estas {producto} lo que buscamos es durabilidad. ¿Qué te hace dudar? Si querés te paso una foto del detalle de las costuras/material."
            
            # 2. OBJECIÓN DE PRECIO
            elif any(x in txt for x in ["caro", "plata", "dinero", "precio", "costo"]):
                res = random.choice([
                    f"El precio es lo que pagás, el valor es lo que te llevás. Estas {producto} te van a durar el triple que una barata. ¿Preferís comprar una hoy o tres el mes que viene?",
                    f"Entiendo, pero pensá que la calidad de este {producto} te ahorra dolores de cabeza. ¿Querés que veamos un descuento por cantidad?"
                ])
            
            # 3. OBJECIÓN DE TIEMPO / VUELTERO
            elif any(x in txt for x in ["pensar", "mañana", "luego", "después", "aviso"]):
                res = f"Dale, no hay drama. Pero ojo que las {producto} están saliendo rápido y no sé si mañana voy a tener el mismo stock o precio. ¿Te reservo un par?"

            # 4. RESPUESTA POR DEFECTO (Más natural)
            else:
                res = f"Te entiendo perfectamente. Decime una cosa, ¿qué es lo que más te interesa de este {producto}? Así te confirmo si es lo que buscás o te recomiendo algo mejor."

            st.write(f"👉 **Copiá esto:** {res}")
            st.balloons()

    if st.button("🗑️ Nueva Consulta"):
        st.rerun()

else:
    st.info("Poné la clave 'pincha2026' a la izquierda.")
