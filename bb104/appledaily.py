"""
    Apple Daily Crawler

    author: Ian Chen <ianchen06@gmail.com>
"""
import re
import csv

import requests 
from bs4 import BeautifulSoup

DOMAIN = "http://www.appledaily.com.tw"

f = open('./data.csv', 'w')
headers = ['title', 'dt', 'content', 'view_count']
writer = csv.DictWriter(f, fieldnames=headers)

writer.writeheader()

def article_crawler(url):
    """
    Crawls article url, and extract fields

    args:
        url <str>: article url

    return:
        article_dict <dict>: artilce dict with fields
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html5lib')

    article = {}
    article['title']   = soup.select_one('#h1').text.replace('\u3000',' ').strip()
    article['dt']      = soup.select_one('div.gggs > time').text.strip()
    article['content'] = soup.select_one('#summary').text.strip()

    if soup.select_one('div.urcc > a.function_icon.clicked'):
        article['view_count'] = int(re.findall('\d+', soup.select_one('div.urcc > a.function_icon.clicked').text)[0])
    else:
        article['view_count'] = 0
    writer.writerow(article)
    f.flush() # Flush here so we don't loose data on exception
    return article

def list_crawler(pg=5):
    """
    Cralers appledaiy's realtime news

    args:
        pg <int>: number of pages to crawl
    """
    url = DOMAIN + "/realtimenews/section/new/%s"

    article_data = []

    for p in range(1,pg+1):
        print("[INFO] crawling %s"%url%p)
        resp = requests.get(url%p)
        urls = [DOMAIN + x for x in re.findall('href="(/realtimenews/article/.*/.*/.*/.+)" target', resp.text)]
        for article_url in urls:
            article_data.append(article_crawler(article_url))

if __name__ == "__main__":
    list_crawler(1)

