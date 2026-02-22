from textblob import TextBlob

def analizar_sentimiento(texto):
  analisis = TextBlob(texto)
  polaridad = analisis.sentiment.polarity
  
  if polaridad > 0:
    return "Positivo"
  elif polaridad < 0:
    return "Negativo"
  else:
    return "Neutral"
  
# Ejemplo de uso
  
comentario = "Me encanta este producto, es increíble!"
