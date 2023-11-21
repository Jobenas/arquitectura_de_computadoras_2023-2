import numpy as np
import time

M = 5000
N = 5000

def mult_vector_vector(x: list[np.int32], y: list[np.int32]) -> np.int32:
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == "__main__":
    resultado = list()

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    inicio = time.perf_counter()
    for vector in mat_M:
        resultado.append(mult_vector_vector(vector, vector_A))
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")
