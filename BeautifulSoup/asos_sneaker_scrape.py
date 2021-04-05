# tutorial1:https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup
# tutorial2: https://www.journaldev.com/44473/scrape-amazon-product-information-beautiful-soup

# imports
import requests
import bs4 as bs

# defining an user agent
agent = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
agent2 = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'})

# get web page as soup object
url = "https://www.asos.com/de/herren/schuhe-stiefel-sneaker/sneaker/cat/?cid=5775&nlid=mw|schuhe|nach+produkt+shoppen|sneaker"
webpage = requests.get(url, headers = agent2)
soup = bs.BeautifulSoup(webpage.content,'lxml')

# get all items
article_containers = soup.find_all("article")
article = article_containers[0]

# open csv-file
f = open("asos_sneaker.csv","w")
headers = "id, name, price, link\n"
f.write(headers)

# loop over all items and write to csv
for article in article_containers:
    product_id = article['id']
    temp = article.a['aria-label'].split("; Preis: ")
    product_name = temp[0]
    product_price = temp[1]
    product_url = article.a['href']
    f.write(product_id + ", " + product_name + ", " +
    product_price.replace(",",".") + ", " +  product_url + "\n")

f.close()
