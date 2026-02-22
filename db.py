import sqlite3
from datetime import datetime

def crear_tabla():
  conexion = sqlite3.connect("sentimientos.db")
  cursor = conexion.cursor()
  cursor.execute("""
                 CREATE TABLE IF NOT EXISTS historial(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   texto TEXT NOT NULL,
                   resultado TEXT NOT NULL,
                   fecha TEXT NOT NULL)
                 """)
  conexion.commit()
  conexion.close()
  
def guardar_analisis(resultado,texto):
  conexion = sqlite3.connect("sentimientos.db")
  cursor = conexion.cursor()
  fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  cursor.execute("INSERT INTO historial (texto, resultado, fecha) VALUES (?, ?, ?)", (texto, resultado, fecha))
  conexion.commit()
  conexion.close()