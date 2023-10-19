import socket
import time

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    inicio = time.perf_counter()
    
    sock.connect(server_address)
    try:
        msg = "Hola mundo!"
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
        # print(f"Recibido {data}")
    finally:
        # print("Cerrando conexion")
        sock.close()
    fin = time.perf_counter()

    print(f"Recibido {data}")
    print(f"Tiempo de operacion: {fin - inicio} segundos")
