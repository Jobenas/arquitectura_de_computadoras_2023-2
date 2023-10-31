import time


def func1():
    print("Iniciando funcion 1")
    time.sleep(2)
    print("Terminando funcion 1")


def func2():
    print("Iniciando funcion 2")
    time.sleep(3)
    print("Terminando funcion 2")


def func3():
    print("Iniciando funcion 3")
    time.sleep(1)
    print("Terminando funcion 3")


def main():
    func1()
    func2()
    func3()


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
