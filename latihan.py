# from ipaddress import ip_address
# import socket

# #MENGAMBIL HOSTNAME DEV
# host_name = socket.gethostname()
# print ("host name = %s" %host_name)

# #MENGAMBIL IP ADDRESS
# ip_address = socket.gethostbyname(host_name)
# print("Ip address = %s"  %ip_address)


#download
from ast import Break
import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from requests.auth import HTTPBasicAuth
import wget

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
#        self.loadPage()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Abdulatif Engine')
        pilih = input("mau 1 buka link, 2 download file, 3 cek authentikasi")
        if pilih =='1':
            while 1:
                url1 = input("masukkan link: ")
                r = requests.get(url1, allow_redirects=True,auth=HTTPBasicAuth("user", "pass"))
                if r.status_code==200:
                    self.webEngineView.setUrl(QUrl(url1))
                elif r.status_code==404:
                    with open('404.html', 'r') as f:

                        html = f.read()
                        self.webEngineView.setHtml(html)
                elif r.status_code == 403:
                    with open('403.html', 'r') as f:
                        html = f.read
                        self.webEngineView.setHtml(html)
                elif r.status_code == 500:
                    with open('500.html', 'r') as f:
                        html = f.read
                        self.webEngineView.setHtml(html)
                self.show()
        elif pilih=='2':
            url2 = "https://instagram.com/favicon.ico"
            download = requests.get(url2)
            open("instagram.ico", "wb").write(download.content)
            if download.content==True: 
                print('download berhasil!')

        elif pilih == '3':
            url3 = "https://httpbin.org/basic-auth/user/pass"
            auth = requests.get(url3, auth=HTTPBasicAuth("user", "pass"))
            print(auth)
                
def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)

#cek 404
