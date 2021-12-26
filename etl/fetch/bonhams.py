from logging import log
import bs4

from requests.api import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import os
from bs4 import BeautifulSoup
import json
import os
import multiprocessing
import parmap
from uncurl import parse
from time import sleep
from urllib.parse import urljoin
from multiprocessing import Manager
import json
import os
import uncurl
import json
from math import ceil
num_cores = multiprocessing.cpu_count() 

# 참고
# https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html

chrome_driver_path = r'D:\Programming\artpassion\aucetl\chromedriver.exe'

curl_list = '''curl 'https://www.bonhams.com/api/v1/search_json/?content=sale&date_range=past&exclude_sale_type=3&length=12&page=1&randomise=False' \
  -H 'authority: www.bonhams.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'x-newrelic-id: VQAOWVNSChAFUlhSBgAFVw==' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bonhams.com/' \
  -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: csrftoken=d7nu8pPYHoqNX25HKYgFRoD3Mf3Ru5wAtCPmZYrxPy5UTcIWYDcG1fmDSWQ0vKOe; sessionid=6vio9dpk9wu355ai4cve5uf2qr0o3c5f; _gcl_au=1.1.1200473760.1640157175; _ga=GA1.2.1028556115.1640157176; _gid=GA1.2.456626654.1640157176; _evga_520c={%22uuid%22:%2235fd447efffc7b61%22}; _fbp=fb.1.1640157176230.1522378618; _hjFirstSeen=1; _hjSession_534403=eyJpZCI6IjQ1NmVkNmE0LTNmNmYtNDMwMC04OTlmLTkyZTQzMDQ4ZGUzNyIsImNyZWF0ZWQiOjE2NDAxNTcxNzY5Mjh9; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; _hjSessionUser_534403=eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==; userDissmissCookieBox=agree; __atuvc=2%7C51; __atuvs=61c2d1cec2241f00001; _dc_gtm_UA-3400662-1=1; _dc_gtm_UA-48397636-1=1' \
  -H 'if-none-match: W/"4d5f11146a570c9fcfb823d4ee7449e0"' \
  --compressed
'''

print(parse(curl_list))


curl_lot = '''curl 'https://www.bonhams.com/api/v1/lots/26784/?category=list&length=12&minimal=false&page=1' \
  -H 'authority: www.bonhams.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'x-newrelic-id: VQAOWVNSChAFUlhSBgAFVw==' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bonhams.com/' \
  -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: csrftoken=d7nu8pPYHoqNX25HKYgFRoD3Mf3Ru5wAtCPmZYrxPy5UTcIWYDcG1fmDSWQ0vKOe; _gcl_au=1.1.1200473760.1640157175; _ga=GA1.2.1028556115.1640157176; _evga_520c={%22uuid%22:%2235fd447efffc7b61%22}; _fbp=fb.1.1640157176230.1522378618; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; _hjSessionUser_534403=eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==; userDissmissCookieBox=agree; sessionid=sd1czd8r1pk5sbphnw95ply2qspvp8c1; _gid=GA1.2.1827316181.1640477046; _dc_gtm_UA-3400662-1=1; _dc_gtm_UA-48397636-1=1; _hjSession_534403=eyJpZCI6ImIxMTIzY2M2LTVkNTYtNDQxNC05YzA0LWQzNDFhYTMzNzYyZCIsImNyZWF0ZWQiOjE2NDA0NzcwNjAxMzV9; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; __atuvc=2%7C51%2C1%7C52; __atuvs=61c7b195a805129a000' \
  --compressed
'''

print(parse(curl_lot))


curl_online_lot = '''curl 'https://api01.bonhams.com/api/search/auction/27658/?page=1&page_size=12' \
  -H 'authority: api01.bonhams.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'origin: https://www.bonhams.com' \
  -H 'sec-fetch-site: same-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bonhams.com/' \
  -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  --compressed'''

print(parse(curl_online_lot))

curl_public_lot = '''curl 'https://www.bonhams.com/api/v1/lots/26784/?category=list&length=12&minimal=false&page=1' \
  -H 'authority: www.bonhams.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'x-newrelic-id: VQAOWVNSChAFUlhSBgAFVw==' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bonhams.com/' \
  -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: csrftoken=d7nu8pPYHoqNX25HKYgFRoD3Mf3Ru5wAtCPmZYrxPy5UTcIWYDcG1fmDSWQ0vKOe; _gcl_au=1.1.1200473760.1640157175; _ga=GA1.2.1028556115.1640157176; _evga_520c={%22uuid%22:%2235fd447efffc7b61%22}; _fbp=fb.1.1640157176230.1522378618; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; _hjSessionUser_534403=eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==; userDissmissCookieBox=agree; sessionid=sd1czd8r1pk5sbphnw95ply2qspvp8c1; _gid=GA1.2.1827316181.1640477046; _hjSession_534403=eyJpZCI6ImIxMTIzY2M2LTVkNTYtNDQxNC05YzA0LWQzNDFhYTMzNzYyZCIsImNyZWF0ZWQiOjE2NDA0NzcwNjAxMzV9; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; _dc_gtm_UA-3400662-1=1; _dc_gtm_UA-48397636-1=1; __atuvc=2%7C51%2C6%7C52; __atuvs=61c7b195a805129a005' \
  -H 'if-none-match: W/"c2122a8c4d28c54d099615ae329ef95b"' \
  --compressed
'''

print(parse(curl_public_lot))

curl_fixed_lot ='''
curl 'https://www.bonhams.com/api/v1/lots/27674/?category=list&length=12&minimal=false&page=1' \
  -H 'authority: www.bonhams.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'x-newrelic-id: VQAOWVNSChAFUlhSBgAFVw==' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.bonhams.com/' \
  -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: csrftoken=d7nu8pPYHoqNX25HKYgFRoD3Mf3Ru5wAtCPmZYrxPy5UTcIWYDcG1fmDSWQ0vKOe; _gcl_au=1.1.1200473760.1640157175; _ga=GA1.2.1028556115.1640157176; _evga_520c={%22uuid%22:%2235fd447efffc7b61%22}; _fbp=fb.1.1640157176230.1522378618; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; _hjSessionUser_534403=eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==; userDissmissCookieBox=agree; _gid=GA1.2.1827316181.1640477046; sessionid=zxb2b4t5kapbrtqhoso3ql9qevnhyn1i; _hjSession_534403=eyJpZCI6IjY0MzZhYjVmLTRkNDgtNGJkNS05ZDMyLTIwNTVkYzNmYjNhMCIsImNyZWF0ZWQiOjE2NDA0OTExMjU2MDB9; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; _dc_gtm_UA-3400662-1=1; _dc_gtm_UA-48397636-1=1; __atuvc=2%7C51%2C8%7C52; __atuvs=61c7e8b23442eccb001' \
  -H 'if-none-match: W/"f68449653641807d08991f90746a624a"' \
  --compressed
'''
print(parse(curl_fixed_lot))


#headless driver 생성
def getHeadlessChromeDriver():
  try:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("lang=ko_KR") # 한국어!
    driver = webdriver.Chrome('chromedriver', chrome_options=options)  
    driver.get('about:blank')
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
    return driver
  except Exception as e:
    print(e)
    raise e

def getSessionCookie():
  try:
    url = 'https://www.bonhams.com/results/'
    driver = getHeadlessChromeDriver()
    driver.get(url)
    cookies = driver.get_cookies()
    session_cookie = dict()
    for cookie in cookies:
        print('name : ',cookie['name'],'value : ',cookie['value'],'\n')
        session_cookie[cookie['name']] = cookie['value']
    driver.close()
    return session_cookie
  except Exception as e:
    raise e



def getAuctionList(cookie:dict,length:int,page:int,getcnt:bool=False):
  res = requests.get(f"https://www.bonhams.com/api/v1/search_json/?content=sale&date_range=past&exclude_sale_type=3&length={length}&page={page}&randomise=False",
    headers={
        "accept": "application/json, text/plain, */*",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "authority": "www.bonhams.com",
        "if-none-match": "W/\"4d5f11146a570c9fcfb823d4ee7449e0\"",
        "referer": "https://www.bonhams.com/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "x-newrelic-id": "VQAOWVNSChAFUlhSBgAFVw=="
    },
    cookies={
        "__atuvc": "2%7C51",
        "__atuvs": "61c2d1cec2241f00001",
        "_dc_gtm_UA-3400662-1": "1",
        "_dc_gtm_UA-48397636-1": "1",
        "_evga_520c": "{%22uuid%22:%2235fd447efffc7b61%22}",
        "_fbp": "fb.1.1640157176230.1522378618",
        "_ga": "GA1.2.1028556115.1640157176",
        "_gcl_au": "1.1.1200473760.1640157175",
        "_gid": "GA1.2.456626654.1640157176",
        "_hjAbsoluteSessionInProgress": "0",
        "_hjFirstSeen": "1",
        "_hjIncludedInSessionSample": "1",
        "_hjSessionUser_534403": "eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==",
        "_hjSession_534403": "eyJpZCI6IjQ1NmVkNmE0LTNmNmYtNDMwMC04OTlmLTkyZTQzMDQ4ZGUzNyIsImNyZWF0ZWQiOjE2NDAxNTcxNzY5Mjh9",
        "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
        "csrftoken": cookie['csrftoken'],
        "sessionid": cookie['sessionid'],
        "userDissmissCookieBox": "agree"
    },
    auth=(),
)
  res.status_code
  j = json.loads(res.text)
  mr = j['model_results']
  return mr['sale']['total_count'] if getcnt else mr['sale']['items']






def getLotDetail(auction:dict,cookie):
  # from urllib.parse import urljoin 
  # base_path = 'https://www.bonhams.com'
  # auction = auction_list[0]
  url_suffix_path = auction['url']
  #auction_url = urljoin(base_path,url_suffix_path)
  auction_type = auction['sale_type']
  sale_no = auction['iSaleNo']
  if auction_type =='PUBLIC':
    lot_res = requests.get(f"https://www.bonhams.com/api/v1/lots/{sale_no}]/?category=list&length=1000&minimal=false&page=1",
        headers={
            "accept": "application/json, text/plain, */*",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "authority": "www.bonhams.com",
            "referer": "https://www.bonhams.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "x-newrelic-id": "VQAOWVNSChAFUlhSBgAFVw=="
        },
        cookies={
            "__atuvc": "2%7C51%2C1%7C52",
            "__atuvs": "61c7b195a805129a000",
            "_dc_gtm_UA-3400662-1": "1",
            "_dc_gtm_UA-48397636-1": "1",
            "_evga_520c": "{%22uuid%22:%2235fd447efffc7b61%22}",
            "_fbp": "fb.1.1640157176230.1522378618",
            "_ga": "GA1.2.1028556115.1640157176",
            "_gcl_au": "1.1.1200473760.1640157175",
            "_gid": "GA1.2.1827316181.1640477046",
            "_hjAbsoluteSessionInProgress": "0",
            "_hjIncludedInSessionSample": "1",
            "_hjSessionUser_534403": "eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==",
            "_hjSession_534403": "eyJpZCI6ImIxMTIzY2M2LTVkNTYtNDQxNC05YzA0LWQzNDFhYTMzNzYyZCIsImNyZWF0ZWQiOjE2NDA0NzcwNjAxMzV9",
            "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
            "csrftoken": cookie['csrftoken'],
            "sessionid": cookie['sessionid'],
            "userDissmissCookieBox": "agree"
        },
        auth=(),
    )
  elif auction_type == 'ONLINE':        
    #online
    lot_res = requests.get(f"https://api01.bonhams.com/api/search/auction/{sale_no}/?page=1&page_size=1000",
        headers={
            "accept": "application/json, text/plain, */*",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "authority": "api01.bonhams.com",
            "origin": "https://www.bonhams.com",
            "referer": "https://www.bonhams.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        },
        cookies={},
        auth=(),
    )
  elif auction_type =='FIXED':
    lot_res = requests.get(f"https://www.bonhams.com/api/v1/lots/{sale_no}/?category=list&length=1000&minimal=false&page=1",
      headers={
          "accept": "application/json, text/plain, */*",
          "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
          "authority": "www.bonhams.com",
          "if-none-match": "W/\"f68449653641807d08991f90746a624a\"",
          "referer": "https://www.bonhams.com/",
          "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
          "x-newrelic-id": "VQAOWVNSChAFUlhSBgAFVw=="
      },
      cookies={
          "__atuvc": "2%7C51%2C8%7C52",
          "__atuvs": "61c7e8b23442eccb001",
          "_dc_gtm_UA-3400662-1": "1",
          "_dc_gtm_UA-48397636-1": "1",
          "_evga_520c": "{%22uuid%22:%2235fd447efffc7b61%22}",
          "_fbp": "fb.1.1640157176230.1522378618",
          "_ga": "GA1.2.1028556115.1640157176",
          "_gcl_au": "1.1.1200473760.1640157175",
          "_gid": "GA1.2.1827316181.1640477046",
          "_hjAbsoluteSessionInProgress": "0",
          "_hjIncludedInSessionSample": "1",
          "_hjSessionUser_534403": "eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==",
          "_hjSession_534403": "eyJpZCI6IjY0MzZhYjVmLTRkNDgtNGJkNS05ZDMyLTIwNTVkYzNmYjNhMCIsImNyZWF0ZWQiOjE2NDA0OTExMjU2MDB9",
          "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
          "csrftoken": cookie['csrftoken'],
          "sessionid": cookie['sessionid'],
          "userDissmissCookieBox": "agree"
      },
      auth=(),
  )

  else:
    lot_res = requests.get(f"https://api01.bonhams.com/api/search{url_suffix_path}?page=1&page_size=1000",
        headers={
            "accept": "application/json, text/plain, */*",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "authority": "api01.bonhams.com",
            "origin": "https://www.bonhams.com",
            "referer": "https://www.bonhams.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        },
        cookies={},
        auth=(),
    )
  
  if lot_res.status_code == 200:
    j = lot_res.json() #json.loads(lot_res.text)
    results = j['results']
    return results
  else:
    return []


def writeResultAsFile(path,no,res:dict):
  p = os.path.join(path,f'{no}.json')
  with open(p,'w') as j:
      json.dump(res,j)



length = 96
c= getSessionCookie()

#1. Auction List 가져오기
cnt = getAuctionList(c,1,1,True)
loopcnt = ceil(cnt/length)
auction_list = []
for i in range(1,10): # range(1,loopcnt+1):
  print(i)
  items = getAuctionList(c,length,i)
  auction_list.extend(items)

#2. Auction 별 Lot List 가져오기
base_path = os.path.join(os.getcwd(),'bonhams')
for i,a in enumerate(auction_list[:6]):
  final_res = dict()
  final_res['auction_info'] = a
  final_res['lot_info'] = getLotDetail(a,c)
  #writeResultAsFile(base_path,a['iSaleNo'],final_res)
  writeResultAsFile(base_path,i,final_res)




# a = auction_list[0]
# auction = a
# cookie = c
# pprint(a)
# getLotDetail(a,c)

# url_suffix_path = '/auctions/26784/' #auction['url']
# #auction_url = urljoin(base_path,url_suffix_path)

# #public
# lot_res = requests.get("https://www.bonhams.com/api/v1/lots/26784/?category=list&length=1000&minimal=false&page=1",
#     headers={
#         "accept": "application/json, text/plain, */*",
#         "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#         "authority": "www.bonhams.com",
#         "referer": "https://www.bonhams.com/",
#         "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-origin",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
#         "x-newrelic-id": "VQAOWVNSChAFUlhSBgAFVw=="
#     },
#     cookies={
#         "__atuvc": "2%7C51%2C1%7C52",
#         "__atuvs": "61c7b195a805129a000",
#         "_dc_gtm_UA-3400662-1": "1",
#         "_dc_gtm_UA-48397636-1": "1",
#         "_evga_520c": "{%22uuid%22:%2235fd447efffc7b61%22}",
#         "_fbp": "fb.1.1640157176230.1522378618",
#         "_ga": "GA1.2.1028556115.1640157176",
#         "_gcl_au": "1.1.1200473760.1640157175",
#         "_gid": "GA1.2.1827316181.1640477046",
#         "_hjAbsoluteSessionInProgress": "0",
#         "_hjIncludedInSessionSample": "1",
#         "_hjSessionUser_534403": "eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==",
#         "_hjSession_534403": "eyJpZCI6ImIxMTIzY2M2LTVkNTYtNDQxNC05YzA0LWQzNDFhYTMzNzYyZCIsImNyZWF0ZWQiOjE2NDA0NzcwNjAxMzV9",
#         "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
#         "csrftoken": cookie['csrftoken'],
#         "sessionid": cookie['sessionid'],
#         "userDissmissCookieBox": "agree"
#     },
#     auth=(),
# )

# resres = lot_res.json()
# resres.keys()
# len(resres['lots'])



# print(parse(t))

# import pandas as pd
# tt = [(aa['url'],aa['iSaleNo'], aa['sale_type']) for aa in auction_list]
# df = pd.DataFrame(tt)
# df.columns = ['url','saleno','type']
# df.type.unique()
# df[df.type =='EXHIBITION'].iloc[0]
# df[df.saleno ==26784].iloc[0]
# from pprint import pprint
# pprint(a)

# #online
# requests.get("https://api01.bonhams.com/api/search/auction/27658/?page=1&page_size=12",
#     headers={
#         "accept": "application/json, text/plain, */*",
#         "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#         "authority": "api01.bonhams.com",
#         "origin": "https://www.bonhams.com",
#         "referer": "https://www.bonhams.com/",
#         "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
#     },
#     cookies={},
#     auth=(),
# )

# #FIXED
# requests.get("https://www.bonhams.com/api/v1/lots/27674/?category=list&length=12&minimal=false&page=1",
#     headers={
#         "accept": "application/json, text/plain, */*",
#         "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#         "authority": "www.bonhams.com",
#         "if-none-match": "W/\"f68449653641807d08991f90746a624a\"",
#         "referer": "https://www.bonhams.com/",
#         "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-origin",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
#         "x-newrelic-id": "VQAOWVNSChAFUlhSBgAFVw=="
#     },
#     cookies={
#         "__atuvc": "2%7C51%2C8%7C52",
#         "__atuvs": "61c7e8b23442eccb001",
#         "_dc_gtm_UA-3400662-1": "1",
#         "_dc_gtm_UA-48397636-1": "1",
#         "_evga_520c": "{%22uuid%22:%2235fd447efffc7b61%22}",
#         "_fbp": "fb.1.1640157176230.1522378618",
#         "_ga": "GA1.2.1028556115.1640157176",
#         "_gcl_au": "1.1.1200473760.1640157175",
#         "_gid": "GA1.2.1827316181.1640477046",
#         "_hjAbsoluteSessionInProgress": "0",
#         "_hjIncludedInSessionSample": "1",
#         "_hjSessionUser_534403": "eyJpZCI6ImFiOGE1ODE5LTM0ZjUtNTc1Mi1iYmE3LWZkZmVhNzY0NjMyMCIsImNyZWF0ZWQiOjE2NDAxNTcxNzYwMDksImV4aXN0aW5nIjp0cnVlfQ==",
#         "_hjSession_534403": "eyJpZCI6IjY0MzZhYjVmLTRkNDgtNGJkNS05ZDMyLTIwNTVkYzNmYjNhMCIsImNyZWF0ZWQiOjE2NDA0OTExMjU2MDB9",
#         "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
#         "csrftoken": "d7nu8pPYHoqNX25HKYgFRoD3Mf3Ru5wAtCPmZYrxPy5UTcIWYDcG1fmDSWQ0vKOe",
#         "sessionid": "zxb2b4t5kapbrtqhoso3ql9qevnhyn1i",
#         "userDissmissCookieBox": "agree"
#     },
#     auth=(),
# )
# >>>