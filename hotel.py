from fastapi import FastAPI
import asyncio

app = FastAPI()

habitaciones = 8
lock = asyncio.Lock()

@app.get("/reservar")
async def reservar():
    global habitaciones

    async with lock:
        if habitaciones > 0:
            await asyncio.sleep(0.2)
            habitaciones -= 1
            return {"mensaje": "Reserva exitosa", "disponibles": habitaciones}
        else:
            return {"mensaje": "No hay habitaciones disponibles"}

@app.get("/estado")
async def estado():
    return {"habitaciones_disponibles": habitaciones}

@app.post("/reiniciar")
async def reiniciar():
    global habitaciones
    habitaciones = 8
    return {"mensaje": "Sistema reiniciado", "habitaciones": habitaciones}