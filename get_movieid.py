from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import re
from random import randint
from time import sleep
from imdb import IMDb
#415803
while(True):
    f1 = open('url.txt','r')
    page = get(f1.read())
    f1.close()
    #sleep(randint(1,3))
    html = bs(page.content, 'html.parser')
    x = html.find_all('div', {'class':'lister-item mode-advanced'})
    f = open("movieid.txt",'a')
    for movie in x:
        mname = movie.h3.a.get('href')
        m_id = mname.split('/tt')[-1]
        m_id = m_id.split('/')[0]
        print(m_id)
        f.write(m_id+'\n')
    f.close()
    u = html.find('div', {'class':'desc'})
    p = u.find('a', {'class':'lister-page-next next-page'})
    print(p)
    if p==None:
        print('Completed')
        break
    url = 'https://www.imdb.com' + p.get('href')
    print(url)
    f1 = open('url.txt', 'w')
    f1.write(url)
    f1.close
    

        

        
