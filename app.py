
import streamlit as st

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🧠")

# Título y Estilo
st.markdown("<h1 style='text-align: center;'>🧠 VentaPsicologica AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Consultor Universal de Cierres</p>", unsafe_allow_html=True)
st.write("---")

# Panel lateral para la clave
st.sidebar.header("🔐 Acceso")
clave = st.sidebar.text_input("Introducí tu Clave Premium", type="password")

if clave == "pincha2026":
    st.success("¡Acceso Total, Fran!")
    
    # Cuadro para que el vendedor ponga qué está vendiendo (Contexto)
    producto = st.text_input("¿Qué estás vendiendo?", placeholder="Ej: Un auto, un curso, una sesión de terapia...")
    
    chat_cliente = st.text_area("Pegá acá lo que te puso el cliente:", height=150)

    if st.button("🚀 ANALIZAR ESTRATEGIA"):
        if not chat_cliente or not producto:
            st.warning("Che, completá qué vendés y qué te dijeron así te puedo ayudar.")
        else:
            texto = chat_cliente.lower()
            st.subheader("🎯 Análisis Psicológico:")
            
            # Lógica de Análisis Universal
            if "caro" in texto or "plata" in texto or "presupuesto" in texto:
                st.info("💡 **Diagnóstico:** Objeción de Precio (Falta de valor percibido)")
                st.write(f"**Estrategia:** No hables de costo, hablá de beneficio. Decile: 'Entiendo que el monto te haga dudar, pero comparado con el beneficio de tener tu {producto} ahora, el costo es mínimo. ¿Querés que veamos una facilidad de pago?'")
            
            elif "pensar" in texto or "mañana" in texto or "después" in texto:
                st.info("💡 **Diagnóstico:** Miedo al compromiso / Procrastinación")
                st.write(f"**Estrategia:** Atacá con escasez. Decile: 'Perfecto, pensalo tranquilo. Pero ojo, que la disponibilidad de {producto} que tengo a este precio es corta y no quiero que te quedes afuera por esperar.'")
            
            elif "competencia" in texto or "otro" in texto or "visto" in texto:
                st.info("💡 **Diagnóstico:** Falta de Autoridad / Comparación")
                st.write(f"**Estrategia:** Diferenciación. Decile: 'Hay muchas opciones de {producto}, pero lo que nos diferencia es [tu ventaja]. Si buscás calidad y no solo precio, esta es tu mejor opción.'")
            
            else:
                st.info("💡 **Diagnóstico:** Interés tibio (Falta un cierre)")
                st.write(f"**Estrategia:** Cierre de Doble Alternativa. Decile: 'Buenísimo que te interese el {producto}. ¿Te parece que coordinemos para hoy a la tarde o preferís mañana a la mañana?'")

    if st.button("Limpiar Pantalla"):
        st.rerun()

else:
    st.error("⚠️ Poné tu clave en el panel de la izquierda.")
