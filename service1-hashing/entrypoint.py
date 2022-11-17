import requests
import sys
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print(IPAddr)


url = 'http://172.21.128.1:5000/'
message = requests.get(url).text
myobj = {'md5': message}
#x = requests.post(url, json = myobj)
