from fastapi import FastAPI
from cerebro import analizar_sentimiento
from db import crear_tabla, guardar_analisis


crear_tabla() #crear la  base de datos  al inicialr la app 
app = FastAPI()

@app.get("/analizar/")
def analizar(comentario: str):
# analizar los sentimientos del comentario
  resultado = analizar_sentimiento(comentario)
    
#guardar en SQLite
  guardar_analisis(resultado, comentario)
  return{"comentario": comentario,
         "sentimiento": resultado,
         "status":"guardado con exito"  }