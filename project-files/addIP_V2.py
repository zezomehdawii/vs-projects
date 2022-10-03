import os
from netfilterqueue import NetfilterQueue
from scapy.all import *


def get_IP_and_add_device(packet):
    pkt = IP(packet.get_payload())
    packet.set_payload(str(pkt))
    print ("pkt: " + dir(pkt)) # dir return all the variables and methods of the called parameter
    print ("packet: " + dir(packet))
    if IP in pkt:
        ip_src = pkt[IP].src
        mac_src = packet.get_hw()
    print (f"[*] IP Detected: {str(ip_src)}")
    
    with open("ip_list.txt","r") as fr:
        iplist = fr.read()
        with open("ip_list.txt","w") as fw:
            while True:
                new_ip = ip_src
                choice = input(f"Do you want to confirm the IP [{new_ip}] and MAC [{}] ? y/n: ")
                if choice == "n": 
                    fw.write(iplist) 
                    print ("<++ [ADDED!] ++>")
                    packet.drop()
                    break
                if new_ip not in iplist: 
                    if len(iplist) == 0 : iplist = iplist + new_ip 
                    else: iplist = iplist + "," + new_ip
                    print ("<++ [ADDED!] ++>")
                    packet.drop()
                    break
                else: 
                    print (f"The entered IP [{new_ip}] is already exists!")
                    packet.drop()
                    break   

    

os.system("sudo iptables -F")
os.system("sudo iptables -t nat -F")
os.system("sudo iptables -t nat -A INPUT -j NFQUEUE --queue-num 2")
addnfqueue = NetfilterQueue()
addnfqueue.bind(2, get_IP_and_add_device)
try:
    addnfqueue.run()
except KeyboardInterrupt:
    print("Erorr")


