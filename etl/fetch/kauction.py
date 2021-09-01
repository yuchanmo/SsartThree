from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
from bs4 import BeautifulSoup
import json
import os
import uncurl


# fetch_curl ='''
# curl 'https://www.k-auction.com/api/Auction/4/273' \
#   -H 'authority: www.k-auction.com' \
#   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
#   -H 'accept: */*' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
#   -H 'content-type: application/json' \
#   -H 'origin: https://www.k-auction.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://www.k-auction.com/Auction/Weekly/273?price_from=0&price_to=6000000&page=1&auc_kind=4&auc_num=273' \
#   -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'cookie: K-Auction.Token=1ec8523e3e974d6a9f5ece0c959200cf; _ga=GA1.2.2036382434.1628002323; _BS_GUUID=uxejjSc8YlP89qfJQxxbBJ9e3JPuIYqcvFwOxJWw; _TRK_CR=https%3A%2F%2Fwww.google.co.kr%2F; _gid=GA1.2.163908607.1628264643; _TRK_UID=a0b860d20f9b700c7c1aec08990c070f:2:1.51805234375:1628264642813; _TRK_SID=8294505574fb40983d414f707c7ec59c; .AspNetCore.Cookies=CfDJ8Go3F9LXhqNHnmEE9fnBWD5ZPHsScByGNSSUDCFufiELQjbofFDOvQGpf2lznKhnT1F3F-uSZnqULh23k5B-IOqwEEX0b_bhXgPEGUfFSJSeNqhI6_KjCbgbzEGSRHo2a-N0h51bIA1LHSN6I8LZM2coMiwAvV6Z67o4Au3lBtDRjlQZ4GeB47-iqQGulqpWIiDv4zXB9oozfz9Y8euI74V_7pYQTrJSgNGf0l-mzc3j5M6RLKsYIThuW9jF_LkN7Q1jc3BXEAlx4PyexXJnqsu6GSVmij11baQevZU-nJDdO3IMUUU5qPqTYAPEWoHa38V_ehO0Wk8pXDzpwF__p9i5lmjF3RTwWHb4a8oQaGXgZ8TLeGFOpbmYizjdNCP-v7k3QmjJ7z_G85G4aCjlgaf8mwOWr7v-zd323o3lCb0gT7fEXDwjGDc5Qfas-EG-eDMkMShjgLVFZ3F-SOw9lIOZjp7KFXmDrVEJzZiJsHfGe7ZMmXeGVPkT6EXoes8hdI_U8lRWhCM9VfyxwMtiDNAuG5xD9ZRLHtvq7piePQHY7W1E3lFaz5jxvA1pcPv95_BWBzUJXxPUD29g6Uzgs00DN9xvwAU35h_GI-qSLRtK2nRc78AZgFmctEHrM22TVufK8yZtiNs2nLDevMJaPpGaPWxAWeiPqt3UAb_COKkTv1vYM1Vrl9BB_jFXpfpllfmco4YvyskD7vdWUuJ-Km1fGYghYL1l5TkLbKJpUJtNVSr0tDAxdH9HWtGNkzxWdHoCTxDQXq57lZ4opobq8VNYyIMtbh9p4_EYYf2iRq1pptSu99aaBz2bj3nDjcYJu2A9S2hnhbD6BU6hjgsIucadhU5s-TuwcCkehIzWsUIQMi0Zs7LZcyhkfBBLVFreSr6o1fd6LHX63RfdgrmtNRm57RQwbwh2-TogsHQneM6L; .AspNetCore.Culture=c%3Den-US%7Cuic%3Den-US; _TRK_EX=14' \
#   --data-raw '{"price_from":"0","price_to":"6000000","page":"1","auc_kind":"4","auc_num":"273"}' \
#   --compressed'''


# weekly ='''
# curl 'https://www.k-auction.com/api/Auction/4/273' \
#   -H 'authority: www.k-auction.com' \
#   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
#   -H 'accept: */*' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
#   -H 'content-type: application/json' \
#   -H 'origin: https://www.k-auction.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://www.k-auction.com/Auction/Weekly/273?price_from=0&price_to=6000000&page=1&auc_kind=4&auc_num=273' \
#   -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'cookie: K-Auction.Token=1ec8523e3e974d6a9f5ece0c959200cf; _ga=GA1.2.2036382434.1628002323; _BS_GUUID=uxejjSc8YlP89qfJQxxbBJ9e3JPuIYqcvFwOxJWw; _TRK_CR=https%3A%2F%2Fwww.google.co.kr%2F; _gid=GA1.2.163908607.1628264643; _TRK_UID=a0b860d20f9b700c7c1aec08990c070f:2:1.51805234375:1628264642813; _TRK_SID=8294505574fb40983d414f707c7ec59c; .AspNetCore.Cookies=CfDJ8Go3F9LXhqNHnmEE9fnBWD5ZPHsScByGNSSUDCFufiELQjbofFDOvQGpf2lznKhnT1F3F-uSZnqULh23k5B-IOqwEEX0b_bhXgPEGUfFSJSeNqhI6_KjCbgbzEGSRHo2a-N0h51bIA1LHSN6I8LZM2coMiwAvV6Z67o4Au3lBtDRjlQZ4GeB47-iqQGulqpWIiDv4zXB9oozfz9Y8euI74V_7pYQTrJSgNGf0l-mzc3j5M6RLKsYIThuW9jF_LkN7Q1jc3BXEAlx4PyexXJnqsu6GSVmij11baQevZU-nJDdO3IMUUU5qPqTYAPEWoHa38V_ehO0Wk8pXDzpwF__p9i5lmjF3RTwWHb4a8oQaGXgZ8TLeGFOpbmYizjdNCP-v7k3QmjJ7z_G85G4aCjlgaf8mwOWr7v-zd323o3lCb0gT7fEXDwjGDc5Qfas-EG-eDMkMShjgLVFZ3F-SOw9lIOZjp7KFXmDrVEJzZiJsHfGe7ZMmXeGVPkT6EXoes8hdI_U8lRWhCM9VfyxwMtiDNAuG5xD9ZRLHtvq7piePQHY7W1E3lFaz5jxvA1pcPv95_BWBzUJXxPUD29g6Uzgs00DN9xvwAU35h_GI-qSLRtK2nRc78AZgFmctEHrM22TVufK8yZtiNs2nLDevMJaPpGaPWxAWeiPqt3UAb_COKkTv1vYM1Vrl9BB_jFXpfpllfmco4YvyskD7vdWUuJ-Km1fGYghYL1l5TkLbKJpUJtNVSr0tDAxdH9HWtGNkzxWdHoCTxDQXq57lZ4opobq8VNYyIMtbh9p4_EYYf2iRq1pptSu99aaBz2bj3nDjcYJu2A9S2hnhbD6BU6hjgsIucadhU5s-TuwcCkehIzWsUIQMi0Zs7LZcyhkfBBLVFreSr6o1fd6LHX63RfdgrmtNRm57RQwbwh2-TogsHQneM6L; _TRK_EX=15; .AspNetCore.Culture=c%3Dko-KR%7Cuic%3Dko-KR' \
#   --data-raw '{"price_from":"0","price_to":"6000000","page":"1","auc_kind":"4","auc_num":"273"}' \
#   --compressed'''


# print(uncurl.parse(weekly))

# major ='''
# curl 'https://www.k-auction.com/api/Auction/1/140' \
#   -H 'authority: www.k-auction.com' \
#   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
#   -H 'accept: */*' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
#   -H 'content-type: application/json' \
#   -H 'origin: https://www.k-auction.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://www.k-auction.com/Auction/Major/140' \
#   -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'cookie: K-Auction.Token=1ec8523e3e974d6a9f5ece0c959200cf; _ga=GA1.2.2036382434.1628002323; _BS_GUUID=uxejjSc8YlP89qfJQxxbBJ9e3JPuIYqcvFwOxJWw; .AspNetCore.Culture=c%3Dko-KR%7Cuic%3Dko-KR; _gid=GA1.2.807899113.1629995506; _TRK_UID=a0b860d20f9b700c7c1aec08990c070f:5:4.613849625:1629995506406; _TRK_SID=d62400ee6c33cfb8a34c00b75a307b20; _TRK_CR=https%3A%2F%2Fwww.google.co.kr%2F; .AspNetCore.Cookies=CfDJ8IbdZ8JAoitLr_VBu41ix5UlTqeEWLatBz_ksKXrsfLVSkUE7npAsXPH1txoKafPUmNrjemQYyoVbWy5sZvRZXqwWkRZO_GSsT58RN_08S9Q9OC-JFcdOhULqiyYmR9sh-eU6Ibdan4Ok5xkiCvNtdl695xXxaQpBpB8a5rNQOTXMpCmsR5fNBpdF2r3ON7AKpRHiMiBjIPoRIGZKjgE0OcObrObdbOD-6jSTCAG2W4TbDJA3qZGf8e4U8pJ3P345AYl6frk0F-UFXP8gtwv9gSby2Tw8VIt4ulYy1fYx72_OKeVL-X5LdWC5AzU33EzNp_U5iDuNOd3WmSgvKWG2X08fRQ5ftRIO7qKdH0bM5lW_-JS-g4UWl0SJpyQNB0p7Gw97eupPIAp6HLR06pn0YARAAzOXJkZzfeaREbuHCznkRdqEIkhof6nUVTOkYhtydjUpIy3v5ygUswRMYu27iO6bg_Rlm4pqjKZ8RXafChHZpdNUq8pdMrBZN6n3lX6N1y3lxFDNnt-MZYYYirXNoUtf4RUnAp9BUCIOuAsKEkpgFq78V_qmoR8JSQwK49gq1cTrEau6giIFGdWDsodAsemtO_cHpwQcmGArLOFJi-UUzpLELxQYU-Np244Rahtw__m90z2kQi8T7HHDZUIL8ciLbbRQuv8M2nunmJkbNVsv7tDJxLQNyj9ZX0NX9GFfKEVlynQ-A5OdRucDBBmrBifj54oC1duqNI4yBXrUX1-N4DIsV9VLlw7GdpuRL1u31VZnrHB-cVOp8ILRaqlur0aURST03lr5tnLjI51L-oJm3hYE00Ia6zUNwUf53b37z2BvQgMU-Drr5DkgmiygNEym1tRaJAORyvyKQTY0AatsANTuOwZvrno5h1lOz2M3JJloi5h0qWb5cVGjyCDS1AYE0qYMxKtTFncLy66xbCg; _gat_gtag_UA_90943423_1=1; _TRK_EX=4' \
#   --data-raw '{"price_from":0,"price_to":1000000000,"page":1,"auc_kind":"1","auc_num":"140"}' \
#   --compressed
# '''

# print(uncurl.parse(major))

# premium='''
# curl 'https://www.k-auction.com/api/Auction/2/128' \
#   -H 'authority: www.k-auction.com' \
#   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
#   -H 'accept: */*' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
#   -H 'content-type: application/json' \
#   -H 'origin: https://www.k-auction.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://www.k-auction.com/Auction/Premium/128' \
#   -H 'accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'cookie: K-Auction.Token=1ec8523e3e974d6a9f5ece0c959200cf; _ga=GA1.2.2036382434.1628002323; _BS_GUUID=uxejjSc8YlP89qfJQxxbBJ9e3JPuIYqcvFwOxJWw; .AspNetCore.Culture=c%3Dko-KR%7Cuic%3Dko-KR; _gid=GA1.2.807899113.1629995506; _TRK_UID=a0b860d20f9b700c7c1aec08990c070f:5:4.613849625:1629995506406; _TRK_SID=d62400ee6c33cfb8a34c00b75a307b20; _TRK_CR=https%3A%2F%2Fwww.google.co.kr%2F; .AspNetCore.Cookies=CfDJ8IbdZ8JAoitLr_VBu41ix5UlTqeEWLatBz_ksKXrsfLVSkUE7npAsXPH1txoKafPUmNrjemQYyoVbWy5sZvRZXqwWkRZO_GSsT58RN_08S9Q9OC-JFcdOhULqiyYmR9sh-eU6Ibdan4Ok5xkiCvNtdl695xXxaQpBpB8a5rNQOTXMpCmsR5fNBpdF2r3ON7AKpRHiMiBjIPoRIGZKjgE0OcObrObdbOD-6jSTCAG2W4TbDJA3qZGf8e4U8pJ3P345AYl6frk0F-UFXP8gtwv9gSby2Tw8VIt4ulYy1fYx72_OKeVL-X5LdWC5AzU33EzNp_U5iDuNOd3WmSgvKWG2X08fRQ5ftRIO7qKdH0bM5lW_-JS-g4UWl0SJpyQNB0p7Gw97eupPIAp6HLR06pn0YARAAzOXJkZzfeaREbuHCznkRdqEIkhof6nUVTOkYhtydjUpIy3v5ygUswRMYu27iO6bg_Rlm4pqjKZ8RXafChHZpdNUq8pdMrBZN6n3lX6N1y3lxFDNnt-MZYYYirXNoUtf4RUnAp9BUCIOuAsKEkpgFq78V_qmoR8JSQwK49gq1cTrEau6giIFGdWDsodAsemtO_cHpwQcmGArLOFJi-UUzpLELxQYU-Np244Rahtw__m90z2kQi8T7HHDZUIL8ciLbbRQuv8M2nunmJkbNVsv7tDJxLQNyj9ZX0NX9GFfKEVlynQ-A5OdRucDBBmrBifj54oC1duqNI4yBXrUX1-N4DIsV9VLlw7GdpuRL1u31VZnrHB-cVOp8ILRaqlur0aURST03lr5tnLjI51L-oJm3hYE00Ia6zUNwUf53b37z2BvQgMU-Drr5DkgmiygNEym1tRaJAORyvyKQTY0AatsANTuOwZvrno5h1lOz2M3JJloi5h0qWb5cVGjyCDS1AYE0qYMxKtTFncLy66xbCg; _gat_gtag_UA_90943423_1=1; _TRK_EX=8' \
#   --data-raw '{"price_from":0,"price_to":52000000,"page":1,"auc_kind":"2","auc_num":"128"}' \
#   --compressed
# '''

# print(uncurl.parse(premium))

JSON_SAVE_PATH = '/mnt/auc/datas/que/k'
IMAGE_SAVE_PATH = '/mnt/auc/images/k'

class KAuctionRequester():
    def __init__(self):
        global JSON_SAVE_PATH,IMAGE_SAVE_PATH
        self.session = requests.Session()
       

    def __setSessionInfo(self):
        pass

    def getAuctionResult(self,no,json_base_path, auctiontype, writeAsFile=True):
        try:
            data_params = {
            'weekly':{
                'param':{"price_from":0,"price_to":1000000000,"page":1,"auc_kind":"4","auc_num":str(no)},
                'url':f"https://www.k-auction.com/api/Auction/4/{no}",
                'referer':f"https://www.k-auction.com/Auction/Weekly/{no}"
            },
            'major':{            
                'param':{"price_from":0,"price_to":1000000000,"page":1,"auc_kind":"1","auc_num":str(no)},
                'url':f'https://www.k-auction.com/api/Auction/1/{no}',
                'referer':f'https://www.k-auction.com/Auction/Major/{no}'
            },
            'premium':{            
                'param':{"price_from":0,"price_to":1000000000,"page":1,"auc_kind":"2","auc_num":str(no)},
                'url':f'https://www.k-auction.com/api/Auction/2/{no}',
                'referer':f'https://www.k-auction.com/Auction/Premium/{no}'
            },
            }
            kor_data = []
            eng_data = []
            i = 1   
            flag = True    
            while flag:               
                print(f'==============load page {i}==============')
                #data_param = {"price_from":0,"price_to":100000000,"page":1,"auc_kind":"4","auc_num":str(no)}
                data_param = data_params[auctiontype]['param']
                url = data_params[auctiontype]['url']
                referer = data_params[auctiontype]['referer']
                data_param['page']=i
                data_param_str = json.dumps(data_param)
                cultures= [
                    {"lang":"eng", "Culture":"c%3Den-US%7Cuic%3Den-US","TRK_EX":"14"}
                     ,{"lang":'kor',"Culture":"c%3Dko-KR%7Cuic%3Dko-KR","TRK_EX":"15"}
                    ]
                for c in cultures:
                    lang,cul,trk = c['lang'],c['Culture'],c['TRK_EX']
                    res = requests.post(url,
                                data=data_param_str,
                                headers={
                                    "Accept": "*/*",
                                    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                                    "Connection": "keep-alive",
                                    "Content-Type": "application/json",
                                    "Origin": "https://www.k-auction.com",
                                    "Referer": referer,
                                    "Sec-Fetch-Dest": "empty",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Site": "same-origin",
                                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
                                    "sec-ch-ua-mobile": "?0"
                                },
                                cookies={
                                    ".AspNetCore.Cookies": "CfDJ8Go3F9LXhqNHnmEE9fnBWD7wLHLnrnFBEl1IDcZBlrAW5G_YZ_3ZgU1Js1CNymfgHhrkHe9WtmRTjTW9wVsyELPRzkvjDzXo_UWP9mTY0hAMnfqj_JMbwvhPmfxAolyG253dHb79tAkVVEqPMN9hFuHuMsdft21Q7hRHiTeNOYrs3VJUt3zjBBkzlOmh9Bk06ANFbp4g94HJasOrm2xa6vgKwf-mQQa_kY59vyKjrvRrDh3za4PlAAUpc_8qRfoVYyRgtH7cewpCBlt-_sXAFyzY5VUcEDJfNo_uW6YCrNjI5XIYhw48KfTqoOHtD4Y_kPlVnI8Sezim7yemTMTG4LabLxVD-edNzfKWrrfH5rhVSc8yw-DwMFgrBBsCLxuhuF8s5IHJLxmEy05UIKUfyKa3brKbo0IGr7HkKg6prdlki64lOlWM1WcDY-If--YsqAS-nJ60MjR7Imf3c8ZUj8RKJNXXBwu0KjNS1g1bDwhaenRoR4wyt1Wewcumc9lshSDl05GqBTPTRO-ICU3_VIiIlkkGekQqsQ6ribvMdbzTV9b8stjTqaCmSPg2pZNKgxUjrWn6ULQAXwXk8LxlU5xOIbVxwZo0nSBK1smrmwDmY0MrraBJ4OxUMY2vFCyhc2G6DJtMC1BVEy_xL4zSeYzoIRl57tLAEHULfhsGxe1Km8hCLsqCsZznyuQBoCxJTlMvH5SsAmDX21cSAU0KkEGKovYLktEaLqTlSOMiOLl1gmSS-WfqIizIddzdXEKQbvEhJOH4Aif6M2TJe8Yjylms1yq82EK8QoyeZvB7Q3VihvqfSLZll14yq0ZWb6EDRAWenDw5-XJkCM32kdZoQsfdKjdDx3uTI13UAiqVl0RcZrLDcSmWAholAx9C4boDZey3kOEXRfw3OjfZSa5eb1LoobmXgK1ZBsjToHdogxfN",
                                    ".AspNetCore.Culture": cul,
                                    "K-Auction.Token": "72b82788b73843e392870e6429c87b5f",
                                    "_BS_GUUID": "M7E2S8ctbljVUcxcI9foeHMnH2q2l237aIa2Qnw2",
                                    "_TRK_CR": "https%3A%2F%2Fwww.k-auction.com%2Fnotify-HTTPS_Notice%3FaHR0cHM6Ly93d3cuay1hdWN0aW9uLmNvbS8=",
                                    "_TRK_EX": "4",
                                    "_TRK_SID": "4128f78f055ee710efefd1314d9ed3ed",
                                    "_TRK_UID": "10f7813b2850ac576d3093e0cc94fb72:1:0:1627975671726",
                                    "_ga": "GA1.2.1805053168.1627975672",
                                    "_gat_gtag_UA_90943423_1": "1",
                                    "_gid": "GA1.2.1540520634.1627975672",
                                    "notified-HTTPS_Notice": "1"
                                },
                                auth=(),
                            )
                    if res.status_code==200:
                        data_json = res.json()
                        auction_results = data_json['data']
                        if len(auction_results) == 0:
                            flag = False
                            break
                        else:
                            if lang =='eng':
                                eng_data.extend(auction_results)
                            else:
                                kor_data.extend(auction_results)
                    time.sleep(0.2)
                i+=1     

            final_result = {'kor':kor_data,'eng':eng_data}
            if writeAsFile:
                p = os.path.join(json_base_path,auctiontype,f'{no}.json')                
                with open(p,'w') as j:
                    json.dump(final_result,j)
            return final_result
        except Exception as e:
            print(e)
            raise e

    #https://images.k-auction.com/www/Konline/Work/0273/27300301001_L.jpg
    @staticmethod
    def downloadArtImages(no,json_base_path, image_base_path, auctiontype):
        try:
            data_path = f'{json_base_path}/{auctiontype}/{no}.json'
            with open(data_path) as f:
                data = json.load(f)
            samples = data['kor']
            for sample in samples:
                lot_no,image_path = sample['lot_num'],sample['img_file_name']
                no4 = ('0000'+str(no))[-4:]
                u = f'https://images.k-auction.com/www/Konline/Work/{no4}/{image_path}'                
                #print(u)
                response = requests.get(u,stream=True)
                #print('success to access to image')
                if response.status_code==200:
                    dest_folder = f'{image_base_path}/{auctiontype}/{no}'
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder,exist_ok=True)
                    file_path = os.path.join(dest_folder,f'LOT{lot_no}_{image_path}')
                    with open(file_path,'wb') as f:
                        for chunk in response:
                            f.write(chunk)
                else:
                    pass
        except Exception as e:
            print(e)
            pass



def fetchDatas(numlist:list,json_base_path,image_base_path):    
    auctiontypes = ['weekly','major','premium']
    auctiontypes = ['major','premium']
    k = KAuctionRequester()
    for i in numlist:
        for a in auctiontypes:
            try:
                print(f' {a} [kauction no {i}]')
                k.getAuctionResult(i,json_base_path,a)
                KAuctionRequester.downloadArtImages(i,json_base_path,image_base_path,a)
            except Exception as e:
                raise e
