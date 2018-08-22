#!/usr/bin/python3
from os import system
from random import choice
from re import findall
from datetime import datetime

from requests import get
from bs4 import BeautifulSoup

def get_proxy():
    html = get('https://free-proxy-list.net/anonymous-proxy.html').text
    soup = BeautifulSoup(html, 'html.parser')
    proxy_arr = []
    ts = datetime.today().strftime('%d-%m-%Y')
    fname = 'proxies_'+ts+'.txt'

    for td in soup.find_all('tr'):
        td_data = (findall('>(.*?)<',str(td)))
        for i in td_data:
            if i == '':
                td_data.remove(i)
            else:
                continue

        if len(td_data) < 8:
            continue
        else:
            proxy_arr.append(td_data)
            file_data = str(datetime.now()).split('.',1)[0]+'\t'+str(td_data)+'\n'
            with open(fname,'a+') as f:
                f.write(file_data)

    proxy_arr.pop(0)
    proxy = choice(proxy_arr)
    proxy = {'ip_addr':proxy[0], 'port':proxy[1], 'code':proxy[2],
              'country':proxy[3], 'anon_level':proxy[4], 'google':proxy[5],
              'https':proxy[6], 'last_checked':proxy[7]}

    return proxy

proxy = get_proxy()
print(proxy)
