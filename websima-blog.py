import pandas
import requests
import datetime
from bs4 import BeautifulSoup
start = datetime.datetime.now()
titles = []
for num in range(1, 30):
    url = f'https://websima.com/blog/page/{str(num)}/'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    h2 = soup.find_all('h2')
    for h in h2:
        titles.append(h.a.string)
print(titles)
data = {}
for title in titles:
    url = f'https://www.google.com/search?q={title}'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    h3 = soup.find_all('h3')
    list = []
    for h in h3:
        list.append(h.string)
    data[title] = list

data = pandas.DataFrame.from_dict(data, orient='index')
data = data.transpose()
writer = pandas.ExcelWriter('websima-blog.xlsx')
data.to_excel(writer)
writer.save()
end = datetime.datetime.now()
print(f'duration : {end-start}')
