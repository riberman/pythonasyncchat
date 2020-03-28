import socket
import time
import threading

BUFSIZ = 1024
# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9000))

flag = True
def listemServer(sock,flag):
    while (flag):
        # Leia o tamanho da mensagem
        expected_data_size = len(sock.recv(BUFSIZ).decode())
        #print("Tamanho de dado esperado = {}".format(expected_data_size))

        received_data = ''
        while len(received_data) < expected_data_size:
            # Ler o dado recebido
            received_data += sock.recv(BUFSIZ).decode()
            print("Tamanho do dado {}".format(len(received_data)))
        print("servidor: " + received_data)
        time.sleep(3)
        if (received_data == "see ya"):
            time.sleep(3)
            flag = False

listener = threading.Thread(target=listemServer, args=(sock,flag,))
listener.setDaemon(True)
listener.start()

while (flag):
    # Tamanho da mensagem
    inputTxt = raw_input("Enter your message to server! \n")
    mensagem = inputTxt
    send_data_size = len(mensagem)
    sock.sendall(str(send_data_size).zfill(BUFSIZ).encode())

    # Enviar a mensagem
    sock.sendall(mensagem.encode())

    if (mensagem == "see ya"):
        time.sleep(3)
        flag = False

# Finalizar a conexao
sock.close()
