import requests as req
from bs4 import BeautifulSoup as bs

def getarticle(url):
    ge = req.get(url).text
    sop = bs(ge,'html.parser')
    x = sop.find_all('body')
    judul = sop.find('h1').text
    isiberita = []
    for isi in x:
        for i in isi.find_all('p'):
            isiberita.append(i.text)
    return isiberita,judul