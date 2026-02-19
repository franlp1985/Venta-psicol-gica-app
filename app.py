import streamlit as st
import PyPDF2
import random

st.set_page_config(page_title="VentaPsicologica AI", page_icon="💰")

# Diseño más profesional y limpio
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>💰 VentaPsicologica AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>Tu Mentor de Cierre en Tiempo Real</b></p>", unsafe_allow_html=True)
st.write("---")

# Función para extraer sabiduría del curso sin que el usuario lo lea
def extraer_tecnica(tipo_objecion):
    try:
        with open("curso.pdf", "rb") as f:
            reader = PyPDF2.PdfReader(f)
            # Buscamos en páginas clave según la objeción
            texto_base = ""
            for page in reader.pages[20:100]: # Buscamos en el núcleo del curso
                contenido = page.extract_text()
                if tipo_objecion.lower() in contenido.lower():
                    texto_base = contenido[:300]
                    break
            return texto_base
    except:
        return None

# Acceso
st.sidebar.header("🔐 Acceso Premium")
clave = st.sidebar.text_input("Clave de Usuario", type="password")

if clave == "pincha2026":
    st.success("¡Bienvenido al Cerrador Universal!")
    
    # Campo abierto para cualquier vendedor
    chat_cliente = st.text_area("¿Qué excusa te puso el cliente?", height=150, placeholder="Ej: 'Me parece caro', 'Lo tengo que pensar', 'No confío'...")

    if st.button("🚀 OBTENER RESPUESTA MAESTRA"):
        if not chat_cliente:
            st.warning("Pegá el mensaje del cliente para analizarlo.")
        else:
            txt = chat_cliente.lower()
            
            # --- LÓGICA DE PSICOLOGÍA APLICADA ---
            if any(x in txt for x in ["caro", "precio", "plata", "dinero", "presupuesto"]):
                categoria = "Precio"
                tecnica = "Reencuadre de Valor"
                respuestas = [
                    "Entiendo perfectamente que el presupuesto sea un tema. Pero decime, ¿estás evaluando el costo hoy o el beneficio que te va a dar a largo plazo?",
                    "Si el dinero no fuera el problema, ¿sentís que este producto es lo que necesitás? Para ver si te puedo ayudar con una atención especial.",
                    "Entiendo. Lo barato suele salir caro porque no soluciona el problema de fondo. ¿Querés que veamos cómo esto se paga solo con los resultados?"
                ]
            
            elif any(x in txt for x in ["pensar", "después", "luego", "mañana", "aviso"]):
                categoria = "Postergación"
                tecnica = "Escasez y Miedo a la Pérdida"
                respuestas = [
                    "Dale, consultalo tranquilo. Solo te aviso que el stock/cupo es limitado y no quiero que te quedes afuera por dudar. ¿Te reservo el lugar un par de horas?",
                    "Totalmente. Pero recordá que el problema que tenés hoy no se va a pensar solo. ¿Qué es lo que te falta para estar 100% convencido y arrancar?",
                    "Claro. Pero a veces 'pensarlo' es solo una forma de no decidir. ¿Qué te parece si resolvemos la duda principal ahora?"
                ]
                
            elif any(x in txt for x in ["mala", "calidad", "trucho", "malo", "feo", "rompe"]):
                categoria = "Desconfianza"
                tecnica = "Prueba Social y Autoridad"
                respuestas = [
                    "Te entiendo, hay mucha desconfianza hoy. Pero justamente mi fuerte es la durabilidad. ¿Te sirve si te paso testimonios de otros que pensaban igual?",
                    "Es lógico dudar si no nos conocés. Por eso te doy garantía total. Si no es la calidad que esperás, nos hacemos cargo. ¿Te parece justo?",
                    "La calidad se nota en el uso. Yo no arriesgaría mi reputación con algo malo. ¿Querés ver un video del detalle técnico?"
                ]
            
            else:
                categoria = "Cierre"
                tecnica = "Doble Alternativa"
                respuestas = [
                    "¡Excelente punto! Para avanzar y que no se te pase la oportunidad, ¿preferís que coordinemos para hoy o para mañana?",
                    "Te entiendo. Decime, ¿qué es lo que más te gustó de lo que vimos? Así cerramos los detalles ahora mismo.",
                    "Buenísimo. Para arrancar ya, ¿te queda más cómodo pagar con tarjeta o transferencia?"
                ]

            # Mostrar el resultado al vendedor
            st.subheader(f"🎯 Técnica sugerida: {tecnica}")
            st.write(f"👉 **Respuesta para copiar:** {random.choice(respuestas)}")
            
            # El "Bonus" del curso de Fran (invisible para el cliente del vendedor)
            sabiduria = extraer_tecnica(categoria)
            if sabiduria:
                with st.expander("💡 ¿Por qué funciona esto? (Saber más)"):
                    st.write(f"Basado en la psicología de ventas de tu curso: {sabiduria}...")

    if st.button("🗑️ Nueva Consulta"):
        st.rerun()

else:
    st.info("Ingresá tu clave de suscriptor.")
