import time

CUENTA = 50_000_000


def cuenta(n):
    while n > 0:
        n -= 1

def cuenta_sync():
    inicio = time.perf_counter()
    cuenta(CUENTA)
    fin = time.perf_counter()

    return fin - inicio


if __name__ == "__main__":
    tiempos = list()

    for i in range(10):
        print(f"Iteración {i + 1} / 10")
        tiempos.append(cuenta_sync())

    tiempo_promedio = sum(tiempos) / len(tiempos)

    print(f"Tiempo de ejecucion sincrono: {tiempo_promedio} segundos")
