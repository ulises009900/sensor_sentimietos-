# Sensor de Sentimientos

Este proyecto es una API REST construida con **FastAPI** que permite analizar el sentimiento de un texto ingresado (Positivo, Negativo o Neutral) utilizando la librería **TextBlob**. Los resultados se almacenan automáticamente en una base de datos **SQLite**.

## Características

- **Análisis de Sentimiento:** Clasifica comentarios según su polaridad usando procesamiento de lenguaje natural.
- **Persistencia de Datos:** Guarda cada análisis con su fecha y resultado en una base de datos local.
- **Historial:** Permite consultar todos los análisis realizados anteriormente.

## Requisitos

Necesitas tener instalado Python 3.x y las siguientes dependencias:

- `fastapi`
- `uvicorn`
- `textblob`

Puedes instalarlas ejecutando:

```bash
pip install fastapi uvicorn textblob
```

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el servidor con el siguiente comando:

```bash
uvicorn Api:app --reload
```

3. El servidor iniciará en `http://127.0.0.1:8000`.

## Uso de la API

### 1. Analizar un comentario

- **Endpoint:** `/analizar/`
- **Método:** `GET`
- **Ejemplo:** `http://127.0.0.1:8000/analizar/?comentario=Estoy muy feliz con el resultado`

Devuelve un JSON con el sentimiento detectado y confirma el guardado.

### 2. Ver historial

- **Endpoint:** `/historial/`
- **Método:** `GET`
- **Ejemplo:** `http://127.0.0.1:8000/historial/`

Devuelve una lista de todos los registros almacenados en la base de datos.

## Estructura del Proyecto

- `Api.py`: Punto de entrada de la aplicación FastAPI.
- `cerebro.py`: Lógica de análisis de sentimiento.
- `db.py`: Funciones para interactuar con la base de datos SQLite.