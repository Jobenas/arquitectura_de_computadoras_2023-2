from multiprocessing import Pool
import time

proc = 4

tareas = 4

def potencia(n: int, div: int) -> int:
    pot = 1

    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot


if __name__ == "__main__":
    inicio = time.perf_counter()
    args = [[100_000, tareas]] * tareas
    p = Pool(processes=proc)
    p1 = p.starmap(potencia, args)
    p.close()
    p.join()

    pot = 1
    for i in range(len(p1)):
        pot = pot * p1[i]
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")