# coding: utf-8
import sys
import datetime

from pymongo import MongoClient
import pymongo
import requests
import json

start_date = sys.argv[1]
days = int(sys.argv[2])

conn = MongoClient()

for day in range(1,days + 1):
    dstr = (datetime.datetime.strptime(start_date,'%Y%m%d') - datetime.timedelta(days=day)).strftime("%Y%m%d")

    print("[DEBUG] Requesting %s"%dstr)
    url = "https://trends.google.com/trends/hottrends/hotItems"
    data = {
        "ajax": "1",
        "pn": "p12",
        "htd": dstr,
        "htv": "l"
    }

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "cache-control": "no-cache",
        "content-length": "32",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://trends.google.com",
        "pragma": "no-cache",
        "referer": "https://trends.google.com/trends/hottrends",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    resp = requests.post(url, data=data, headers=headers)
    data = resp.json()
    print("[INFO] %s"%data.get('oldestVisibleDate'))
    data['_id'] = data.get('oldestVisibleDate')

    # conn.<db_name>.<table_name>.<operation>
    try:
        res = conn.crawler.google_trends.insert(data)
        print("[INFO] Inserted id %s"%res)
    except pymongo.errors.DuplicateKeyError as e:
        print(e)
        print("[INFO] %s exists, skipping"%data['_id'])
