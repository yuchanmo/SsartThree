import uncurl

kauction_curl ='''
curl 'https://www.k-auction.com/api/Auction/4/273' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  -H 'Accept: */*' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://www.k-auction.com' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://www.k-auction.com/Auction/Weekly/273' \
  -H 'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Cookie: K-Auction.Token=72b82788b73843e392870e6429c87b5f; notified-HTTPS_Notice=1; _BS_GUUID=M7E2S8ctbljVUcxcI9foeHMnH2q2l237aIa2Qnw2; _TRK_UID=10f7813b2850ac576d3093e0cc94fb72:1:0:1627975671726; _TRK_SID=4128f78f055ee710efefd1314d9ed3ed; _TRK_CR=https%3A%2F%2Fwww.k-auction.com%2Fnotify-HTTPS_Notice%3FaHR0cHM6Ly93d3cuay1hdWN0aW9uLmNvbS8=; _ga=GA1.2.1805053168.1627975672; _gid=GA1.2.1540520634.1627975672; _gat_gtag_UA_90943423_1=1; .AspNetCore.Cookies=CfDJ8Go3F9LXhqNHnmEE9fnBWD7wLHLnrnFBEl1IDcZBlrAW5G_YZ_3ZgU1Js1CNymfgHhrkHe9WtmRTjTW9wVsyELPRzkvjDzXo_UWP9mTY0hAMnfqj_JMbwvhPmfxAolyG253dHb79tAkVVEqPMN9hFuHuMsdft21Q7hRHiTeNOYrs3VJUt3zjBBkzlOmh9Bk06ANFbp4g94HJasOrm2xa6vgKwf-mQQa_kY59vyKjrvRrDh3za4PlAAUpc_8qRfoVYyRgtH7cewpCBlt-_sXAFyzY5VUcEDJfNo_uW6YCrNjI5XIYhw48KfTqoOHtD4Y_kPlVnI8Sezim7yemTMTG4LabLxVD-edNzfKWrrfH5rhVSc8yw-DwMFgrBBsCLxuhuF8s5IHJLxmEy05UIKUfyKa3brKbo0IGr7HkKg6prdlki64lOlWM1WcDY-If--YsqAS-nJ60MjR7Imf3c8ZUj8RKJNXXBwu0KjNS1g1bDwhaenRoR4wyt1Wewcumc9lshSDl05GqBTPTRO-ICU3_VIiIlkkGekQqsQ6ribvMdbzTV9b8stjTqaCmSPg2pZNKgxUjrWn6ULQAXwXk8LxlU5xOIbVxwZo0nSBK1smrmwDmY0MrraBJ4OxUMY2vFCyhc2G6DJtMC1BVEy_xL4zSeYzoIRl57tLAEHULfhsGxe1Km8hCLsqCsZznyuQBoCxJTlMvH5SsAmDX21cSAU0KkEGKovYLktEaLqTlSOMiOLl1gmSS-WfqIizIddzdXEKQbvEhJOH4Aif6M2TJe8Yjylms1yq82EK8QoyeZvB7Q3VihvqfSLZll14yq0ZWb6EDRAWenDw5-XJkCM32kdZoQsfdKjdDx3uTI13UAiqVl0RcZrLDcSmWAholAx9C4boDZey3kOEXRfw3OjfZSa5eb1LoobmXgK1ZBsjToHdogxfN; _TRK_EX=4' \
  --data-raw '{"price_from":0,"price_to":6000000,"page":1,"auc_kind":"4","auc_num":"273"}' \
  --compressed'''

print(uncurl.parse(kauction_curl))

import requests

res = requests.post("https://www.k-auction.com/api/Auction/4/173",
    data='{"price_from":0,"price_to":6000000,"page":1,"auc_kind":"4","auc_num":"173"}',
    headers={
        "Accept": "*/*",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.k-auction.com",
        "Referer": "https://www.k-auction.com/Auction/Weekly/272",
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
).json()
from pprint import pprint
pprint(res)