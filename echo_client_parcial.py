import socket
import time

SOCK_BUFFER = 4


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    inicio = time.perf_counter()
    sock.connect(server_address)

    try:
        msg = "Hola mundo!"
        amnt_expected = len(msg)
        amnt_received = 0
        sock.sendall(msg.encode("utf-8"))
        data = b''
        while amnt_received < amnt_expected:
            partial_data = sock.recv(SOCK_BUFFER)
            amnt_received += len(partial_data)
            print(f"Recibido {partial_data}")
            data += partial_data
        # print(f"Total Recibido {data}")
    finally:
        # print("Cerrando conexion")
        sock.close()
    
    fin = time.perf_counter()

    print(f"Total Recibido {data}")
    print(f"Tiempo de operacion: {fin - inicio} segundos")
