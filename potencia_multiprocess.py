from multiprocessing import Process
import time

def potencia(n: int, div: int) -> int:
    pot = 1

    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot


if __name__ == "__main__":
    inicio = time.perf_counter()
    p1 = Process(target=potencia, args=(100_000, 2))
    p2 = Process(target=potencia, args=(100_000, 2))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")