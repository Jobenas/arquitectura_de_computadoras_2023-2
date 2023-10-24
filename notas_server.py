import socket
import time

SOCK_BUFFER = 1024


def busca_codigo(pos: int) -> str:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    c_lista = contenido.split("\n")
    print("Tengo la lista")

    if pos >= len(c_lista):
        return None
    cod = c_lista[pos]

    return cod

def guardar_nota(codigo: str, nota: str) -> None:
    with open("promedios.csv", "a") as f:
        f.write(f"{codigo},{nota}\n")


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
                print(f"Recibi {dato}")
                if not dato:
                    break
                try:
                    # print(f"Recibimos posicion: {dato}")
                    mensaje = dato.decode('utf-8')
                    mensaje = mensaje.split(":")
                    print(f"mensaje: {mensaje}")
                    if len(mensaje) > 1:
                        match mensaje[0]:
                            case "codigo":
                                print("dentro de codigo")
                                inicio_archivo = time.perf_counter()
                                codigo = busca_codigo(int(mensaje[1]) - 20230001)
                                fin_archivo = time.perf_counter()
                                if codigo:
                                    conn.sendall(codigo.encode('utf-8'))
                            case "nota":
                                print("dentro de nota")
                                guardar_nota(mensaje[1], mensaje[2])
                                conn.sendall("Nota guardada".encode('utf-8'))
                            case _:
                                ...
                except ValueError:
                    continue
        except ConnectionResetError:
            print("El cliente cerro la conexion de manera abrupta")
        finally:
            conn.close()
            fin_conexion = time.perf_counter()
            print("Cerrando la conexion")