# import requests
# import time
# import json
# import pandas


# #file_path = str(input("[!] Enter CSV file path: "))
# #urls = domain_CSV['Domain'].tolist()
# #file_path = str(input("[!] Enter file path: "))
# url = str(input("[!] Enter url: "))
# key = "0f284b06aef14c1517bbfa66478167b6c28d6d9e5136aee7b1d177181991a6b9"
# urll = "https://www.virustotal.com/api/v3/urls/id"

# param = {"apikey" : key, "resources": url}
# respond = requests.get(url=urll, params=param)
# #json_response = json.loads(respond)
# #print(json_response)
# print(respond)

import requests
import base64

link = str(input("[!] Enter url: "))
url_id = base64.urlsafe_b64encode(link.encode()).decode().strip("=")
url = "https://www.virustotal.com/api/v3/urls/" + url_id
headers = {
    "Accept": "application/json",
    "x-apikey": "0f284b06aef14c1517bbfa66478167b6c28d6d9e5136aee7b1d177181991a6b9"
}

response = requests.get(url, headers=headers)
print(url)
print(url_id)
print (response)
print(response.text)
