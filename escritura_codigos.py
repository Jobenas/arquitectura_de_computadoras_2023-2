if __name__ == '__main__':
    codigo_inicial = 20230001

    with open("codigos.txt", "w+", encoding="utf-8") as f:
        for i in range(200):
            f.write(f"{codigo_inicial + i}")
