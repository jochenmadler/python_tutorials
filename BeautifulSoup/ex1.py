# Tutorial from: https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
# sample page for scraping: https://pythonprogramming.net/parsememcparseface/

# html structure: https://www.w3schools.com/html/html_intro.asp

from ssl import ALERT_DESCRIPTION_USER_CANCELLED
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
print(source)

# create beautiful soup object
soup = bs.BeautifulSoup(source,'lxml')
print(soup)

# print common html stuff
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)

# get all paragraphs
for paragraph in soup.find_all('p'): # p: paragraph
    print(paragraph.string) # if there a child tags in the paragraph, string retruns None.
    print(str(paragraph.text)) # text always returns all content of the paragraph as unicode text.

# grap links (urls) of a website
for url in soup.find_all("a"):
    print(url.get('href'))