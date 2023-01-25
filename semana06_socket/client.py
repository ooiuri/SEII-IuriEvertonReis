import socket
# declaração de constants
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.26"
ADDR = (SERVER, PORT)

# inicialização de socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conexão com o endereço
client.connect(ADDR)

# função de enviar mensagem
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

# envio da mensagem
send(DISCONNECT_MESSAGE)