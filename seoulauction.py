import requests
import time
import os


# seoul_acution_cur_ver ='''
# curl 'https://www.seoulauction.com/api/actionSet' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'X-CSRF-TOKEN: 35a3c8c4-b38d-4e00-bf09-9237b5236ef3' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
#   -H 'Content-Type: application/json; charset=UTF-8' \
#   -H 'Origin: https://www.seoulauction.com' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=652' \
#   -H 'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'Cookie: notified-HTTPS_Notice=1; JSESSIONID=A1E47CE54CC9537EADDD04A358BEC520.was2; sale_no=652; curr_url=/WEB-INF/views/sale/lotList.jsp; prev_url=/WEB-INF/views/sale/lotList.jsp; wcs_bt=19656f7bcf4c5c:1627969637; reqRowCnt=20; sortBy=LOTAS' \
#   --data-raw '{"baseParms":{"sale_no":"652","expe_from_price":null,"expe_to_price":null,"cate_cds":null,"scate_cds":null,"mate_cds":null,"hashtag_list":null,"fav_cds_list":null},"actionList":[{"actionID":"sale_info","actionType":"select","tableName":"SALE"},{"actionID":"exch_rate_list","actionType":"select","tableName":"EXCH"},{"actionID":"lot_list_count","actionType":"select","tableName":"LOT_CNT","parmsList":[{"for_count":true}]},{"actionID":"lot_list_paging","actionType":"select","tableName":"LOTS","parmsList":[{"from":0,"rows":20,"sale_outside_yn":"N","sort_by":"LOTAS"}]},{"actionID":"get_customer_by_cust_no","actionType":"select","tableName":"CUST_INFO","parmsList":[]},{"actionID":"saleLot_category","actionType":"select","tableName":"CATEGORY"},{"actionID":"saleLot_subcategory","actionType":"select","tableName":"SUBCATEGORY"},{"actionID":"saleLot_material","actionType":"select","tableName":"MATERIAL"},{"actionID":"saleLot_artist","actionType":"select","tableName":"ARTIST"},{"actionID":"saleLot_hashtag","actionType":"select","tableName":"HASHTAG"},{"actionID":"saleHighlight_List","actionType":"select","tableName":"LOT_HIGHLIGHT"},{"actionID":"sale_cert_info","actionType":"select","tableName":"CERT"},{"actionID":"my_paddle_check","actionType":"select","tableName":"PADDLE_CHECK","parmsList":[{}]}]}' \
#   --compressed
#   '''

# import uncurl
# print(uncurl.parse(seoul_acution_cur_ver))

# from pprint import pprint

res = requests.post("https://www.seoulauction.com/api/actionSet",
    data='{"baseParms":{"sale_no":"652","expe_from_price":null,"expe_to_price":null,"cate_cds":null,"scate_cds":null,"mate_cds":null,"hashtag_list":null,"fav_cds_list":null},"actionList":[{"actionID":"sale_info","actionType":"select","tableName":"SALE"},{"actionID":"exch_rate_list","actionType":"select","tableName":"EXCH"},{"actionID":"lot_list_count","actionType":"select","tableName":"LOT_CNT","parmsList":[{"for_count":true}]},{"actionID":"lot_list_paging","actionType":"select","tableName":"LOTS","parmsList":[{"from":0,"rows":200,"sale_outside_yn":"N","sort_by":"LOTAS"}]},{"actionID":"get_customer_by_cust_no","actionType":"select","tableName":"CUST_INFO","parmsList":[]},{"actionID":"saleLot_category","actionType":"select","tableName":"CATEGORY"},{"actionID":"saleLot_subcategory","actionType":"select","tableName":"SUBCATEGORY"},{"actionID":"saleLot_material","actionType":"select","tableName":"MATERIAL"},{"actionID":"saleLot_artist","actionType":"select","tableName":"ARTIST"},{"actionID":"saleLot_hashtag","actionType":"select","tableName":"HASHTAG"},{"actionID":"saleHighlight_List","actionType":"select","tableName":"LOT_HIGHLIGHT"},{"actionID":"sale_cert_info","actionType":"select","tableName":"CERT"},{"actionID":"my_paddle_check","actionType":"select","tableName":"PADDLE_CHECK","parmsList":[{}]}]}',
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
        "X-CSRF-TOKEN": "35a3c8c4-b38d-4e00-bf09-9237b5236ef3",
        "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "sec-ch-ua-mobile": "?0"
    },
    cookies={
        "JSESSIONID": "A1E47CE54CC9537EADDD04A358BEC520.was2",
        "curr_url": "/WEB-INF/views/sale/lotList.jsp",
        "notified-HTTPS_Notice": "1",
        "prev_url": "/WEB-INF/views/sale/lotList.jsp",
        "reqRowCnt": "1000",
        "sale_no": "652",
        "sortBy": "LOTAS",
        "wcs_bt": "19656f7bcf4c5c:1627969637"
    },
    auth=(),
).json()
import json
res['tables'].keys()
json.dumps(res['tables'])