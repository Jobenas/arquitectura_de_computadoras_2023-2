import time

def potencia(n: int, div: int) -> int:
    pot = 1

    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot


if __name__ == "__main__":
    inicio = time.perf_counter()
    p1 = potencia(100_000, 2)
    p2 = potencia(100_000, 2)
    p = p1 * p2
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")