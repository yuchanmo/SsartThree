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
num_cores = multiprocessing.cpu_count() 

# 참고
# https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html

chrome_driver_path = r'D:\Programming\artpassion\aucetl\chromedriver.exe'

#sothebyes model 생성
class SothebysRaw():
  def __init__(self):
    self.lotno = ''
    self.artist_name = ''
    self.title = ''
    self.estimate = ''
    self.sold_price = ''
    self.currency = ''
    self.imgs_urls = []
    self.description = ''
    self.condition = ''
    self.provenance = ''
    self.exhibited = ''
    self.url = ''

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

#selector 에서 text 추출할때 helper
def getTextFromSelector(sel):
  return sel[0].text if len(sel)>0 else ''

#auction 회차 당 페이지내 작품리스트
def getLotListPerPage(pagesource):
  bs = BeautifulSoup(pagesource,'html.parser')
  links = bs.select('a.css-lys2zi')
  linklist = []
  for l in links:
    linklist.append(l['href'])
  return linklist,bs

#auction 회차에 대한 작품리스트
def getTotalLotList(url):
  driver = getHeadlessChromeDriver()
  driver.get(url)
  alllinklist = []
  firstpage,bs = getLotListPerPage(driver.page_source)
  alllinklist.extend(firstpage)
  next_btn_selector = '#__next > div > div:nth-child(4) > div > div.css-11qcavf > div > div > div > div.css-102pgyu > div.css-13o7eu2 > div > div > div > div.css-prdn7r > div > div.css-jxqdoq > ul > li:nth-child(5) > button'
  next_btn = bs.select(next_btn_selector)
  while len(next_btn) > 0 and next_btn[0]['aria-disabled']=='false':    
    try:
      #https://stackoverflow.com/questions/56779520/elementclickinterceptedexception-element-click-intercepted
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #page 마지막에 있는 버튼 클릭시 오류 해결 방법
      sleep(3)
      driver.find_element_by_css_selector(next_btn_selector).click()
      nextpage,bs = getLotListPerPage(driver.page_source)   
      alllinklist.extend(nextpage)
      next_btn = bs.select(next_btn_selector)
    except Exception as e:
      pass
  driver.close()
  return alllinklist


#lot 에 대한 detail 정보   
def getLotDetail(url,driver): 
    print(f'lot detail : {url}')
    status = True
    lot_selector = '#lot-detail-navigator-lot-number'
    artist_name_selector = '#__next > div > div:nth-child(4) > div > div > div.css-178yklu.row > div.col-xs-12.col-sm-12.col-md-4.col-lg-4.css-12boka1 > div.css-ojf2e4 > div.css-10pbwcw > div.css-5z1i8i > h1.headline-module_headline28Regular__4N1Ch.css-1js7kn9'
    title_selector = '#__next > div > div:nth-child(4) > div > div > div.css-178yklu.row > div.col-xs-12.col-sm-12.col-md-4.col-lg-4.css-12boka1 > div.css-ojf2e4 > div.css-10pbwcw > div.css-5z1i8i > p.paragraph-module_paragraph18Regular__34C1i.css-ahigpk'
    estimate_selector = '#__next > div > div:nth-child(4) > div > div > div.css-178yklu.row > div.col-xs-12.col-sm-12.col-md-4.col-lg-4.css-12boka1 > div.css-ojf2e4 > div.css-10pbwcw > div.css-5z1i8i > div.css-10l5lxu > p:nth-child(2)'
    sold_price_selector = '#__next > div > div:nth-child(4) > div > div > div.css-178yklu.row > div.col-xs-12.col-sm-12.col-md-4.col-lg-4.css-12boka1 > div.css-ojf2e4 > div.css-10pbwcw > div:nth-child(4) > div.css-14fljz1 > div.css-11pw8p5 > p.label-module_label16Medium__2HDfw.css-1u9s01'
    currency_selector = '#__next > div > div:nth-child(4) > div > div > div.css-178yklu.row > div.col-xs-12.col-sm-12.col-md-4.col-lg-4.css-12boka1 > div.css-ojf2e4 > div.css-10pbwcw > div:nth-child(4) > div.css-14fljz1 > div.css-11pw8p5 > p.label-module_label16Medium__2HDfw.css-15titbp'
    imgs_selector = 'img.css-r91awh'
    detail_selector = 'div.css-8cpbw4'  
    driver.get(url)
    source = driver.page_source
    bs =BeautifulSoup(source,'html.parser')
    s = SothebysRaw()
    s.url = url
    try:
      s.lotno = getTextFromSelector(bs.select(lot_selector))
      s.artist_name = getTextFromSelector(bs.select(artist_name_selector))
      s.title = getTextFromSelector(bs.select(title_selector)) 
      s.estimate = getTextFromSelector(bs.select(estimate_selector)) 
      s.sold_price = getTextFromSelector(bs.select(sold_price_selector)) 
      s.currency = getTextFromSelector(bs.select(currency_selector)) 
      imgs = bs.select(imgs_selector)
      s.imgs_urls = [i['src'] for i in imgs]
      details = bs.select(detail_selector)
      s.description =str(details[0].select('p')) if len(details)>=1 else ''
      s.condition = str(details[1].select('p')) if len(details)>=2 else ''
      s.provenance = [str(f.text) for f in  details[2].select('div.css-xs9w33')] if len(details)>=3 else []
      s.exhibited = [str(f.text) for f in details[3].select('div.css-xs9w33')] if len(details)>=4 else []  
    except Exception as e:
      status = False
      pass
    finally:
      pass     
    return s

#sothebye 접속 위한 세션정보 불러오기
def getSessionInfo():
  try:
    driver = getHeadlessChromeDriver()
    driver.get('https://www.sothebys.com')
    cookies = driver.get_cookies()
    session_cookie = dict()
    for cookie in cookies:
        print('name : ',cookie['name'],'value : ',cookie['value'],'\n')
        session_cookie[cookie['name']] = cookie['value']
    driver.close()
  except Exception as e:
    pass
  return session_cookie

# 필터조건에 대한 전체 옥션리스트 가져오기
def getAuctionList(sessionCookie,i):
  reslist=[]
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
      "ak_bmsc": sessionCookie['ak_bmsc'],
      "bm_sv": sessionCookie['bm_sv'],
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
  return reslist

def getUidSet(auctionList:list):
  if type(auctionList) == list:
    return set([t['uid'] for t in auctionList])
  else:
    return set()


def getTotalAuctionList():
  try:
    total_auction_list = []
    session_cookie = getSessionInfo()
    prev_set = set()
    curr_set = set()
    loop_flag = True  
    i = 1
    while loop_flag:
      print(i)
      auction_list = getAuctionList(session_cookie,i)
      print(auction_list)
      curr_set = getUidSet(auction_list)
      if prev_set != curr_set:
        total_auction_list.extend(auction_list)
        i+=1
        prev_set = curr_set    
      else:
        loop_flag = False
    with open('sothebyes.json','w') as f:
      json.dump(total_auction_list,f)
  except Exception as e:
    pass

def loadTotalAuctionList():
  ff = open('sothebyes.json',encoding='utf-8')
  a = json.load(ff)
  ff.close()
  return a




def crawlAuction(t):  
  u = t['link']  
  print(f'===start crawling : {u}===')
  res = getTotalLotList(u)
  res = set(res)
  baseurl = 'https://www.sothebys.com'
  lotlist_urls = [urljoin(baseurl,uu) for uu in res]
  driver = getHeadlessChromeDriver()
  lotdetail_list = []     
  i = 1
  for lu in lotlist_urls:
    tmp = getLotDetail(lu,driver)
    lotdetail_list.append(tmp.__dict__)    
  #parmap.map(getLotDetail,lotlist_urls[:3],driver,total_lot_details,pm_pbar=True,pm_processes=int(num_cores/2))  
  driver.close()
  t['data'] = lotdetail_list# total_lot_details
  filename = t['uid']+'.json'
  full_path = os.path.join(os.getcwd(),'sothebyes',filename)
  with open(full_path,'w') as f:
    json.dump(t,f)
  #return True


if __name__=='__main__':
  al = loadTotalAuctionList()
  for a in al:
    crawlAuction(a)
  #parmap.map(crawlAuction,al,pm_pbar=True,pm_processes=int(num_cores/2))
  

