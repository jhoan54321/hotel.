import asyncio
import httpx

URL = "http://127.0.0.1:8000/reservar"

semaforo = asyncio.Semaphore(5)

async def cliente(id):
    async with semaforo:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(URL)
                data = response.json()

                if "exitosa" in data["mensaje"]:
                    print(f"Cliente {id}: Reservado")
                else:
                    print(f"Cliente {id}: Sin disponibilidad")

            except Exception as e:
                print(f"Cliente {id}: Error {e}")

async def main():
    tareas = [cliente(i) for i in range(1, 31)]
    await asyncio.gather(*tareas)

    async with httpx.AsyncClient() as client:
        estado = await client.get("http://127.0.0.1:8000/estado")
        print("Estado final:", estado.json())

if __name__ == "__main__":
    asyncio.run(main())