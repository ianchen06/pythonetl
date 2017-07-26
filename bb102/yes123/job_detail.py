#!/usr/bin/env python
# coding: utf-8
import requests as r

HOST = 'https://www.yes123.com.tw/admin/'

def get_detail():
    with open('./urls_uniq.txt') as f:
        for line in f:
            URL = HOST + line.strip()
            print("[INFO] crawling %s"%URL)
            res = r.get(URL, headers={'User-Agent': ''})
            job_id = line.split("=")[-1].strip()
            print(res.status_code)
            with open('./detail_html/java_job_%s.html'%job_id, 'w') as f:
                f.write(res.text)
