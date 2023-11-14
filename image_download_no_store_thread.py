import time
import requests
from threading import Thread



urls =  [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg' ,
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
] * 40


def descarga(url) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    return True

if __name__ == "__main__":
    inicio = time.perf_counter()
    threads = list()
    for i in range(len(urls)):
        thread = Thread(target=descarga, args=(urls[i],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    fin = time.perf_counter()

    print(f"Tiempo de descarga: {fin - inicio} segundos")
