#!/usr/bin/env python
# coding: utf-8
import re

import requests

DATA_PATH = '/tmp/ptt_data'
CRAWL_PAGE_CNT = 10
URL_TEMPLATE = "https://www.ptt.cc/bbs/Gossiping/index{}.html"
HOST = "https://www.ptt.cc"


def get_w_cookie(url):
    """GET HTTP url with custom header containing cookie info for PTT

    Parameters
    ----------
    url : str
        PTT八卦版需要驗證年齡的URL，
        如：https://www.ptt.cc/bbs/Gossiping/index31063.html

    Returns
    -------
    Response
        Requestsµ模組的Response Object
    """
    custom_headers = {
        "cookie": "over18=1;"
    }
    resp = requests.get(url, headers=custom_headers)
    return resp


def get_total_page_cnt():
    """取得現在ptt板塊的總頁數

    Parameters
    ----------

    Returns
    -------
    int
       現在ptt板塊的總頁數
    """
    url = URL_TEMPLATE.format('')
    resp = get_w_cookie(url)

    # 這個符號
    # ‹-> &lsaquo;
    total_page_cnt = int(re.findall('href="/bbs/Gossiping/index(\d+).html">&lsaquo; 上頁', resp.text)[0]) + 1
    return total_page_cnt

def get_list_page(url):
    """GET列表頁，取得內文頁的連結們

    Parameters
    ----------
    url : str
        PTT 列表頁URL

    Returns
    -------
    list
       PTT內文頁的links
    """
    resp = get_w_cookie(url)
    links = re.findall('<a href="(/bbs/Gossiping/M.+\.html)">.+</a>', resp.text)
    detail_page_links = [HOST + link for link in links]
    return detail_page_links

def dump_page(url):
    """GET url的HTML並且寫到檔案裡

    Parameters
    ----------
    url : str
        PTT 內文頁URL

    Returns
    -------
    str
       儲存的檔案名稱
    """
    filename = "_".join(url.split('/')[-1].split('.')[:-1]) + '.html'
    resp = get_w_cookie(url)

    with open(DATA_PATH + '/' + filename, 'w') as f:
        f.write(resp.text)
    return filename

if __name__ == "__main__":
    """
    以下的code只有被單獨跑的時候才會執行
    被import的時候不會執行
    """
    total_page_cnt = get_total_page_cnt()

    for pg in range(total_page_cnt, total_page_cnt - CRAWL_PAGE_CNT, -1):
        url = URL_TEMPLATE.format(pg)
        for link in get_list_page(url):
            print(link)
            dump_page(link)

