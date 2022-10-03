import hashlib
from scapy.all import *
import json
import os
from eth_API import *
from netfilterqueue import NetfilterQueue
from web3 import Web3

##################################################
##                Blockchain Info               ##
blockchainNetworkIP = "127.0.0.1:9545"
web3 = Web3(Web3.HTTPProvider(blockchainNetworkIP))
jsonArray = '[{"constant":false,"inputs":[{"internalType":"string","name":"_hash_id","type":"string"}],"name":"Activate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_addr","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_hash_id","type":"string"}],"name":"add_device","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"_hash_id","type":"string"}],"name":"authFunc","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_hash_id","type":"string"}],"name":"deActivate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"device","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"hash_id","type":"string"},{"internalType":"enum BlockChanger.State","name":"device_state","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"deviceCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"device_addresses","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]'
abi = json.loads(jsonArray)

contractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138"
address = web3.toChecksumAddress(contractAddress)
contract = web3.eth.contract(address=address, abi=abi)
##################################################


def addDevice(packet):
    pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string
    #print ("packet (before get_payload function): " + dir(packet))
    #print ("pkt (after get_payload function): " + dir(pkt)) # dir return all the variables and methods of the called parameter
    iplist = ""
    addr = ""
    deviceID = ""
    deviceName = ""

    if IP in pkt:
        ip_src = pkt[IP].src
        #mac_src = packet.get_hw() #function by nfqueue gives hex data
        mac_src = getmacbyip(str(ip_src)) #funtion by scapy
    print (f"[*] Device Detected!: [{str(ip_src)}] [{mac_src}]")
    print("-----------------------------------------------------------------------------------------")
    
    choice = input(f"Do you want to confirm the IP [{ip_src}] and MAC [{mac_src}] ? y/n: ")
    if choice == "y":
        with open("ip_list.txt","r") as fr:
            iplist = fr.read()
            with open("ip_list.txt","w") as fw:
                while True:
                    if ip_src not in iplist:
                        if len(iplist) == 0: 
                            iplist = iplist + ip_src 
                        else: 
                            iplist = iplist + "," + ip_src
                        
                        fw.write(iplist)
                        addr = personal_newAccount_and_unlock() # return the new address
                        deviceName = input("Enter device Name: ") # get device name
                        deviceID = hashlib.md5((ip_src + mac_src + "saltValue").encode('utf-8')).hexdigest()# calculate the id
                        contract.functions.add_device(addr, deviceName, deviceID).transact() # store the id to the blockchain
                        print ("<++ [ADDED!] ++>")
                        packet.drop()
                        break
                    else: 
                        choice = input(f"The connected device [{ip_src}] [{mac_src}] is already exists!\n do you want to add another device? y/n: ")
                        packet.drop()
                        if choice == "n":
                            break
                        else:
                            print ("[*] waiting for device to be connected!")    



os.system("sudo iptables -F")
os.system("sudo iptables -I INPUT -s 192.168.100.0/24 -j NFQUEUE --queue-num 2")

addnfqueue = NetfilterQueue()
addnfqueue.bind(2, addDevice)
try:
    print ("[*] waiting for device to be connected!")
    print ("Note that the traffic on the network will be on hold while you are running this function!")
    print ("-----------------------------------------------------------------------------------------")
    addnfqueue.run()
except KeyboardInterrupt:
    print("/nError!")