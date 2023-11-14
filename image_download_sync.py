import time
import requests



urls =  [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg' ,
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]


def descarga(url) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    with open(f'./images/{url.split("/")[-1]}', 'wb') as f:
        f.write(response.content)
    
    return True

if __name__ == "__main__":
    inicio = time.perf_counter()
    for url in urls:
        print(f"Descargando {url}")
        resultado = descarga(url)
        if not resultado:
            print(f"Error al descargar {url}")
    fin = time.perf_counter()

    print(f"Tiempo de descarga: {fin - inicio} segundos")
