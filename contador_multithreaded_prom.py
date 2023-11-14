import time
from threading import Thread

CUENTA = 50_000_000


def cuenta(n):
    while n > 0:
        n -= 1


def cuenta_multithreaded():
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(CUENTA // 2,))
    t2 = Thread(target=cuenta, args=(CUENTA // 2,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    fin = time.perf_counter()

    return fin - inicio


if __name__ == "__main__":
    tiempos = list()
    
    for i in range(10):
        print(f"Iteracion {i + 1} / 10")
        tiempos.append(cuenta_multithreaded())

    tiempo_promedio = sum(tiempos) / len(tiempos)

    print(f"Tiempo de ejecucion multihilo: {tiempo_promedio} segundos")
