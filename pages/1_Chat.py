import streamlit as st
import logging
from utils.pinecone_utils import interpret_and_search
from utils.embedding_utils import generate_chat_response

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a la página ChatBot IoT con interfaz estilo ChatGPT")

    st.title("ChatBot IoT - Estilo ChatGPT")

    # Inicializar el historial en session_state, si no existe
    if "messages" not in st.session_state:
        st.session_state["messages"] = []  # cada elemento: {"role": "user"/"assistant", "content": "texto..."}

    # Mostrar mensajes previos en burbujas de chat
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Crear una entrada de chat (input) en la parte inferior
    user_prompt = st.chat_input("Escribe tu pregunta o comando...")

    if user_prompt:  # cuando el usuario envía algo
        # Añadir el mensaje del usuario al historial
        st.session_state["messages"].append({"role": "user", "content": user_prompt})
        # Render burbuja
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # 1) Interpretar la query => obtener contextos
        contexts, used_filter, used_fallback = interpret_and_search(user_prompt)

        # 2) Generar respuesta
        # Podrías construir un “mega prompt” con la historia + contexts, pero
        # si no lo necesitas, bastará con mandar contexts a generate_chat_response.
        # Ejemplo simple: pasamos contexts y user_prompt.
        assistant_response = generate_chat_response(contexts, user_prompt)

        # Añadir respuesta al historial
        st.session_state["messages"].append({"role": "assistant", "content": assistant_response})
        # Render burbuja assistant
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

def main():
    app()

if __name__ == "__main__":
    main()
