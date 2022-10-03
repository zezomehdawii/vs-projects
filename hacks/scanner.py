from ctypes import sizeof
import socket
from tkinter.tix import NoteBook
from termcolor import colored
import optparse
from threading import * 

socket.setdefaulttimeout(2)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    parser = optparse.OptionParser("Usage of program:" + "-H <target host ip> -p <target port or ports>")
    parser.add_option("-H",dest="targetHost", type="string", help="specify target host")
    parser.add_option("-p",dest="targetPort", type="int", help="specify target port")
    (options,args) = parser.parse_args()
    targetHost = options.targetHost
    targetPort = options.targetPort
    if (targetHost == None or targetPort == None):
        print (parser.usage)
        exit(0)
    else:
        t = Thread(target=portScanner, args=(targetHost,int(targetPort)))
        t.start()


def portScanner(host, port):
    if sock.connect_ex((host,port)):
        print (colored(f"[!!] port {port} is closed!", "red"))
    else:
        print (colored(f"[+] port {port} is open!", "green"))

if __name__ == "__main__":
    main()


