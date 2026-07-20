<div align="center">

# 👑 R.A.M.S. — MAGI Terminal

**Un "Sistema Operativo de IA" de escritorio: voz, visión, control del PC y memoria, con una interfaz HUD estilo NERV/Evangelion.**

[![Versión](https://img.shields.io/badge/Versión-2.0-red.svg?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Motor: Gemini](https://img.shields.io/badge/Motor-Google_Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![Plataforma](https://img.shields.io/badge/Plataforma-Windows_10%2F11-0078D6?style=flat-square&logo=windows&logoColor=white)](#)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg?style=flat-square)](LICENSE)

</div>

---

R.A.M.S. es un asistente virtual avanzado y altamente personalizable de código abierto. Más que un chatbot, es un asistente con personalidad propia capaz de interactuar con tu computadora: ve tu pantalla, controla tu música, organiza tus archivos, genera documentos y aprende de sus errores.

## 📑 Tabla de Contenidos

- [Características principales](#-características-principales)
- [Requisitos](#-requisitos)
- [Instalación y primer uso](#-instalación-y-primer-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Privacidad y seguridad](#️-privacidad-y-seguridad)
- [Licencia](#-licencia)

---

## ✨ Características Principales

* **👁️ Visión computacional:** captura y analiza tu pantalla en tiempo real, o lee la señal de tu cámara web.
* **🎵 Control total de Spotify:** reproduce canciones, cambia de pista, ajusta el volumen y consulta qué suena.
* **🎮 Modos de entorno:**
    * *Modo Juego*: abre Steam y Xbox Game Bar y prepara el ambiente automáticamente.
    * *Modo Chamba*: abre tus IAs y buscadores favoritos de golpe para trabajar.
* **👻 Modo Fantasma:** la IA puede minimizar ventanas, abrir el Bloc de Notas y escribirte mensajes con su propia "conciencia".
* **🗂️ Organizador inteligente:** ordena carpetas clasificando imágenes, vídeos, documentos y código automáticamente.
* **📝 Creador de documentos:** genera archivos Word, Excel (con gráficos) y PDF con un solo comando de voz o texto.
* **🧠 Memoria y cápsulas de tiempo:** aprende de errores de código, guarda recordatorios programados y te envía mensajes al futuro.
* **🎙️ TTS y voz:** usa Edge TTS para hablar de forma fluida; integrable con backends de clonación de voz.

---

## 📋 Requisitos

- **Python 3.10 o superior**
- **Windows 10 / 11** (usa APIs específicas de Windows para el control del sistema)
- Una **API Key de Google Gemini** ([obtenla aquí](https://aistudio.google.com/app/apikey))

---

## 🚀 Instalación y Primer Uso

```bash
# 1. Clona el repositorio
git clone https://github.com/Sencans/proyecto_RAMS.git
cd proyecto_RAMS

# 2. (Recomendado) Crea un entorno virtual
python -m venv .venv
.venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Inicia el sistema
python main.py
```

### Inicialización MAGI

Al ejecutarlo por primera vez, el sistema detecta que no hay configuración y abre una interfaz gráfica que te pide:

- El **nombre** que quieres darle a tu IA.
- Tu **API Key de Google Gemini**.
- *(Opcional)* Tus datos **SMTP** para el envío de correos.

Estos datos se guardan localmente en `config_rams.txt`, que está **excluido del control de versiones** por el `.gitignore` para proteger tus claves.

---

## 📂 Estructura del Proyecto

```
proyecto_RAMS/
├── main.py             # Núcleo del asistente (IA, voz, visión, control del SO)
├── hud.html            # Interfaz HUD estilo NERV/MAGI (mostrada vía pywebview)
├── memoria_rams.py     # Módulo de memoria persistente (SQLite)
├── RAMS_REGLAS.md      # Reglas / personalidad del asistente
├── requirements.txt    # Dependencias de Python
└── Workspace_RAMS/     # Carpeta de trabajo donde la IA genera documentos y scripts
```

---

## ⚠️ Privacidad y Seguridad

- **API Keys:** el archivo `config_rams.txt` contiene tus claves y **nunca debe subirse** a un repositorio público. Ya está incluido en `.gitignore`.
- **Control del PC:** este programa puede mover el ratón, teclear, abrir archivos y capturar la pantalla. Úsalo bajo tu propia responsabilidad y supervisión.

---

## 📄 Licencia

Distribuido bajo la licencia **MIT**. Consulta el archivo [`LICENSE`](LICENSE) para más información.

---

<div align="center">

Hecho con 💜 por [**Sencanxg**](https://github.com/Sencans) · Colombia 🇨🇴

*"Si el sistema no tiene personalidad, solo es una calculadora rápida."*

</div>
