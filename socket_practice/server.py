import socket 
import threading


PORT = 5050
myPC = socket.gethostname() # this function return the host name
"""SERVER = socket.gethostbyname(myPC) # this function return the ip address by hostname 
for some reasons, it returns tonly the ethernet adapter ip, which im not using
"""
SERVER = "192.168.100.7"
ADDR = (SERVER, PORT)
print (SERVER, myPC, ADDR)

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to initilize the connection stream over IPv4
socket_server.bind(ADDR) # return any connection of this address and port to the socket


def start():
    socket_server.listen() # start listening on the binded port
    print(f"[LISTENING] server listening of port {PORT}")
    while True:
        conn, addr = socket_server.accept() # stores any connection and do not drop it
        thread = threading.Thread(target=client_handle, args=(conn,addr)) ;""" 
        push the incoming connections into client_handle funciton, all in separated threads"""
        thread.start() #start the thread process
        print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # print the active threads, (-1) to remove the program thread form count

HEADER = 64
FORMAT = "utf-8"
LEA = "LEAVE"
def client_handle(conn, addr):
    print(f"[NEW CONNECTION] {addr} is connected")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len: #check if the messsage is not empty
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == LEA:
                connected = False        
            print (f"[{addr}] ==> {msg}")
            conn.send("msg received!".encode(FORMAT ))
    conn.close()

try:
    print ("[STARTING] server is starting...")
    start()
except KeyboardInterrupt:
    print("Bye!")

