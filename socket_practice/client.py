import socket
# from socket_practice.server import SERVER
PORT = 5050
SERVER = "192.168.100.7"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
LEA = "LEAVE"
HEADER = 64
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialize the socket of the client
socket_client.connect(ADDR) # instead of bind, we connect

def send_msg(msg):
    message = msg.encode(FORMAT) # encode string into bytes to send it
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    socket_client.send(send_len)
    socket_client.send(message)
    print(socket_client.recv(2048).decode(FORMAT))

send_msg("hello")
send_msg("hello")
send_msg("hello")
send_msg("hello")
send_msg(LEA)
