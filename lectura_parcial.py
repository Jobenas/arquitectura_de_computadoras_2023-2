import time


if __name__ == '__main__':
    contenido = ""
    inicio = time.perf_counter()
    with open("codigos.txt", "r", encoding="utf-8") as f:
        for _ in range(200):
            contenido += f.readline()
    fin = time.perf_counter()
    
    print(contenido)
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

