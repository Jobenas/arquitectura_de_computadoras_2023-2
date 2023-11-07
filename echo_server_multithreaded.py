import socket
from threading import Thread

SOCK_BUFFER = 1024

num_clientes = 0

def client_handler(conn, client_address):
    global num_clientes
    print(f"Conexion desde {client_address[0]}:{client_address[1]}")
    num_clientes += 1
    print(f"Numero de clientes conectados: {num_clientes}")
    try:
        while True:
            data = conn.recv(SOCK_BUFFER)

            if data:
                print(f"Recibido {data}")
                conn.sendall(data)
            else:
                print(f"No hay mas datos")
                break
    except ConnectionResetError:
        print("el cliente ha cerrado abruptamente la conexion")
    finally:
        print("El cliente ha cerrado la conexion")
        conn.close()
        num_clientes -= 1


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en IP {server_address[0]} y puerto {server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        connection, c_address = sock.accept()
        
        t = Thread(target=client_handler, args=(connection, c_address))
        t.start()
