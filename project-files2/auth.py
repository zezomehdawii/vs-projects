import hashlib
import scapy.all
import json
from netfilterqueue import NetfilterQueue
from web3 import Web3
##################################################
##Blockchain Info                               ##
blockchainNetworkIP = ""
web3 = Web3.HTTPProvider(blockchainNetworkIP)
jsonArray = ""
abi = json.loads(jsonArray)
contractAddress = ""
address = web3.toChecksumAddress(contractAddress)
contract = web3.eth.contract(address=address, abi=abi)
##End of Infor                                  ##
##################################################

deviceID = ""


def authFunc(packet):
    #ip = input("input device IP: ")
    #mac = input("input device MAC: ")
    pkt = IP(packet.get_payload())##
    packet.set_payl9oad(str(pkt))##
    print ("pkt: " + dir(pkt))## # dir return all the variables and methods of the called parameter
    print ("packet: " + dir(packet))##

    if IP in pkt:
        ip = pkt[IP].src
        mac = packet.get_hw()
    deviceID = hashlib.md5((ip + mac + "saltValue").encode('utf-8')).hexdigest()
    print (deviceID) ##
    if(contract.functions.authFunc(deviceID).call):
        print ("Sender is autherized!")
        packet.accept()
    else: 
        print ("sender is not autherized")
        packet.drop()
    


nfqueue = NetfilterQueue()
nfqueue.bind(1, authFunc)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print("Error")