import streamlit as st
import PyPDF2
import random

st.set_page_config(page_title="VentaPsicologica AI", page_icon="🔥")

st.markdown("<h1 style='text-align: center;'>🔥 VentaPsicologica: El Cerrador</h1>", unsafe_allow_html=True)
st.write("---")

# Función para buscar en el PDF
def buscar_en_curso(palabra_clave):
    try:
        # ACA: Si tu archivo no tiene .pdf, sacáselo en la siguiente línea
        with open("curso.pdf", "rb") as f:
            reader = PyPDF2.PdfReader(f)
            texto_encontrado = ""
            # Buscamos en las 170 páginas de forma inteligente
            for page in reader.pages:
                contenido = page.extract_text()
                if palabra_clave.lower() in contenido.lower():
                    # Agarramos un pedacito del texto para que sirva de base
                    texto_encontrado = contenido[:400] + "..." 
                    break
            return texto_encontrado
    except:
        return None

# Panel lateral
st.sidebar.header("🔐 Acceso VIP")
clave = st.sidebar.text_input("Introducí tu Clave", type="password")

if clave == "pincha2026":
    st.success("¡Conectado! Leyendo las 170 páginas del curso...")
    
    chat_cliente = st.text_area("¿Qué te puso el cliente?", height=150)

    if st.button("🚀 CONSULTAR AL CURSO Y RESPONDER"):
        if not chat_cliente:
            st.warning("Che, pegá el chat así lo analizo con el PDF.")
        else:
            txt = chat_cliente.lower()
            
            # Determinamos qué buscar en tu curso según la excusa
            busqueda = "cierre"
            if "caro" in txt or "precio" in txt: busqueda = "precio"
            elif "pensar" in txt or "tiempo" in txt: busqueda = "objeción"
            elif "mala" in txt or "calidad" in txt: busqueda = "calidad"
            
            leccion = buscar_en_curso(busqueda)
            
            st.subheader("🎯 Estrategia según tu curso:")
            if leccion:
                st.write("📖 *Basado en tu teoría:*")
                st.info(leccion)
                st.write("---")
            
            # Respuesta sugerida final
            st.subheader("👉 Respuesta sugerida para copiar:")
            # Aquí la lógica de respuestas que ya teníamos, pero ahora reforzada
            if "caro" in txt:
                res = "Entiendo. Pero como explico en el curso, el precio es relativo al valor. ¿Vemos cómo esto te va a ahorrar dinero?"
            else:
                res = "Excelente punto. ¿Te parece si coordinamos ahora así no perdés el beneficio por tiempo limitado?"
            
            st.success(res)
            st.balloons()

else:
    st.info("Poné la clave 'pincha2026' para activar el sistema.")
