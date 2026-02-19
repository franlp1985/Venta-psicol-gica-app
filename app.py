import streamlit as st
import random

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Introducí tu Clave Premium", type="password")

if clave == "pincha2026":
    st.success("¡Acceso Total, Fran!")
    
    # Usamos "key" para que Streamlit sepa que los campos deben resetearse
    producto = st.text_input("¿Qué estás vendiendo?", placeholder="Ej: Zapatillas, un auto, asesoría...", key="prod")
    chat_cliente = st.text_area("Pegá acá el chat del cliente:", height=150, key="chat")

    if st.button("🚀 ANALIZAR ESTRATEGIA"):
        if not chat_cliente or not producto:
            st.warning("Completá los dos campos para que pueda ayudarte, che.")
        else:
            texto = chat_cliente.lower()
            st.subheader("🎯 Análisis y Respuesta:")
            
            # --- Respuestas Dinámicas para que no sea siempre lo mismo ---
            res_caro = [
                f"Entiendo que el precio asuste, pero pensá en el beneficio de tener tu {producto} ahora mismo. ¿Es un gasto o una inversión para vos?",
                f"Si lo comparás con no tener el {producto}, ¿qué te sale más caro? Te puedo ofrecer una facilidad de pago si te sirve.",
                f"El valor de este {producto} no está en el precio, sino en la solución que te da. ¿Querés que te explique por qué vale cada peso?"
            ]
            
            res_pensar = [
                f"Dale, pensalo tranquilo. Pero te aviso que este {producto} vuela y no quiero que te quedes sin el tuyo por dudar. ¿Te reservo uno?",
                f"Claro, consultalo con la almohada. Solo recordá que la oferta actual por el {producto} termina pronto. ¿Hay algo que te genere duda?",
                f"Te entiendo. La mayoría de mis clientes que hoy disfrutan su {producto} al principio también lo pensaron. ¿Qué te falta para decidirte?"
            ]

            # Lógica mejorada
            if any(x in texto for x in ["caro", "plata", "dinero", "precio", "presupuesto"]):
                st.info("💡 **Diagnóstico:** Objeción de Precio")
                st.write(f"**Estrategia:** {random.choice(res_caro)}")
            
            elif any(x in texto for x in ["pensar", "mañana", "después", "luego"]):
                st.info("💡 **Diagnóstico:** Procrastinación")
                st.write(f"**Estrategia:** {random.choice(res_pensar)}")
            
            else:
                st.info("💡 **Diagnóstico:** Cierre de Alternativa")
                st.write(f"**Estrategia:** '¡Buenísimo! ¿Preferís que coordinemos el envío de tu {producto} para hoy o te queda mejor mañana?'")

    # Botón de Limpiar mejorado (borra la memoria de la sesión)
    if st.button("Limpiar Pantalla"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

else:
    st.error("⚠️ Poné tu clave 'pincha2026' a la izquierda.")
