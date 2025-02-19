import streamlit as st
from utils.logging_config import setup_logging
import logging

def main():
    # Iniciamos logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # Configurar la página de Streamlit
    st.set_page_config(
        page_title="Monitor IoT",
        page_icon="🛰️",
        layout="wide"
    )

    # Mensaje inicial
    logger.info("Iniciando la app principal app.py")
    st.title("IoT Monitor: La Solución Integral para Dispositivos IoT")
    st.markdown("""
    <style>
    .highlight {
        background-color: #eef8fa;
        padding: 15px;
        border-radius: 5px;
    }
    .titulo-seccion {
        color: #2B547E;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    <h2 class="titulo-seccion">¿Qué es IoT Monitor?</h2>
    <p>
      IoT Monitor es la plataforma definitiva para supervisar, gestionar y optimizar 
      tus dispositivos IoT, aprovechando <strong>Pinecone</strong> y <strong>OpenAI</strong>.
    </p>
    <h3 class="titulo-seccion">Beneficios Clave:</h3>
    <ul>
      <li><strong>Monitoreo en tiempo real</strong> (señal, batería, ubicación)</li>
      <li><strong>Búsqueda Inteligente</strong> con embeddings + re-rank</li>
      <li><strong>Reportes PDF</strong> para clientes</li>
      <li><strong>Alertas avanzadas</strong> (tamper detectado, restricción violada, etc.)</li>
    </ul>
    <p>
      Eleva la productividad de tus operaciones y ahorra costos con 
      una solución IoT verdaderamente completa. 
      ¡Bienvenido a <em>IoT Monitor</em>!
    </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
