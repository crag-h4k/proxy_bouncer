#!/usr/bin/python3
from os import system
from random import choice
from re import findall
from datetime import datetime

from requests import get
from bs4 import BeautifulSoup
class proxy:
    def __init__(self, ip_addr, port, code, country, anon_level, google, https, last_checked):
        self.ip_addr = ip_addr
        self.port = port
        self.code = code
        self.country = country
        self.anon_level = anon_level
        self.google = google
        self.https = https
        self.last_checked = last_checked

def get_proxy(log=False):
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
            if log == True:
                file_data = str(datetime.now()).split('.',1)[0]+'\t'+str(td_data)+'\n'
                with open(fname,'a+') as f:
                    f.write(file_data)

    proxy_arr.pop(0)
    p = choice(proxy_arr)
    P = proxy(ip_addr = p[0], port = p[1], code = p[2], country = p[3],anon_level = p[4], google = p[5], https = p[6], last_checked = p[7])

    return P

#proxy = get_proxy()
#print(proxy)
