from bs4 import BeautifulSoup
import requests
import re
import json
from pprint import pprint
import pandas as pd
import os
from itertools import chain
from urllib.parse import urlparse
#from utils.writer import *



def writeDataAsFile(filepath,data):
    try:
        with open(filepath,'w') as f:
            if type(data) == dict:
                f.write(json.dumps(data))
            elif type(data) == str:
                f.write(data)
            else:
                raise Exception
        print('success')
        return True
    except Exception as e:
        print('fail')
        return False


def getJson(link_url:str):
    try:
        #link_url = 'https://www.christies.com/Latin-American-Art-Online-28907.aspx?lid=1'
        res = requests.get(link_url)
        url = res.url
        parsed_url = urlparse(url)
        if len(parsed_url.query) == 0:
            final_url = f'{url}' +'?filters=&page=30&searchphrase=&sortby=LotNumber&themes=' 
        elif (len(parsed_url.query)>0) and ('page=' in parsed_url.query):
            final_url = url.replace('page=','page=30')
        elif (len(parsed_url.query)>0) and ('page=' not in parsed_url.query):
            final_url = url+'&page=30'
        else:
            raise Exception
        all_html = requests.get(final_url).content
        bs = BeautifulSoup(all_html,'html.parser')
        ss = bs.find_all('script')
        pts = ['{"header":{"data":{"header":{"language":(.*?)};','{"data":{"save_lot_api_endpoint":(.*?)};']        
        data_search_groups = chain.from_iterable([list(map(lambda x : re.search(pt,str(x.string)),ss)) for pt in pts])
        data = list(filter(lambda x : x!=None,data_search_groups))[0]
        json_string = data.group()[:-1]        
        return json_string
    except Exception as e:
        print(e)
        return {}



dest_path =r'/mnt/auc/christies' 
df = pd.read_csv(r'/home/fakeblocker/code/python/Auc/cr.txt')
urls = df['url'].to_list()
for url in urls:    
    
    fn = url.split('/')[-1].split('.aspx')[0]
    link_url = url
    print('===============',fn,f'({url})===============')
    file_fullpath = os.path.join(dest_path,fn+'.json')
    tmp = getJson(link_url)
    writeDataAsFile(file_fullpath,tmp)

# link_url = 'https://www.christies.com/The-BJ-Eastwood-Collection-29444.aspx?lid=1'
# res = requests.get(link_url)
# url = res.url
# parsed_url = urlparse(url)
# if len(parsed_url.query) == 0:
#     final_url = f'{url}' +'?filters=&page=30&searchphrase=&sortby=LotNumber&themes=' 
# elif (len(parsed_url.query)>0) and ('page=' in parsed_url.query):
#     final_url = url.replace('page=','page=30')
# elif (len(parsed_url.query)>0) and ('page=' not in parsed_url.query):
#     final_url = url+'&page=30'

# else:
#     raise Exception
# all_html = requests.get(final_url).content
# bs = BeautifulSoup(all_html,'html.parser')

# open('tetetet.html','wb').write(all_html)

# ss = bs.find_all('script')
# pts = ['{"header":{"data":{"header":{"language":(.*?)};','{"data":{"save_lot_api_endpoint":(.*?)};']        
# data_search_groups = chain.from_iterable([list(map(lambda x : re.search(pt,str(x.string)),ss)) for pt in pts])
# data = list(filter(lambda x : x!=None,data_search_groups))[0]
# json_string = data.group()        
# final_url = f'{url}' #+'?filters=&page=20&searchphrase=&sortby=LotNumber&themes='
# all_html = requests.get(final_url).content
# bs = BeautifulSoup(all_html,'html.parser')
# ss = bs.find_all('script')
# len(ss)
# data = str(ss[7].string)
# writeDataAsFile(fn+'.txt',data)
# a = list(filter(lambda x : re.search(pt,str(x.string)) !=None,ss))
# ss = bs.find_all('script')
# pt = ' {"header":{"data":{"header":{"language":(.*?)"method":"POST"}}}};'
# data_search_groups = map(lambda x : re.search(pt,str(x.string)),ss)
# data = list(filter(lambda x : x!=None,data_search_groups))[0]
# data.group()

# for u in urls:
#     try:
#         print(u)
#         filename = u.split('/')[-1].split('.aspx')[0]
#         dest_path = os.path.join(dest_path,filename+'.json')
#         tmp = getJson(u)
#         open(dest_path,'w').write(json.dumps(tmp))
#     except Exception as e:
#         pass