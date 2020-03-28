import socket
import multiprocessing
import threading
# from socket import *
BUFSIZ = 1024

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escutar a porta 9000
server = sock.bind(('localhost', 9000))

# Definir o limite de 1 conexao paralela
sock.listen(1)

def send_msg():
    msg = raw_input("Enter your message to client! \n")
    for conn in connections:
        conn.send("servidor: " +msg)
    # for socket_client in connections:
    #         socket_connection.connection.sendall(str(len(msg)).zfill(BUFSIZ).encode())
    #         socket_connection.connection.sendall(message.encode())

def wait_message(client):
    msg_client = ''

    while msg_client != 'see ya':
        expected_data_size = ''
        while expected_data_size == '':
            expected_data_size += client.recv(BUFSIZ).decode()
        expected_data_size = int(expected_data_size)

        received_data = ''
        while len(received_data) < expected_data_size:
            received_data += client.recv(BUFSIZ).decode()

        formatted_message = "cliente: " + received_data
        msg_client = received_data
        print(formatted_message)

    connections.remove(client)
    client.connection.close()


last_message = ''
connections = []


while True:
    print("Aguardando conexao")
    connection, address_client = sock.accept()
    print("connection\n")
    print(connection)
    print("address_client\n")
    print(address_client)
    connection.send(bytes("Now type your name and press enter"))
    #new_connection = SockConnection(connection, address_client)
    connections.append(address_client)
    print("{} conectado".format(address_client))
    threading.Thread(target=wait_message, args=(connection,)).start()
    threading.Thread(target=send_msg).start()
    # worker.setDaemon(True)
    # worker.start()


# Finalizar a conexao
connection.close()
