import socket
import time

SOCK_BUFFER = 1024


def busca_codigo(pos: int) -> str:
    with open("codigos.txt", "r") as f:
        contenido = f.read()
    c_lista = contenido.split("\n")

    if pos >= len(c_lista):
        return None
    cod = c_lista[pos]

    return cod


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)
    print("Esperando conexiones...")

    while True:
        conn, client_address = sock.accept()
        # print(f"Conexion desde {client_address[0]}:{client_address[1]}")
        inicio_conexion = time.perf_counter()
        try:
            while True:
                dato = conn.recv(SOCK_BUFFER)

                if not dato:
                    break
                try:
                    # print(f"Recibimos posicion: {dato}")
                    inicio_archivo = time.perf_counter()
                    codigo = busca_codigo(int(dato.decode('utf-8')))
                    fin_archivo = time.perf_counter()
                except ValueError:
                    continue

                if codigo:
                    conn.sendall(codigo.encode('utf-8'))
        except ConnectionResetError:
            print("El cliente cerro la conexion de manera abrupta")
        finally:
            # print("Cerrando la conexion")
            conn.close()
            fin_conexion = time.perf_counter()
            print(f"Tiempo de lectura de archivo: {fin_archivo - inicio_archivo} segundos")
            print(f"Tiempo de conexion: {fin_conexion - inicio_conexion} segundos")
