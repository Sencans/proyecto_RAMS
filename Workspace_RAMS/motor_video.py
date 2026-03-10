import google.generativeai as genai
import time
import os

def analizar_video(ruta_video, pregunta_usuario):
    print(f"[OJO BIÓNICO REAL] Subiendo el video '{os.path.basename(ruta_video)}'...")
    inicio = time.time()
    
    try:
        # 1. Leer tu API Key secreta desde tu archivo de configuración
        ruta_config = "config_rams.txt"
        if not os.path.exists(ruta_config):
            ruta_config = "../config_rams.txt" # Respaldo por si busca en otra carpeta
            
        with open(ruta_config, "r") as f:
            api_key = f.read().splitlines()[1] # La API Key siempre está en la línea 2
            
        genai.configure(api_key=api_key)
        
        # 2. Subimos el video físico a la nube
        video_file = genai.upload_file(path=ruta_video)
        
        # 3. Esperamos a que el servidor lo procese
        print("[OJO BIÓNICO REAL] Extrayendo fotogramas... (esto toma unos 10-20 segundos)")
        while video_file.state.name == "PROCESSING":
            time.sleep(2)
            video_file = genai.get_file(video_file.name)
            
        if video_file.state.name == "FAILED":
            return {"estado": "Error", "razonamiento": "El formato del video no fue aceptado."}
            
        # 4. Razonamiento Visual
        print("[OJO BIÓNICO REAL] Razonando sobre las imágenes...")
        modelo = genai.GenerativeModel('gemini-2.5-flash')
        respuesta = modelo.generate_content([video_file, pregunta_usuario])
        
        # 5. Limpiamos la memoria
        genai.delete_file(video_file.name)
        
        return {
            "estado": "Visión completada",
            "razonamiento": respuesta.text
        }
        
    except Exception as e:
        return {"estado": "Error", "razonamiento": f"Fallo visual: {str(e)}"}