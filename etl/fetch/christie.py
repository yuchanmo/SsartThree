from bs4 import BeautifulSoup
import requests
import re
import json
from pprint import pprint
import pandas as pd
import os

def getJson(link_url:str):
    try:
        #link_url = 'https://www.christies.com/Latin-American-Art-Online-28907.aspx?lid=1'
        res = requests.get(link_url)
        url = res.url
        final_url = f'{url}' #+'?filters=&page=20&searchphrase=&sortby=LotNumber&themes='
        all_html = requests.get(final_url).content
        bs = BeautifulSoup(all_html,'html.parser')
        ss = bs.find_all('script')
        data = str(ss[7].string)
        pt = 'window.chrComponents = (.*?);'
        json_string = re.search(pt,data)
        sp,ep = json_string.span()
        art_data = json.loads(data[sp+23:-3])
        return art_data
    except Exception as e:
        return {}

dest_path =r'/mnt/auc/christies' 

df = pd.read_csv(r'/home/fakeblocker/code/python/Auc/cr.txt')
urls = df['url'].to_list()
urls[0].split('/')[-1].split('.aspx')[0]
for u in urls:
    try:
        print(u)
        filename = u.split('/')[-1].split('.aspx')[0]
        dest_path = os.path.join(dest_path,filename+'.json')
        tmp = getJson(u)
        open(dest_path,'w').write(json.dumps(tmp))
    except Exception as e:
        pass