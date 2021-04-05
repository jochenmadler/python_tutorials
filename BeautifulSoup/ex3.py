# tutorial from: https://pythonprogramming.net/tables-xml-scraping-parsing-beautiful-soup-tutorial/?completed=/navigating-pages-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

# get table - this website has only one
table = soup.find("table") # here, find_all() is not possible - why?

# get all rows
table_rows = table.find_all("tr")

# iterate through rows and find data tags (td) for each
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

# better option for parsing tables: pandas
import pandas as pd

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs: # here, there is only on df -> len(dfs) = 1
    print(df) # you could simply call print(dfs) instead

# parse XML
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read() # we are grabbing the sitemap now
soup = bs.BeautifulSoup(source,'xml') # here is the difference

# get all urls
urls = soup.find_all("loc")
for url in urls:
    print(url.text)

