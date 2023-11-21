import time

def potencia(n: int) -> int:
    pot = 1
    for _ in range(n):
        pot = pot * n

    return pot


if __name__ == "__main__":
    inicio = time.perf_counter()
    potencia(100_000)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")