import requests
import sys


#url = 'http://172.21.128.1:5000/'
url = 'http://service2-web-page:5000'
message = requests.get(url).text
myobj = {'md5': message}
#x = requests.post(url, json = myobj)
