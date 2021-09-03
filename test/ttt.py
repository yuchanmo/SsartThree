import requests
requests.post("https://www.k-auction.com/api/Auction/1/140",
    data='{"price_from":0,"price_to":1000000000,"page":1,"auc_kind":"2","auc_num":"140"}',
    headers={
        "accept": "*/*",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "authority": "www.k-auction.com",
        "content-type": "application/json",
        "origin": "https://www.k-auction.com",
        "referer": "https://www.k-auction.com/Auction/Major/140",
        "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    },
    cookies={
        ".AspNetCore.Cookies": "CfDJ8IbdZ8JAoitLr_VBu41ix5UlTqeEWLatBz_ksKXrsfLVSkUE7npAsXPH1txoKafPUmNrjemQYyoVbWy5sZvRZXqwWkRZO_GSsT58RN_08S9Q9OC-JFcdOhULqiyYmR9sh-eU6Ibdan4Ok5xkiCvNtdl695xXxaQpBpB8a5rNQOTXMpCmsR5fNBpdF2r3ON7AKpRHiMiBjIPoRIGZKjgE0OcObrObdbOD-6jSTCAG2W4TbDJA3qZGf8e4U8pJ3P345AYl6frk0F-UFXP8gtwv9gSby2Tw8VIt4ulYy1fYx72_OKeVL-X5LdWC5AzU33EzNp_U5iDuNOd3WmSgvKWG2X08fRQ5ftRIO7qKdH0bM5lW_-JS-g4UWl0SJpyQNB0p7Gw97eupPIAp6HLR06pn0YARAAzOXJkZzfeaREbuHCznkRdqEIkhof6nUVTOkYhtydjUpIy3v5ygUswRMYu27iO6bg_Rlm4pqjKZ8RXafChHZpdNUq8pdMrBZN6n3lX6N1y3lxFDNnt-MZYYYirXNoUtf4RUnAp9BUCIOuAsKEkpgFq78V_qmoR8JSQwK49gq1cTrEau6giIFGdWDsodAsemtO_cHpwQcmGArLOFJi-UUzpLELxQYU-Np244Rahtw__m90z2kQi8T7HHDZUIL8ciLbbRQuv8M2nunmJkbNVsv7tDJxLQNyj9ZX0NX9GFfKEVlynQ-A5OdRucDBBmrBifj54oC1duqNI4yBXrUX1-N4DIsV9VLlw7GdpuRL1u31VZnrHB-cVOp8ILRaqlur0aURST03lr5tnLjI51L-oJm3hYE00Ia6zUNwUf53b37z2BvQgMU-Drr5DkgmiygNEym1tRaJAORyvyKQTY0AatsANTuOwZvrno5h1lOz2M3JJloi5h0qWb5cVGjyCDS1AYE0qYMxKtTFncLy66xbCg",
        ".AspNetCore.Culture": "c%3Dko-KR%7Cuic%3Dko-KR",
        "K-Auction.Token": "1ec8523e3e974d6a9f5ece0c959200cf",
        "_BS_GUUID": "uxejjSc8YlP89qfJQxxbBJ9e3JPuIYqcvFwOxJWw",
        "_TRK_CR": "https%3A%2F%2Fwww.google.co.kr%2F",
        "_TRK_EX": "4",
        "_TRK_SID": "d62400ee6c33cfb8a34c00b75a307b20",
        "_TRK_UID": "a0b860d20f9b700c7c1aec08990c070f:5:4.613849625:1629995506406",
        "_ga": "GA1.2.2036382434.1628002323",
        "_gat_gtag_UA_90943423_1": "1",
        "_gid": "GA1.2.807899113.1629995506"
    },
    auth=(),
).text