from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
from bs4 import BeautifulSoup
import json
import os

# 0. curl 정보로 requests 포멧 확인
seoul_acution_cur_ver ='''
curl 'https://www.seoulauction.com/api/actionSet' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'X-CSRF-TOKEN: 35a3c8c4-b38d-4e00-bf09-9237b5236ef3' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
  -H 'Content-Type: application/json; charset=UTF-8' \
  -H 'Origin: https://www.seoulauction.com' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=652' \
  -H 'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Cookie: notified-HTTPS_Notice=1; JSESSIONID=A1E47CE54CC9537EADDD04A358BEC520.was2; sale_no=652; curr_url=/WEB-INF/views/sale/lotList.jsp; prev_url=/WEB-INF/views/sale/lotList.jsp; wcs_bt=19656f7bcf4c5c:1627969637; reqRowCnt=20; sortBy=LOTAS' \
  --data-raw '{"baseParms":{"sale_no":"652","expe_from_price":null,"expe_to_price":null,"cate_cds":null,"scate_cds":null,"mate_cds":null,"hashtag_list":null,"fav_cds_list":null},"actionList":[{"actionID":"sale_info","actionType":"select","tableName":"SALE"},{"actionID":"exch_rate_list","actionType":"select","tableName":"EXCH"},{"actionID":"lot_list_count","actionType":"select","tableName":"LOT_CNT","parmsList":[{"for_count":true}]},{"actionID":"lot_list_paging","actionType":"select","tableName":"LOTS","parmsList":[{"from":0,"rows":20,"sale_outside_yn":"N","sort_by":"LOTAS"}]},{"actionID":"get_customer_by_cust_no","actionType":"select","tableName":"CUST_INFO","parmsList":[]},{"actionID":"saleLot_category","actionType":"select","tableName":"CATEGORY"},{"actionID":"saleLot_subcategory","actionType":"select","tableName":"SUBCATEGORY"},{"actionID":"saleLot_material","actionType":"select","tableName":"MATERIAL"},{"actionID":"saleLot_artist","actionType":"select","tableName":"ARTIST"},{"actionID":"saleLot_hashtag","actionType":"select","tableName":"HASHTAG"},{"actionID":"saleHighlight_List","actionType":"select","tableName":"LOT_HIGHLIGHT"},{"actionID":"sale_cert_info","actionType":"select","tableName":"CERT"},{"actionID":"my_paddle_check","actionType":"select","tableName":"PADDLE_CHECK","parmsList":[{}]}]}' \
  --compressed
  '''

import uncurl
print(uncurl.parse(seoul_acution_cur_ver))


JSON_SAVE_PATH = '/home/fakeblocker/code/python/Auc/result/seoul'
IMAGE_SAVE_PATH = '/home/fakeblocker/code/python/Auc/result/seoul/images'

class SeoulAuctionRequester():
    def __init__(self):
        self.session = requests.Session()
        self.__setSessionInfo()

    def __setSessionInfo(self):
        try:
        #https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html
        #1. selenium 으로 login 후 requests에 필요한 cookie/csrf취합
            print('===========1)login in seoul auction===========')
            login_info = {
                'id':'densetsu',
                'pwd':'ahdbapwk55*'
            }

            id = login_info['id']
            pwd = login_info['pwd']

            CHROMEDRIVER_PATH = r'/home/fakeblocker/code/python/Auc/chromedriver'
            options = Options()
            options.add_argument('headless')
            options.headless = driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
            driver.get('https://www.seoulauction.com/login')
            driver.find_element_by_id('loginId').send_keys(id)
            driver.find_element_by_id('password').send_keys(pwd)
            driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div/div[3]/div[3]/span/button').click()

            #http://me2c.blogspot.com/2019/04/selenium-python-requests-chromedriver-2.html
            print('===========2)get csrf info===========')
            #1) csrf 정보 취득
            html = driver.page_source
            bs = BeautifulSoup(html,'html.parser')
            csrf = bs.find('input',{'name':'_csrf'})['value']

            #2) session 정보 취득
            print('===========3)set Cookie===========')
            self.session_cookie = {
                'JSESSIONID':'',
                'wcs_bt':'',
                'csrf':csrf
            }
            cookies = driver.get_cookies()
            for cookie in cookies:
                #print(cookie['name'],cookie['value'])
                self.session.cookies.set(cookie['name'],cookie['value'])
                self.session_cookie[cookie['name']] = cookie['value']
            driver.close()
        except Exception as e:
            raise e

    def getAuctionResult(self,no,writeAsFile=True):
        try:       
            print(f'========load data for auction no {no}========')           
            row_cnt = 500
            data_param = {"baseParms":{"sale_no":f"{no}","expe_from_price":None,"expe_to_price":None,"cate_cds":None,"scate_cds":None,"mate_cds":None,"hashtag_list":None,"fav_cds_list":None},"actionList":[{"actionID":"sale_info","actionType":"select","tableName":"SALE"},{"actionID":"exch_rate_list","actionType":"select","tableName":"EXCH"},{"actionID":"lot_list_count","actionType":"select","tableName":"LOT_CNT","parmsList":[{"for_count":True}]},{"actionID":"lot_list_paging","actionType":"select","tableName":"LOTS","parmsList":[{"from":0,"rows":row_cnt,"sale_outside_yn":"N","sort_by":"LOTAS"}]},{"actionID":"get_customer_by_cust_no","actionType":"select","tableName":"CUST_INFO","parmsList":[]},{"actionID":"saleLot_category","actionType":"select","tableName":"CATEGORY"},{"actionID":"saleLot_subcategory","actionType":"select","tableName":"SUBCATEGORY"},{"actionID":"saleLot_material","actionType":"select","tableName":"MATERIAL"},{"actionID":"saleLot_artist","actionType":"select","tableName":"ARTIST"},{"actionID":"saleLot_hashtag","actionType":"select","tableName":"HASHTAG"},{"actionID":"saleHighlight_List","actionType":"select","tableName":"LOT_HIGHLIGHT"},{"actionID":"sale_cert_info","actionType":"select","tableName":"CERT"},{"actionID":"my_paddle_check","actionType":"select","tableName":"PADDLE_CHECK","parmsList":[{}]}]}
            data_param_str = json.dumps(data_param)
            res = requests.post("https://www.seoulauction.com/api/actionSet",
                data=data_param_str,
                headers={
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Origin": "https://www.seoulauction.com",
                    "Referer": "https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=652",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                    "X-CSRF-TOKEN": f"{self.session_cookie['csrf']}",
                    "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
                    "sec-ch-ua-mobile": "?0"
                },
                cookies={
                    "JSESSIONID": f"{self.session_cookie['JSESSIONID']}",
                    "curr_url": "/WEB-INF/views/sale/lotList.jsp",
                    "notified-HTTPS_Notice": "1",
                    "prev_url": "/WEB-INF/views/sale/lotList.jsp",
                    "reqRowCnt": str(row_cnt),
                    "sale_no": str(no),
                    "sortBy": "LOTAS",
                    "wcs_bt": f"{self.session_cookie['wcs_bt']}"
                },
                auth=(),
            )
            if res.status_code ==200:
                if writeAsFile:
                    p = os.path.join(JSON_SAVE_PATH,f'{no}.json')
                    with open(p,'w') as j:
                        json.dump(res.json(),j)
                return res.json()
            else:
                return None
        except Exception as e:
            print(e)

    @staticmethod
    def downloadArtImages(no):
        try:
            data_path = f'{JSON_SAVE_PATH}/{no}.json'
            with open(data_path) as f:
                data = json.load(f)
            samples = data['tables']['LOTS']['rows']
            for sample in samples:
                lot_no,image_path,image_name = sample['LOT_NO'],sample['LOT_IMG_PATH'],sample['LOT_IMG_NAME']
                image_full_path_url = f"https://www.seoulauction.com/nas_img{image_path}/list/{image_name}"
                print(image_full_path_url)
                response = requests.get(image_full_path_url,stream=True)
                dest_folder = f'{i}'
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                file_path = os.path.join(dest_folder,f'{lot_no}_{image_name}')
                with open(file_path,'w') as f:
                    for chunk in response:
                        f.write(chunk)
        except Exception as e:
            print(e)
            pass
        


#if __name__ =='__main__':
#c= SeoulAuctionRequester()
for i in range(1,653):
    #rr = c.getAuctionResult(i)
    SeoulAuctionRequester.downloadArtImages(i)
    time.sleep(1)


i
#https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
samples = rr['tables']['LOTS']['rows']
for sample in samples:
    lot_no,image_path,image_name = sample['LOT_NO'],sample['LOT_IMG_PATH'],sample['LOT_IMG_NAME']
    image_full_path_url = f"https://www.seoulauction.com/nas_img{image_path}/list/{image_name}"
    print(image_full_path_url)
    response = requests.get(image_full_path_url,stream=True)
    dest_folder = f'{i}'
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    file_path = os.path.join(dest_folder,f'{lot_no}_{image_name}')
    with open(file_path,'w') as f:
        for chunk in response:
            f.write(chunk)
    

# 'https://www.seoulauction.com/nas_img/front/plan0652/list/b144b083-0cdb-4b73-83c0-67b21e6e9f56.jpg'
IMAGE_BASE_URL = 'https://www.seoulauction.com/nas_img/front/plan0652/list/b144b083-0cdb-4b73-83c0-67b21e6e9f56.jpg'