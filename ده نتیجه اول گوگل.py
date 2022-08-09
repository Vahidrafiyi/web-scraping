import pandas
from googlesearch import search


def search_results(query, number, file_name, advanced=True):
    titles = []
    urls = []
    for title in search(query, num_results=number, advanced=advanced):
        titles.append(title.title)
        # urls.append(title.url.split('/')[2])
        urls.append(title.url)
    dict_show = {'URL': urls, 'TITLE': titles}
    data = pandas.DataFrame.from_dict(dict_show, orient='index')
    data = data.transpose()
    excel = pandas.ExcelWriter(f"{file_name}.xlsx")
    data.to_excel(excel)
    excel.save()


search_results('Python', 10, 'python2')
