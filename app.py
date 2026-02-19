import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Conectado, Fran! Vamos a domar a ese cliente.")
    
    # Usamos plural para que las frases queden naturales (ej: Las remeras)
    producto = st.text_input("¿Qué estás ofreciendo?", placeholder="Ej: Remeras, zapatillas...", key="prod")
    chat_cliente = st.text_area("¿Qué excusa te puso el cliente?", height=120, key="chat")

    if st.button("🚀 GENERAR RESPUESTA GANADORA"):
        if not chat_cliente or not producto:
            st.warning("Che, no te olvides de poner qué vendés y qué te dijeron.")
        else:
            txt = chat_cliente.lower()
            st.subheader("🎯 Tu estrategia de cierre:")

            # --- LÓGICA DE DETECCIÓN REAL ---
            
            # 1. SI TE ATACAN LA CALIDAD (Lo que falló recién)
            if any(x in txt for x in ["mala", "calidad", "trucho", "feo", "malo", "rompe", "tela"]):
                res = f"Mirá, te entiendo porque hoy hay mucha porquería dando vueltas. Pero justamente el punto fuerte de estas {producto} es que la tela no se deforma ni pierde color. Si querés te paso un video del detalle para que veas que no te miento. ¿Te sirve?"
            
            # 2. SI DICEN QUE ES CARO
            elif any(x in txt for x in ["caro", "plata", "dinero", "precio", "costo", "carisimo"]):
                res = f"Entiendo que el precio sea un punto a ver. Pero pensá que estas {producto} te van a durar el triple que una barata de esas que se rompen al primer uso. Al final, lo barato sale caro, ¿no? ¿Querés que te pase el plan de pagos?"
            
            # 3. SI DICEN QUE LO TIENEN QUE PENSAR
            elif any(x in txt for x in ["pensar", "mañana", "luego", "después", "aviso", "consulto"]):
                res = f"Dale, no hay drama, consultalo tranquilo. Pero te aviso que las {producto} están saliendo rápido y me quedan pocas en stock. Si te decidís después y no tengo, no me mates jajaja. ¿Querés que te guarde una por un par de horas?"

            # 4. RESPUESTA POR DEFECTO (Si no detecta nada de lo anterior)
            else:
                res = f"Te entiendo perfectamente. Decime una cosa, ¿qué es lo que más te hace dudar? Porque mi idea es que te lleves unas {producto} que realmente te gusten y te sirvan. ¡Contame y le buscamos la vuelta!"

            st.write(f"👉 **Copiá esto:** {res}")
            st.balloons()

    if st.button("🗑️ Nueva Consulta (Limpiar)"):
        st.rerun()

else:
    st.info("Poné la clave 'pincha2026' a la izquierda para activar la IA.")
