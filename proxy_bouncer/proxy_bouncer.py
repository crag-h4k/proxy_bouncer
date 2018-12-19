#!/usr/bin/python3
from os import system
from random import choice
from re import findall
from datetime import datetime

from requests import get
from bs4 import BeautifulSoup

class Proxy:
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
    P = choice(proxy_arr)
    P = Proxy(ip_addr = P[0], port = P[1], code = P[2], country = P[3],anon_level = P[4], google = P[5], https = P[6], last_checked = P[7])

    return P
if __name__ == '__main__':
    Proxy = get_proxy()
    print(Proxy)
