import requests
from bs4 import BeautifulSoup
import re
import random

def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img = soup.find_all('a', href=re.compile('.mp4$'))
    print(img)
    for src in img:
        name = random.randint(1, 1000)
        link = src.get('href')
        with requests.get(link, stream=True) as request:
            with open(str(name)+'.mp4', 'wb') as image:
                for photo in request.iter_content(chunk_size=1024):
                    image.write(photo)

download('https://video.varzesh3.com/video/250044/%D8%A7%D8%AE%D8%B1%D8%A7%D8%AC-%D8%AC%D9%86%D8%AC%D8%A7%D9%84%DB%8C-%D9%87%D9%85%D8%B2%D9%85%D8%A7%D9%86-%D8%AF%D9%88-%D8%A8%D8%A7%D8%B2%DB%8C%DA%A9%D9%86-%D8%A8%D9%88%D9%84%D9%88%D9%86%DB%8C%D8%A7-%D9%85%D9%82%D8%A7%D8%A8%D9%84-%DB%8C%D9%88%D9%88%D9%86%D8%AA%D9%88%D8%B3')