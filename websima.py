import requests
from bs4 import BeautifulSoup

url = 'https://websima.com/sitemap.xml'
content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')
tag = soup.find_all('loc')
h1 = []
for link in tag:
    url2 = str(link.string)
    content2 = requests.get(url2).content
    soup2 = BeautifulSoup(content2, 'html.parser')
    tag2 = soup2.find_all('loc')
    for link2 in tag2:
        url3 = str(link2.string)
        content3 = requests.get(url3).content
        soup3 = BeautifulSoup(content3, 'html.parser')
        h1 = soup3.find('h1')
        if h1.string == 'این صفحه پیدا نشد!':
            print('')
        elif h1 == None:
            print('')
        else:
            print(h1.string)
                
