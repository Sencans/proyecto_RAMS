import sqlite3
import datetime

class MemoriaRAMS:
    def __init__(self):
        self.conn = sqlite3.connect("memoria_profunda.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS recuerdos 
                            (id INTEGER PRIMARY KEY, fecha TEXT, categoria TEXT, contenido TEXT)''')
        self.conn.commit()

    def guardar_recuerdo(self, categoria, contenido):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO recuerdos (fecha, categoria, contenido) VALUES (?, ?, ?)", 
                            (fecha, categoria, contenido))
        self.conn.commit()
        print(f"🧠 [MEMORIA] Nuevo dato guardado: {categoria}")

    def buscar_recuerdos(self, query):
        # Buscador simple por palabras clave
        self.cursor.execute("SELECT contenido FROM recuerdos WHERE contenido LIKE ?", (f'%{query}%',))
        resultados = self.cursor.fetchall()
        return [r[0] for r in resultados]

    def obtener_todo(self):
        self.cursor.execute("SELECT fecha, categoria, contenido FROM recuerdos ORDER BY id DESC LIMIT 10")
        return self.cursor.fetchall()