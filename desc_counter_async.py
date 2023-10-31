import asyncio
import time


async def count():
    idx = 100
    while idx > 0:
        print(f"{idx}")
        idx -= 1
        await asyncio.sleep(0.1)


async def main():
    tasks = [count() for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin - inicio} segundos")
