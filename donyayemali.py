import pandas
import requests
from bs4 import BeautifulSoup

a_titles = []
a_links = []
for i in range(1, 7):
    url = f'https://donyayemali.com/category/%d9%85%d8%b7%d8%a7%d9%84%d8%a8-%d8%a2%d9%85%d9%88%d8%b2%d8%b4%db%8c/page/{str(i)}/'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find_all('h2', 'title')
    for link in title:
        if 'donyayemali.com' in link.a['href']:
            a_links.append(link.a.get('href'))
            a_titles.append(link.a.string.strip())

c_titles = []
c_links = []
for i in range(1, 5):
    i = str(i)
    url = 'https://donyayemali.com/product-category/%d8%af%d9%88%d8%b1%d9%87-%d8%a2%d9%85%d9%88%d8%b2%d8%b4%db%8c/' + f'page/{i}/'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser', multi_valued_attributes=None)
    title = soup.find_all('a')
    for x in title:
        try:
            if '/product/' in x['href']:
                c_links.append(x['href'])
                c_titles.append(x.h2.string.strip())
        except:
            continue
c_titles.append('0')
# print(len(set(a_links)))
# print(len(set(a_titles)))
# print(len(set(c_links)))
# print(len(set(c_titles)))
data = {'عنوان دوره': list(set(c_titles)), 'لینک دوره': list(set(c_links))}
df = pandas.DataFrame(data, columns=['عنوان دوره', 'لینک دوره'])
# data = data.transpose()
# writer = pandas.ExcelWriter('donyayemali.xlsx')
# data.to_excel(writer)
# writer.save()
df.to_csv('donyayemali_courses.csv', index=False)
