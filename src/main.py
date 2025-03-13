from fastapi import FastAPI
from controller.controller import router

app = FastAPI(
    title="API de Historias Clínicas",
    description="Sistema de gestión de pacientes y sus historias clínicas",
    version="1.0.0"
)

# Registrar las rutas del controlador
app.include_router(router)

# Mensaje de bienvenida en la raíz
@app.get("/")
async def inicio():
    return {"mensaje": "Bienvenido a la API de Historias Clínicas"}

# Punto de entrada para ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)