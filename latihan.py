from ipaddress import ip_address
import socket

#MENGAMBIL HOSTNAME DEV
host_name = socket.gethostname()
print ("host name = %s" %host_name)

#MENGAMBIL IP ADDRESS
ip_address = socket.gethostbyname(host_name)
print("Ip address = %s"  %ip_address)

#download
import requests
url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)