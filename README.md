# IoT Monitor Pro 🛰️

Sistema de monitoreo, gestión y análisis de dispositivos IoT que combina el poder de **Pinecone** para búsquedas vectoriales con **OpenAI** para procesamiento de lenguaje natural, todo integrado en una interfaz amigable construida con **Streamlit**.

## 🌟 Características

- **RAG (Retrieval Augmented Generation)** para consultas contextuales
- **Análisis SQL** automático mediante GPT-4
- **Monitoreo en tiempo real** de dispositivos IoT
- **Generación de reportes** en PDF
- **Interfaz intuitiva** para consultas en lenguaje natural

## 📁 Estructura del Proyecto

```
IoT Monitor Pro/
├── .streamlit/
│   └── config.toml          # Configuración de Streamlit
├── src/
│   ├── core/               # Lógica principal
│   │   ├── embeddings.py   # Generación de embeddings
│   │   ├── rag.py         # Sistema RAG
│   │   └── evaluation.py   # Métricas y evaluación
│   └── data/              # Manejo de datos
│       ├── pinecone.py    # Conexión con Pinecone
│       └── bigquery.py    # Integración con BigQuery
├── tests/                 # Tests unitarios
├── .env                   # Variables de entorno (no incluido en git)
├── .gitignore            # Configuración de git
├── app.py                # Aplicación principal
└── requirements.txt      # Dependencias del proyecto
```

## 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd IoT-Monitor-Pro
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   .\venv\Scripts\activate  # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   
   Crea un archivo `.env` con:
   ```
   OPENAI_API_KEY=tu_clave_openai
   PINECONE_API_KEY=tu_clave_pinecone
   PINECONE_INDEX_NAME=tracking1-rag
   ```

## 🎮 Uso

1. **Iniciar la aplicación**
   ```bash
   streamlit run app.py
   ```

2. **Acceder a la interfaz**
   - Abre tu navegador en `http://localhost:8501`
   - La aplicación se iniciará en modo pantalla completa

## 💡 Funcionalidades Principales

### Dashboard
- Métricas en tiempo real
- Estado de dispositivos
- Consultas frecuentes predefinidas

### Chat Inteligente
- Consultas en lenguaje natural
- Respuestas contextuales usando RAG
- Análisis SQL automático

### Reportes
- Generación de informes PDF
- Análisis detallado por dispositivo
- Historial de estados y alertas

## 🛠️ Tecnologías Utilizadas

- **Pinecone**: Base de datos vectorial para búsqueda semántica
- **OpenAI**: Generación de embeddings y procesamiento de lenguaje natural
- **Streamlit**: Framework para la interfaz de usuario
- **Python**: Lenguaje principal de desarrollo
- **SQLite**: Base de datos local para análisis

## 📖 Documentación Adicional

Para más detalles sobre el uso y configuración, consulta la [documentación completa](docs/index.md).

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
