import streamlit as st

# Configuración de página
st.set_page_config(page_title="VentaPsicologica AI", page_icon="💰")

# --- ESTILO Y LOGO ---
# Como no tenemos el archivo del logo subido, usamos un emoji grande y un título con estilo
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🧠 VentaPsicologica</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>El Cerrador de Ventas N°1</b></p>", unsafe_allow_html=True)
st.write("---")

# --- PANEL DE CONTROL (IZQUIERDA) ---
st.sidebar.header("🔐 Acceso Clientes")
clave = st.sidebar.text_input("Introducí tu Clave Premium", type="password")

# --- BOTÓN DE PAGO ---
st.sidebar.write("---")
st.sidebar.subheader("💳 Suscripción")
# Reemplazá el link de abajo por tu link de Mercado Pago o tu WhatsApp
link_pago = "https://wa.me/tu_numero_aca?text=Hola%20Fran,%20quiero%20pagar%20la%20membresia"
st.sidebar.markdown(f'''
    <a href="{link_pago}" target="_blank">
        <button style="width:100%; background-color:#00c853; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">
            ✅ PAGAR MEMBRESÍA
        </button>
    </a>
    ''', unsafe_allow_html=True)

# --- LÓGICA DE LA APP ---
if clave == "pincha2026":
    st.success("¡Acceso Total, Fran! Vamos a cerrar esa venta.")
    
    chat_cliente = st.text_area("Pega el chat del cliente acá abajo:", placeholder="Ej: No tengo plata...")

    if st.button("🚀 ANALIZAR Y CERRAR"):
        if not chat_cliente:
            st.warning("Che, no pusiste nada. Escribí lo que te dijo el cliente.")
        else:
            # Lógica de detección mejorada
            texto = chat_cliente.lower()
            st.subheader("🛠️ Estrategia Sugerida:")
            
            if "caro" in texto or "plata" in texto or "dinero" in texto:
                st.info("**Técnica: Reencuadre de Valor**")
                st.write("Decile: 'Entiendo que cuides tu economía. Pero justamente por eso necesitás esto: para dejar de perder ventas y que el dinero deje de ser un problema. ¿Preferís ahorrar hoy o ganar mañana?'")
            
            elif "pensar" in texto or "después" in texto or "mañana" in texto:
                st.info("**Técnica: Escasez y Urgencia**")
                st.write("Decile: 'Tomate el tiempo que necesites. Solo te aviso que los cupos con el descuento actual se están terminando y no quiero que pagues de más después. ¿Te reservo el último?'")
            
            elif "mujer" in texto or "marido" in texto or "socio" in texto:
                st.info("**Técnica: Empoderamiento**")
                st.write("Decile: 'Me parece perfecto que lo consultes. Generalmente, cuando alguien quiere mejorar el negocio, su entorno lo apoya. ¿Querés que te pase un resumen para que le muestres?'")
            
            else:
                st.info("**Técnica: Cierre Directo**")
                st.write("Decile: 'Entiendo perfectamente. Para no dar más vueltas, ¿querés que te mande el link de acceso ahora y ya aprovechás el material hoy mismo?'")
else:
    st.error("⚠️ Debes estar suscripto para usar la IA.")
    st.write("Si todavía no tenés tu clave, hacé clic en el botón verde de la izquierda para pagar por WhatsApp.")
