import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
sys.path.append(os.getcwd())

from docx import Document

# Crear un documento nuevo
documento = Document()

# Añadir un único párrafo con la palabra "hola"
documento.add_paragraph('hola')

# Guardar el documento, sobreescribiendo el anterior
ruta_archivo = 'documento_generado.docx'
documento.save(ruta_archivo)

print(f"El documento '{ruta_archivo}' ha sido modificado para contener el saludo solicitado.")