# code to get the host ip address and turn the last oct to 0 with netmask
# not added yet to the main code!
import socket    

host_name = socket.gethostname()    
IPAddress = socket.gethostbyname(host_name)    
#print("Your Computer Name is:" + host_name)    
#print("Your Computer IP Address is:" + IPAddress) 
hostIP = IPAddress 
hostIP = hostIP[:hostIP.rfind('.')+1] + '0' + "/24"
#print (hostIP)