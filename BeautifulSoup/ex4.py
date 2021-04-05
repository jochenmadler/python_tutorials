# tutorial from: https://pythonprogramming.net/javascript-dynamic-scraping-parsing-beautiful-soup-tutorial/?completed=/tables-xml-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source,'lxml')

js_test = soup.find('p', class_='jstest')
print(js_test.text) # this is the default text which would be dynamically altered when opening the page in a web browser. The browser would run the javascript.

# use PyQt4 to mimic a browser client
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl
import bs4 as bs
import urllib.request

# try out Qt, tutorial from: https://zetcode.com/gui/pyqt5/firstprograms/
def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 500)
    w.move(300, 300)
    w.setWindowTitle('Alert!!')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# import does not work and raises an error?
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Client(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)



