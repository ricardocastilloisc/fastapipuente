from fastapi import FastAPI, HTTPException  # Asegúrate de importar HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import math
app = FastAPI()

# Agregar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a los orígenes que deseas permitir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OBJ_DIR = os.path.join(BASE_DIR, 'models')  # Asegúrate de que existe la carpeta 'models'

@app.get("/puente")
async def get_puente():
    puente_data = {
        "torres": [
            {
                "tipo": "box",
                "ancho": 0.2,
                "alto": 4,
                "profundidad": 0.2,
                "color": "red",
                "posicion": [-2.5, 2, 0]
            },
            {
                "tipo": "box",
                "ancho": 0.2,
                "alto": 4,
                "profundidad": 0.2,
                "color": "red",
                "posicion": [2.5, 2, 0]
            }
        ],
        "cables": [
            {
                "tipo": "cylinder",
                "radio": 0.05,
                "altura": 5,
                "color": "grey",
                "posicion": [0, 0, 0],
                "rotation": [math.pi / 4, 0, 0]
            },
            {
                "tipo": "cylinder",
                "radio": 0.05,
                "altura": 5,
                "color": "grey",
                "posicion": [0, 0, 0],
                "rotation": [-math.pi / 4, 0, 0]
            },
        ],
        "plataforma": {
            "tipo": "box",
            "ancho": 5,
            "alto": 0.2,
            "profundidad": 1,
            "color": "green",
            "posicion": [0, 1, 0]
        }
    }
    return puente_data


@app.get("/casa")
async def get_casa():
    casa_data = {
        "paredes": [
            {
                "tipo": "box",
                "ancho": 4,
                "alto": 3,
                "profundidad": 1,
                "color": "lightblue",
                "posicion": [0, 1.5, 0]
            },
            {
                "tipo": "box",
                "ancho": 4,
                "alto": 3,
                "profundidad": 1,
                "color": "lightblue",
                "posicion": [0, 1.5, -2]
            },
            {
                "tipo": "box",
                "ancho": 1,
                "alto": 3,
                "profundidad": 4,
                "color": "lightblue",
                "posicion": [-2, 1.5, -1]
            },
            {
                "tipo": "box",
                "ancho": 1,
                "alto": 3,
                "profundidad": 4,
                "color": "lightblue",
                "posicion": [2, 1.5, -1]
            },
        ],
        "techo": {
            "tipo": "cone",
            "radio": 3,
            "altura": 2,
            "color": "brown",
            "posicion": [0, 4, -1]
        },
        "jardin": {
            "tipo": "plane",
            "ancho": 10,
            "alto": 10,
            "color": "green",
            "posicion": [0, 0, -1]
        }
    }
    return casa_data