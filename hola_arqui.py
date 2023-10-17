if __name__ == '__main__':
    frase = "hola mundo desde el curso de arqui"

    with open("archivo.txt", "w+", encoding="utf-8") as f:
        f.write(frase)
    