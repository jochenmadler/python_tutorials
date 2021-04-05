# tutorial from: https://pythonprogramming.net/navigating-pages-scraping-parsing-beautiful-soup-tutorial/?completed=/introduction-scraping-parsing-beautiful-soup-tutorial/

# imports
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

# get navigation bar
nav = soup.nav

# get urls only from navigation
for url in nav.find_all('a'):
    print(url.get('href'))

# get body
body = soup.body

# get text from body
for p in body.find_all('p'):
    print(p.text)

# find div's only in class body
for div in soup.find_all("div", class_="body"):
    print(div.text)
