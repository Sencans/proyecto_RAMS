# 👑 R.A.M.S. V2.0 — MAGI Terminal

![R.A.M.S. Version](https://img.shields.io/badge/Versión-2.0-red.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Gemini API](https://img.shields.io/badge/Motor-Gemini_AI-orange.svg)

R.A.M.S. (MAGI Terminal) es un asistente virtual avanzado y altamente personalizable de código abierto. Más que un simple chatbot, es un "Sistema Operativo de IA" con personalidad propia, capaz de interactuar con tu computadora, ver tu pantalla, controlar tu música, organizar tus archivos y aprender de sus errores.

## ✨ Características Principales

Tu asistente cuenta con un arsenal de herramientas integradas:

* **👁️ Visión Computacional:** Puede tomar capturas de pantalla en tiempo real y analizar lo que estás viendo, o leer la señal de tu cámara web.
* **🎵 Control Total de Spotify:** Reproduce canciones, cambia de pista, ajusta el volumen y revisa qué está sonando sin tocar la aplicación.
* **🎮 Modos de Entorno:**
    * `Modo Juego`: Abre Steam, Xbox Game Bar y pone "Welcome to the Jungle" automáticamente.
    * `Modo Chamba`: Prepara tu entorno de trabajo abriendo tus IAs y buscadores favoritos de golpe.
* **👻 Modo Fantasma (Tomar Control):** Inspirado en DDLC, la IA puede minimizar tus ventanas, abrir el Bloc de Notas y escribirte mensajes directamente con su propia "conciencia".
* **🗂️ Organizador Inteligente:** Ordena carpetas caóticas clasificando imágenes, videos, documentos y código automáticamente.
* **📝 Creador de Documentos:** Genera archivos Word, Excel (con gráficos) y PDF visualmente atractivos con un solo comando de voz o texto.
* **🧠 Memoria y Cápsulas de Tiempo:** Aprende de los errores de código, guarda recordatorios programados y te envía mensajes al futuro mediante "Cápsulas de tiempo".
* **🎙️ Clonación y TTS:** Usa Edge TTS para hablar de forma fluida y puede integrarse con ElevenLabs para clonar voces.

## 🚀 Instalación y Primer Uso

R.A.M.S. cuenta con un sistema de configuración inicial automático. No necesitas quemar tus contraseñas en el código.

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/Sencans/proyecto_RAMS.git](https://github.com/Sencans/proyecto_RAMS.git)
   cd proyecto_RAMS
Instala las dependencias necesarias:
Asegúrate de tener instaladas librerías como customtkinter, webview, google-generativeai, spotipy, opencv-python, edge-tts, SpeechRecognition, etc.

Inicia el sistema:

Bash
python test2.py
Inicialización MAGI:
Al correrlo por primera vez, el sistema detectará que no hay configuración. Se abrirá una interfaz gráfica negra pidiéndote:

El nombre que le quieres dar a tu IA.

Tu API Key de Google Gemini.

(Opcional) Tus datos SMTP para envío de correos.

Estos datos se guardarán localmente en un archivo config_rams.txt de forma segura.

⚙️ Estructura del Workspace
El sistema opera dentro de una carpeta segura llamada Workspace_RAMS. Aquí es donde:

Se guardan las imágenes generadas y los modelos 3D interpretados (Blender).

Se almacenan las memorias (RAMS_REGLAS.md, capsulas_tiempo.json).

Se exportan los documentos Word, Excel y PDF creados por la IA.

⚠️ Notas de Privacidad y Seguridad
APIs: Nunca subas el archivo config_rams.txt a repositorios públicos. Mantén tus API Keys seguras.

Control del PC: Este script tiene permisos para mover el mouse, teclear, abrir archivos y capturar pantalla. Úsalo bajo tu propio riesgo y supervisión.

Desarrollado como núcleo central de asistencia personal impulsado por inteligencia artificial.

SOLO FUNCIONA EN WINDOWS 11/10
