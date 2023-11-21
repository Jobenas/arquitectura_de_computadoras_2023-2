from multiprocessing import Process
import time

def potencia(n: int, div: int) -> int:
    pot = 1

    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot


if __name__ == "__main__":
    num_proc = 4
    inicio = time.perf_counter()
    procesos = list()
    for _ in range(num_proc):
        p = Process(target=potencia, args=(100_000, num_proc))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")