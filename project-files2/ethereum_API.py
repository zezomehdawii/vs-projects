import requests

# create a dictionary for each request and keep the rest as it is.
def eth_accounts():
    json_req = {"jsonrpc": "2.0", "id": 3, "method": "eth_accounts", "parmas": []} # send eth_accounts request
    req = requests.post('http://localhost:9545', json=json_req)
    print(f"Status Code: {req.status_code}, Response: {req.json()}")
    #data1 = req.json()
    #addr = ", ".join(data1["result"])
    #print ("address: " + addr)
def personal_newAccount_and_unlock():
    json_req1 = {"jsonrpc": "2.0", "id": 5, "method": "personal_newAccount", "params": ["5uper53cr3t"]}
    req1 = requests.post('http://localhost:9545', json=json_req1)
    #print(f"Status Code: {req1.status_code}, Response: {req1.json()}")
    data = req1.json()
    addr = "".join(data["result"])
    json_req2 = {"jsonrpc": "2.0", "id": 6, "method": "personal_unlockAccount", "params": [addr, "5uper53cr3t"] }
    req2 = requests.post('http://localhost:9545', json=json_req2)
    #print(f"Status Code: {req2.status_code}, Response: {req2.json()}")
    return addr





############################################################
#print (type(data1))
#result = r.json()
#print(json.dumps(result, sort_keys=True, indent=4))
#data2 = json.dumps(req.json())
#print (type(data2))
#print (data2)
#jsonResult = json.loads(data2)
#print (type(jsonResult))
#print(jsonResult["result"])
#addr = (jsonResult["result"])
#print (addr)
#addr = addr.replace(r"[\[']","")
#addr = str(addr)
#print (addr)
#print (re.sub(r"[\[]", "", addr))
#print(re.sub(r"[\]]", "", addr))
