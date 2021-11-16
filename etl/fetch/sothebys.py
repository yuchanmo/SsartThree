from logging import log
from requests.api import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
from bs4 import BeautifulSoup
import json
import os
import multiprocessing
import parmap
from uncurl import parse
num_cores = multiprocessing.cpu_count() 

# 참고
# https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html

chrome_driver_path = r'D:\Programming\artpassion\aucetl\chromedriver.exe'

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


# '''
# curl 'https://www.sothebys.com/data/api/asset.actions.json?id=0000017b-de42-d0fb-ad7b-dee60c540002,0000017c-3133-d118-a9ff-35bfe3d90000,0000017c-7a59-d118-a9ff-7fff0daf0000,0000017c-c6ee-ddb5-abfd-e7ff04240000,0000017a-aa06-d35c-a37e-eb6edffe0000,0000017c-8333-d118-a9ff-97bfe3aa0000,0000017b-caba-d7f6-a1fb-dabafed70000,0000017a-afef-d35c-a37e-efeff1f30000,0000017b-886a-d2cb-a77f-ab6b435b0000,0000017c-bd81-d878-a57c-ff996cde0000,00000178-ead5-dd94-a37f-fadd69090000,0000017c-31b7-d118-a9ff-35bfdd8b0000,0000017c-b6d2-d5e4-a3ff-fef388d40000,0000017c-6fd6-d118-a9ff-7ffe02a70000,0000017a-afef-d35c-a37e-efeff7730000' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'Accept: */*' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://www.sothebys.com/en/results?locale=en' \
#   -H 'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'Cookie: optimizelyEndUserId=oeu1636632778033r0.7569119366452541; ak_bmsc=B53524F7C1CE417CED250810393AC779~000000000000000000000000000000~YAAQRDVDFy/WDwR9AQAAk2TqDg2ky2b8dDrQmbynBtHW9xU+w5KypJZ+PiJn8jA7VxdCt2LQZzjjiEnO6NDzjtEBvNkP4CMKoNk8NKNuYDE3H5Lx64ZMDaxPCyUi5zpAk1mPHqREh0bao84fOmnbvjBtOvg9yA97S6053VDBjPvdJ6Vn1IdeFSctgvHe+zEWcgr+iHztzxdu0Gfayf+4nF3Uk2KtSDg/KbbHhXichjDmLRoOoJBcalmrh0xcVzI1UzIgek/PHNLEw39rOZe2Wx9ZqKRX6448H5GYTkUYSt+xdCoFgRzK6MTVQqKESjeURIYJNZVzNU/Lt866pTgcT6Zx52OPtYUbDIqUDwSPmCkeSVV8FBVkHLpRKNVXZZjCLSYcpKPbbN0ohfTlq96jPnN0bgu4+khdkr7KAAluckaTq9O28VUl5Pq2sXmNzqcc4y8th/Ph9yck4GlMWgT9duJVpIMMJt1eRSBgDBHD7VA=; tracking-preferences={%22version%22:1%2C%22destinations%22:{%22AdWords%22:true%2C%22Adobe%20Analytics%22:true%2C%22Algolia%22:true%2C%22Amplitude%22:true%2C%22Chartbeat%22:true%2C%22DoubleClick%20Floodlight%22:true%2C%22Facebook%20Pixel%22:true%2C%22Google%20Analytics%22:true%2C%22Google%20Tag%20Manager%22:true%2C%22Optimizely%22:true%2C%22Pinterest%20Tag%22:true%2C%22Promoter.io%22:true%2C%22Twitter%20Ads%22:true%2C%22Visual%20Tagger%22:true%2C%22Zaius%22:true}%2C%22custom%22:{%22marketingAndAnalytics%22:true%2C%22advertising%22:true%2C%22functional%22:true}}; ajs_anonymous_id=%223d2fb784-8499-4ff8-9b74-54aedf12a616%22; _cb_ls=1; _cb=HT16CChJ1TCs3QbP; _cb_svref=https%3A%2F%2Fwww.google.co.kr%2F; _ga=GA1.2.1549775581.1636632788; _gid=GA1.2.646594367.1636632788; AMCVS_5AFE123F5245AD060A490D45%40AdobeOrg=1; _fbp=fb.1.1636632787789.1306114302; zaius_js_version=2.21.4; z_idsyncs=; vtsrc=source%3Dgoogle%7Cmedium%3Dorganic; s_ecid=MCMID%7C63915200568645920164539002264889405792; s_cc=true; AMCV_5AFE123F5245AD060A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C18943%7CMCMID%7C63915200568645920164539002264889405792%7CMCAAMLH-1637237587%7C11%7CMCAAMB-1637237587%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1636639988s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; s_sq=%5B%5BB%5D%5D; indentifyUser=unknown; _gat=1; _chartbeat5=; bm_sv=6A5F3887D37D538624B41AA11C627519~PWieWKeX2WqBAQ/ubunrPIHj0xHg3sZPqbIENL60Yj+0HeYBz7/Itdoo8TSPwx0gRfnB9w/wSQIXXoeJP8zarE+CTtpfFUCDoJWn3ErtvnLURlZa5qVnUkvRNIxnDzbTSZijkPWpmDgCCT+kDYR3Uw72gXZrpxtyeBTDA6Gy/Tk=; com.auth0.auth.AJZSu6NRzJY9mzoss82d-6acT-n76MyT={%22nonce%22:%22eUrXFhVbVN6R8hRfmjp8TUwFLxCUwOok%22%2C%22state%22:%22AJZSu6NRzJY9mzoss82d-6acT-n76MyT%22}; _chartbeat2=.1636632787270.1636633007888.1.BKRTfZBQy63ABfkI7-u2u9DYX5Pu.4; vuid=d80723e1-be80-487b-83c4-79a24f846465%7C1636633008271' \
#   --compressed
#   '''

# r =  requests.get(u)
# u = '''
# https://www.sothebys.com/en/results?from=&to=&q=&p=5&_requestType=ajax
# '''

# url = '''
# curl 'https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&f2=00000164-609b-d1db-a5e6-e9ff08ab0000&f2=00000164-609b-d1db-a5e6-e9ff0b150000&f3=LIVE&f3=ONLINE&q=&p=4&_requestType=ajax' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'Accept: */*' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&f2=00000164-609b-d1db-a5e6-e9ff08ab0000&f2=00000164-609b-d1db-a5e6-e9ff0b150000&f3=LIVE&f3=ONLINE&q=' \
#   -H 'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'Cookie: optimizelyEndUserId=oeu1636632778033r0.7569119366452541; tracking-preferences={%22version%22:1%2C%22destinations%22:{%22AdWords%22:true%2C%22Adobe%20Analytics%22:true%2C%22Algolia%22:true%2C%22Amplitude%22:true%2C%22Chartbeat%22:true%2C%22DoubleClick%20Floodlight%22:true%2C%22Facebook%20Pixel%22:true%2C%22Google%20Analytics%22:true%2C%22Google%20Tag%20Manager%22:true%2C%22Optimizely%22:true%2C%22Pinterest%20Tag%22:true%2C%22Promoter.io%22:true%2C%22Twitter%20Ads%22:true%2C%22Visual%20Tagger%22:true%2C%22Zaius%22:true}%2C%22custom%22:{%22marketingAndAnalytics%22:true%2C%22advertising%22:true%2C%22functional%22:true}}; ajs_anonymous_id=%223d2fb784-8499-4ff8-9b74-54aedf12a616%22; _cb_ls=1; _cb=HT16CChJ1TCs3QbP; _ga=GA1.2.1549775581.1636632788; _gid=GA1.2.646594367.1636632788; AMCVS_5AFE123F5245AD060A490D45%40AdobeOrg=1; _fbp=fb.1.1636632787789.1306114302; zaius_js_version=2.21.4; z_idsyncs=; vtsrc=source%3Dgoogle%7Cmedium%3Dorganic; s_ecid=MCMID%7C63915200568645920164539002264889405792; s_cc=true; _pin_unauth=dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw; indentifyUser=unknown; ak_bmsc=7FA1AF16167A7BA585DDE331321D9998~000000000000000000000000000000~YAAQV5c7F6xANOl8AQAAOxhtDw1iCOOcSbi9Pn4FfHQAbyo/ATfDa8CqwPlo9fqJiobCy8cGkLt2yGT67ejiyVMy2tdsyY2QuXWNqpXU7HdbuNY3M+2YWnNNEi8CNHSm58QlgsSid1iZonrRfLV5RIv6MDDTLcGLMBhIF7jHpTNR3yvYL2+QQdmyNX7etLuNMv7s+71FsulVTONddfKZLxl9cZ0Gq0SiL8MiiWuk61HCrtJFE6XjrWgW70aKsNE89/XE2YufgJzRJs6r3GGbB7HXG9HNqTBlxbKTpvXkCzVshwHO18uf9jSwNVpjv50vKnq9ZJYzTDedEZq6qB/o8sbyp1ukE2ACsIenX8F3dgGgVvQ7RTekCDfNXuyXtWrjgrrF4NliYOAvUQFahTNjc+NypB23uCLDxVX9jepLfOob09JW+Q1gGORu6sXk9FI7HfbyqP4hGQQSivyiqWMzN4w6ig9lnjBDfIwHBKU7QPE=; _cb_svref=https%3A%2F%2Fwww.sothebys.com%2Fen%2F; AMCV_5AFE123F5245AD060A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C18943%7CMCMID%7C63915200568645920164539002264889405792%7CMCAAMLH-1637246149%7C11%7CMCAAMB-1637246149%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1636648549s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_sq=%5B%5BB%5D%5D; acceptedCookieUsage=true; _chartbeat2=.1636632787270.1636642290081.1.8fcqUD5AHItBhgBHHfaLHJDwcb_o.9; _gat=1; vuid=d80723e1-be80-487b-83c4-79a24f846465%7C1636642292125; bm_sv=48D027B65AD8D53CC96A0A732D691012~J4/XiACgm9yeJPO2lx3noiu4unrahqZ1Zm2GffnuJ6ef0d5W9YAkRqQM24bM6RfwMbxXRCmxbexdZvi20cZ6BYSLCvivCpJwb0xMCAdw9g39mRHM5Ens7Q1PiRZl4xV++47fkPcDZKx+/uXzP7t6Uza9kx8uaR+PDOK2tjJXK+8=' \
#   --compressed
# '''

#1 전체 auction list 추출
# print(parse(url))
linklist = []

driver = getHeadlessChromeDriver()
driver.get('https://www.sothebys.com')
cookies = driver.get_cookies()
session_cookie = dict()

for cookie in cookies:
    print('name : ',cookie['name'],'value : ',cookie['value'],'\n')
    session_cookie[cookie['name']] = cookie['value']
driver.close()
reslist = []
#for i in range(0,1000):
i= 1
print(f'======={i}=======')
res = requests.get(f"https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&f2=00000164-609b-d1db-a5e6-e9ff08ab0000&f2=00000164-609b-d1db-a5e6-e9ff0b150000&f3=LIVE&f3=ONLINE&q=&p={i}&_requestType=ajax",
  headers={
      "Accept": "*/*",
      "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
      "Connection": "keep-alive",
      "Referer": "https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&f2=00000164-609b-d1db-a5e6-e9ff08ab0000&f2=00000164-609b-d1db-a5e6-e9ff0b150000&f3=LIVE&f3=ONLINE&q=",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
      "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\""
  },
  cookies={
      "AMCVS_5AFE123F5245AD060A490D45%40AdobeOrg": "1",
      "AMCV_5AFE123F5245AD060A490D45%40AdobeOrg": "1585540135%7CMCIDTS%7C18943%7CMCMID%7C63915200568645920164539002264889405792%7CMCAAMLH-1637246149%7C11%7CMCAAMB-1637246149%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1636648549s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0",
      "_cb": "HT16CChJ1TCs3QbP",
      "_cb_ls": "1",
      "_cb_svref": "https%3A%2F%2Fwww.sothebys.com%2Fen%2F",
      "_chartbeat2": ".1636632787270.1636642290081.1.8fcqUD5AHItBhgBHHfaLHJDwcb_o.9",
      "_fbp": "fb.1.1636632787789.1306114302",
      "_ga": "GA1.2.1549775581.1636632788",
      "_gat": "1",
      "_gid": "GA1.2.646594367.1636632788",
      "_pin_unauth": "dWlkPU1UWXlOV1E1TTJNdFpUazRPQzAwTTJSa0xXRTROVFF0Wm1RM1pXWmhOelEzTWpSaw",
      "acceptedCookieUsage": "true",
      "ajs_anonymous_id": "%223d2fb784-8499-4ff8-9b74-54aedf12a616%22",
      "ak_bmsc": session_cookie['ak_bmsc'],
      "bm_sv": session_cookie['bm_sv'],
      "indentifyUser": "unknown",
      "optimizelyEndUserId": "oeu1636632778033r0.7569119366452541",
      "s_cc": "true",
      "s_ecid": "MCMID%7C63915200568645920164539002264889405792",
      "s_sq": "%5B%5BB%5D%5D",
      "tracking-preferences": "{%22version%22:1%2C%22destinations%22:{%22AdWords%22:true%2C%22Adobe%20Analytics%22:true%2C%22Algolia%22:true%2C%22Amplitude%22:true%2C%22Chartbeat%22:true%2C%22DoubleClick%20Floodlight%22:true%2C%22Facebook%20Pixel%22:true%2C%22Google%20Analytics%22:true%2C%22Google%20Tag%20Manager%22:true%2C%22Optimizely%22:true%2C%22Pinterest%20Tag%22:true%2C%22Promoter.io%22:true%2C%22Twitter%20Ads%22:true%2C%22Visual%20Tagger%22:true%2C%22Zaius%22:true}%2C%22custom%22:{%22marketingAndAnalytics%22:true%2C%22advertising%22:true%2C%22functional%22:true}}",
      "vtsrc": "source%3Dgoogle%7Cmedium%3Dorganic",
      "vuid": "d80723e1-be80-487b-83c4-79a24f846465%7C1636642292125",
      "z_idsyncs": "",
      "zaius_js_version": "2.21.4"
  },
  auth=(),
)

bs = BeautifulSoup(res.text,'html.parser')
cards = bs.select('div.Card-info')

for c in cards:
  try:
    link = c.find('a')['href']
    uid = c.find('dynamic-cta')['uuid']
    title = c.select('div.Card-title')[0].text
    detail = c.select('div.Card-details')[0].text
    cres = {'title':title , 'detail':detail,'uid':uid, 'link':link,}
    print(cres)
    reslist.append(cres)
  except Exception as e:
    pass
    
c
import pandas as pd
df = pd.DataFrame(reslist)
df = df.drop_duplicates()
len(df)

df.to_csv('sothebys.csv')

driver = getHeadlessChromeDriver()
driver.get('https://www.sothebys.com/en/buy/auction/2021/contemporary-curated-5')
import codecs
sample_path = 'sotheby_sample.html'
f = codecs.open(sample_path, "w", "utf−8")
h = driver.page_source
f.write(h)
f.close()
driver.page_source
bs = BeautifulSoup(h,'html.parser')
links = bs.select('a.css-lys2zi')
linklist = []

for l in links:
  linklist.append(l['href'])

next_btn = bs.select('#__next > div > div:nth-child(4) > div > div.css-11qcavf > div > div > div > div.css-102pgyu > div.css-13o7eu2 > div > div > div > div.css-prdn7r > div > div.css-jxqdoq > ul > li:nth-child(5) > button')

#2. 각 옥션별 LOT LIST 추출

#3. LOT 별 상세 정보 추출
