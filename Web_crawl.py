import requests
from bs4 import BeautifulSoup
import Open_url


# search on google and open the first link appeared
def get_url(query):
    source_code = requests.get(query).text
    soup = BeautifulSoup(source_code, 'html.parser')
    # print(soup.prettify())
    content = []
    for each_text in soup.findAll('div', {'class': 'BNeawe UPmit AP7Wnd'}):
        content.append(each_text.text)

    link = content[0]
    # print(link)
    Open_url.open(link)


# get_url('https://www.google.com/search?q=youtube')
