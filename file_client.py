import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.25', 5001)
    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    inicio = time.perf_counter()
    sock.connect(server_address)

    pos = "8"

    sock.sendall(pos.encode('utf-8'))
    codigo = sock.recv(SOCK_BUFFER)

    # print(f"Codigo recibido: {codigo.decode('utf-8')}")

    sock.close()
    fin = time.perf_counter()
    print(f"Tiempo de conexion: {fin - inicio} segundos")
