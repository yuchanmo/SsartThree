import requests
u = 'https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=644#page1'
res = requests.get(u)
res.status_code
res.text
open('t.html','w').write(res.text)


ru = 'https://www.seoulauction.com/api/actionSet'
h ={
    'Referer':'https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=644',
    'Cookie': 'notified-HTTPS_Notice=1; JSESSIONID=C6F53CC9F65946F25CB02262280B6C83.was2; sale_no=644; curr_url=/WEB-INF/views/sale/lotList.jsp; prev_url=/WEB-INF/views/sale/lotList.jsp; wcs_bt=19656f7bcf4c5c:1627879504; reqRowCnt=20; sortBy=LOTAS'
} 

hh ={   
'Host': 'www.seoulauction.com',
'Connection': 'keep-alive',
'Content-Length': '1307',
'Accept': 'application/json, text/plain, */*',
'X-CSRF-TOKEN': 'fecef3e5-d716-4169-afda-e73da0ba6af6',
'Content-Type': 'application/json; charset=UTF-8',
'Origin': 'https://www.seoulauction.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=644',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'notified-HTTPS_Notice=1; JSESSIONID=C6F53CC9F65946F25CB02262280B6C83.was2; sale_no=644; curr_url=/WEB-INF/views/sale/lotList.jsp; prev_url=/WEB-INF/views/sale/lotList.jsp; wcs_bt=19656f7bcf4c5c:1627879504; reqRowCnt=20; sortBy=LOTAS'
}


rr = requests.post(ru,headers=hh)
rr.status_code

'''POST /api/actionSet HTTP/1.1
Host: www.seoulauction.com
Connection: keep-alive
Content-Length: 1307
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
Accept: application/json, text/plain, */*
X-CSRF-TOKEN: fecef3e5-d716-4169-afda-e73da0ba6af6
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Content-Type: application/json; charset=UTF-8
Origin: https://www.seoulauction.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.seoulauction.com/saleDetail?view_id=RESULT_AUCTION&sale_no=644
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: notified-HTTPS_Notice=1; JSESSIONID=C6F53CC9F65946F25CB02262280B6C83.was2; sale_no=644; curr_url=/WEB-INF/views/sale/lotList.jsp; prev_url=/WEB-INF/views/sale/lotList.jsp; wcs_bt=19656f7bcf4c5c:1627879504; reqRowCnt=20; sortBy=LOTAS
'''

#https://stackoverflow.com/questions/53032456/login-with-python-requests-and-csrf-token

from urllib.parse import urljoin
login_url = urljoin('https://www.seoulauction.com/login?logout','/processLogin')
https://www.seoulauction.com/processLogin
lh = '''
POST /processLogin HTTP/1.1
Host: www.seoulauction.com
Connection: keep-alive
Content-Length: 94
Cache-Control: max-age=0
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://www.seoulauction.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.seoulauction.com/login?logout
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: notified-HTTPS_Notice=1; sale_no=644; JSESSIONID=6B6BBBA7AB06397E9AEFE5903F02403C.was2; curr_url=/WEB-INF/views/customer/login.jsp; prev_url=/WEB-INF/views/customer/login.jsp; wcs_bt=19656f7bcf4c5c:1627881653
'''


lh = {
'Host': 'www.seoulauction.com',
'Origin': 'https://www.seoulauction.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Referer':'https://www.seoulauction.com/login?logout',
'Cookie': 'notified-HTTPS_Notice=1; sale_no=644; JSESSIONID=6B6BBBA7AB06397E9AEFE5903F02403C.was2; curr_url=/WEB-INF/views/customer/login.jsp; prev_url=/WEB-INF/views/customer/login.jsp; wcs_bt=19656f7bcf4c5c:1627881653',
}

ss = requests.Session()
i = {
    'loginId':'densetsu',
    'password':'ahdbapwk55*',
    'targetUrl': '/',
    '_csrf':'54711bb3-231a-4386-ad62-30f3'
}
ss.post(login_url,data=i,headers=lh)

#value="54711bb3-231a-4386-ad62-30f3b7544f59"