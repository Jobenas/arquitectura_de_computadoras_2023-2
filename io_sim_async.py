import asyncio
import time


async def func1():
    print("Iniciando funcion 1")
    await asyncio.sleep(2)
    print("Termiando funcion 1")


async def func2():
    print("Iniciando funcion 2")
    await asyncio.sleep(3)
    print("Terminando funcion 2")


async def func3():
    print("Iniciando funcion 3")
    await asyncio.sleep(1)
    print("Terminando funcion 3")


async def main():
    await asyncio.gather(func1(), func2(), func3())


if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundo")

