import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica Pro", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Conectado, Fran! Modo Psicología Pura activado.")
    
    # YA NO ESTÁ EL CUADRO DE PRODUCTO
    chat_cliente = st.text_area("¿Qué excusa te puso el cliente?", height=150, key="chat", placeholder="Ej: Es muy caro, lo tengo que pensar...")

    if st.button("🚀 GENERAR RESPUESTA GANADORA"):
        if not chat_cliente:
            st.warning("Che, pegá primero lo que te puso el cliente.")
        else:
            txt = chat_cliente.lower()
            st.subheader("🎯 Estrategia Psicológica:")

            # --- BANCO DE RESPUESTAS DINÁMICAS (Sin mencionar el producto) ---
            
            # 1. CALIDAD / DESCONFIANZA
            if any(x in txt for x in ["mala", "calidad", "trucho", "feo", "malo", "rompe", "tela"]):
                res = random.choice([
                    "Te entiendo, hoy hay mucha porquería dando vueltas. Pero justamente mi garantía es la durabilidad. Si querés te paso pruebas de clientes que ya lo usan hace tiempo. ¿Te sirve?",
                    "Entiendo tu duda. Lo barato suele salir caro, por eso yo me enfoco en que esto te dure y no tengas que volver a comprarlo en dos meses. ¿Qué es lo que más te hace dudar?",
                    "Es lógico que desconfíes si no conocés la marca. Pero te aseguro que el material es de primera. ¿Querés que te mande un video detallado para que veas la calidad real?"
                ])
            
            # 2. PRECIO / PLATA
            elif any(x in txt for x in ["caro", "plata", "dinero", "precio", "costo", "carisimo"]):
                res = random.choice([
                    "Entiendo que el monto sea un punto a evaluar. Pero pensalo como una inversión: ¿cuánto te va a ahorrar esto a largo plazo? ¿Querés que veamos un plan de pagos?",
                    "Si el dinero no fuera el problema... ¿lo llevarías ahora mismo? Te pregunto para saber si realmente es lo que necesitás o si tenés alguna otra duda.",
                    "Entiendo perfectamente. Mi idea no es que gastes, sino que soluciones esto de una vez. ¿Te sirve si te hago una atención especial por ser la primera vez?"
                ])
            
            # 3. TIEMPO / VUELTERO
            elif any(x in txt for x in ["pensar", "mañana", "luego", "después", "aviso", "consulto"]):
                res = random.choice([
                    "Dale, consultalo tranquilo. Pero te aviso que el stock se mueve rápido y no te quiero fallar si después no tengo. ¿Te reservo el cupo por un par de horas?",
                    "Te entiendo. La mayoría de los que hoy están súper conformes al principio también lo pensaron. ¿Qué es lo que te falta para estar 100% convencido?",
                    "Dale, no hay drama. Pero ojo que la oferta actual es solo por tiempo limitado. Si te decidís después y cambió el precio, no me mates jajaja. ¿Te guardo el beneficio?"
                ])

            # 4. RESPUESTA POR DEFECTO
            else:
                res = "Te entiendo perfectamente. Decime una cosa, ¿qué es lo que más te hace dudar ahora mismo? Mi idea es que te lleves algo que realmente te sirva. ¡Contame y le buscamos la vuelta!"

            st.info(res)
            st.balloons()

    if st.button("🗑️ Nueva Consulta"):
        st.rerun()

else:
    st.info("Poné la clave 'pincha2026' a la izquierda.")
