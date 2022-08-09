import pandas
import requests
from bs4 import BeautifulSoup


titles = []
for num in range(1,27):
    url = 'https://www.web24.ir/page/63/%D9%85%D9%82%D8%A7%D9%84%D8%A7%D8%AA' + f'?page={str(num)}'
    response = requests.get(url)
    contents = response.content
    soup = BeautifulSoup(contents, 'html.parser')
    divs = soup('div', "catArticle__caption text-center")
    for div in divs:
        titles.append(div.span.string)
        print(div.span.string)

result = {'موضوع': titles
          }
data = pandas.DataFrame.from_dict(result, orient='index')
data = data.transpose()
writer = pandas.ExcelWriter('web24.xlsx')
data.to_excel(writer)
writer.save()