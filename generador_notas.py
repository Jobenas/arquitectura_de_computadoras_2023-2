import random


if __name__ == "__main__":
    contenido = "codigo,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,e1,e2\n"

    codigo_inicial = 20230001

    for i in range(200):
            linea = f"{codigo_inicial + i},"
            for _ in range(16):
                linea += f"{random.randint(0, 20)},"
            contenido += f"{linea[:-1]}\n"

    with open("notas.csv", "w+", encoding="utf-8") as f:
        f.write(contenido)
