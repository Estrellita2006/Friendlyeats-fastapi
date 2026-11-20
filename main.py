
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.restaurants import router as restaurants_router
from app.api.v1.web import router as web_router


app = FastAPI(title="FriendlyEats FastAPI")


# Conectar archivos CSS, JavaScript e imágenes
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Conectar las rutas de la API
app.include_router(restaurants_router, prefix="/api")


# Conectar las páginas HTML
app.include_router(web_router)


# Comprobar que el servidor funciona
@app.get("/health")
async def health():
    return {"status": "ok"}
