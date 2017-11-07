#!/usr/bin/env python
import re
import os

import requests

HOST = "https://www.ptt.cc"
URL_TPL = "https://www.ptt.cc/bbs/Gossiping/index%s.html"
PG_TO_CRAWL = 5

resp = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html", headers={'cookie': 'over18=1'})

total_page = int(re.findall('/bbs/Gossiping/index(\d+).html', resp.text)[-1]) + 1

for pg in range(total_page, total_page - PG_TO_CRAWL, -1):
    url = URL_TPL%pg
    print(url)
    resp = requests.get(url, headers={'cookie': 'over18=1'})
    articles = re.findall('/bbs/Gossiping/M.+\.html', resp.text)
    for link in [HOST + link for link in articles]:
        resp = requests.get(link,  headers={'cookie': 'over18=1'})
        with open('./data/%s'%(os.path.basename(link)), 'w') as f:
            f.write(resp.text)

