from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import requests
from requests.auth import HTTPBasicAuth

class hyperlink(QLabel):
    def __init__(self, parent:None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()

        self.window = QWidget()
        self.window.setWindowTitle("ABDULATIF ENGINE")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton('Go')
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        
        #self.youtube = QLabel('youtube')
        #self.youtube.setMinimumHeight(30)
        self.youtube = QPushButton('youtube')

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.youtube)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        #self.youtube.
        self.youtube.clicked.connect(lambda: self.browser.setUrl(QUrl("http://youtube.com")))

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        
        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        
        self.cek(url)
        # self.browser.setUrl(QUrl(url))
    
    def cek(self, urlcek):
        username = "fasijardiq@gmail.com"
        password = "11Sandaljepit"

        r = requests.get(urlcek, allow_redirects=True, auth=HTTPBasicAuth('user', 'pass'))
        if r.status_code == 200:
            self.browser.setUrl(QUrl(urlcek))
        elif r.status_code == 404:
            with open('404.html', 'r') as f:
                html = f.read
                self.browser.setHtml(html)
        elif r.status_code == 403:
            with open('403.html', 'r') as f:
                html = f.read
                self.browser.setHtml(html)
        elif r.status_code == 500:
            with open('500.html', 'r') as f:
                html = f.read
                self.browser.setHtml(html)

    #def loadpage(self):
        


app = QApplication([])
window = WebBrowser()
app.exec_()


