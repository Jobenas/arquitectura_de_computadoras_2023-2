import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.25', 5001)
    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    inicio = time.perf_counter()
    sock.connect(server_address)
    codigo_alumno = "20230009"
    pos = f"codigo:{codigo_alumno}"

    sock.sendall(pos.encode('utf-8'))
    codigo = sock.recv(SOCK_BUFFER)

    print(f"Codigo recibido: {codigo.decode('utf-8')}")

    sock.close()
    fin = time.perf_counter()
    print(f"Tiempo de conexion: {fin - inicio} segundos")

    codigo = codigo.decode('utf-8')
    notas = codigo.split(",")

    labs = 0

    for i in range(1, 15):
        labs += int(notas[i])
    labs = labs / 14
    e1 = int(notas[15])
    e2 = int(notas[16])

    promedio = labs * 0.5 + e1 * 0.25 + e2 * 0.25

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.sendall(f"nota:{codigo_alumno}:{promedio}".encode('utf-8'))
    respuesta = sock.recv(SOCK_BUFFER)
    sock.close()
    print(f"Recibi: {respuesta}")
