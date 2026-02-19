import streamlit as st

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)
st.write("---")

# Panel lateral
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Introducí tu Clave Premium", type="password")

if clave == "pincha2026":
    st.success("¡Acceso Total, Fran!")
    
    producto = st.text_input("¿Qué estás vendiendo?", placeholder="Ej: Un auto, una asesoría...")
    chat_cliente = st.text_area("Pegá acá el chat del cliente:", height=150)

    if st.button("🚀 GENERAR ESTRATEGIA ÚNICA"):
        if not chat_cliente or not producto:
            st.warning("Che, no te olvides de completar los campos.")
        else:
            st.subheader("🎯 Respuesta Sugerida:")
            
            # --- Lógica de VentaPsicologica ---
            texto = chat_cliente.lower()
            
            # Análisis de objeciones comunes con respuestas más variadas
            if any(x in texto for x in ["caro", "plata", "dinero", "precio"]):
                st.info("💡 **Técnica:** Reencuadre de Inversión")
                respuesta = f"Entiendo que el precio sea un punto a evaluar. Pero pensá en el costo de oportunidad de no tener tu {producto} hoy. ¿Te sirve si lo financiamos o buscamos una alternativa?"
            
            elif any(x in texto for x in ["pensar", "mañana", "luego", "después"]):
                st.info("💡 **Técnica:** Gancho de Urgencia")
                respuesta = f"Claro, tomate tu tiempo. Solo te aviso que tengo otros interesados en este {producto} y no te quiero fallar si se reserva. ¿Hay algo puntual que te haga dudar?"
                
            elif any(x in texto for x in ["otro", "competencia", "visto"]):
                st.info("💡 **Técnica:** Diferenciación de Autoridad")
                respuesta = f"Es lógico que compares. Pero lo que te llevás con este {producto} no lo vas a encontrar en otro lado por [mencionar tu ventaja]. ¿Querés que te cuente por qué mis clientes nos eligen?"
            
            else:
                st.info("💡 **Técnica:** Cierre de Conclusión")
                respuesta = f"¡Excelente! Veo que el {producto} es justo lo que buscás. Para avanzar, ¿te queda mejor que te mande los datos ahora o preferís que te llame en 5 minutos?"

            st.write(f"👉 **Copiá y pegá esto:** {respuesta}")

    if st.button("🗑️ Limpiar y Nueva Consulta"):
        st.rerun()

else:
    st.error("⚠️ Poné tu clave 'pincha2026' a la izquierda.")
