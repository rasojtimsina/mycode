import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH'

# opens the connection and downloads html page from url
uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")


