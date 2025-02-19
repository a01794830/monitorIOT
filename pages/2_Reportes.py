import streamlit as st
import logging
from utils.pinecone_utils import query_by_id
from utils.pdf_utils import generar_pdf

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a la página Reportes")
    st.title("Generar Reportes PDF")

    if "last_report_id" not in st.session_state:
        st.session_state["last_report_id"] = ""

    tipo_consulta = st.radio("Tipo de consulta:", ("device_id", "user_id"))
    input_id = st.text_input(f"Ingrese {tipo_consulta}:", value=st.session_state["last_report_id"])

    if st.button("Generar reporte"):
        if not input_id.strip():
            st.warning("Por favor, ingresa un valor de ID válido.")
            return

        st.session_state["last_report_id"] = input_id

        try:
            data = query_by_id(input_id, tipo_consulta)
        except Exception as e:
            st.error(f"Error consultando Pinecone: {e}")
            return

        if data:
            st.success(f"Se encontraron {len(data)} resultados para {tipo_consulta} = {input_id}")
            for idx, item in enumerate(data, start=1):
                st.subheader(f"Registro #{idx}")
                st.json(item)
                st.markdown("---")

            pdf_bytes = generar_pdf(data)
            if pdf_bytes:
                st.download_button(
                    label="Descargar Reporte en PDF",
                    data=pdf_bytes,
                    file_name=f"Reporte_{tipo_consulta}_{input_id}.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("No se generó el PDF.")
        else:
            st.warning(f"No se encontraron registros para {tipo_consulta} = {input_id}")

def main():
    app()

if __name__ == "__main__":
    main()
