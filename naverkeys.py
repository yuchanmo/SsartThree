import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,urlunparse,urlparse,unquote
import pandas as pd
import parmap
import multiprocessing
from multiprocessing import Manager
num_cores = multiprocessing.cpu_count() 

def keywordShoppinPanNumber(query:str):
    #query = '블라인드'
    try:
        url = f'https://m.search.naver.com/search.naver?sm=mtp_sly.hst&where=m&query={quote(query)}&acr=1'
        res = requests.get(url)
        html = res.text
        b =BeautifulSoup(html,'html.parser')
        sections = b.select('section')
        i = 0 
        res_cnt = -1
        for s in sections:            
            if ('sp_nshop' in s['class']):
                res_cnt = i
                break
            if i > 5:
                res_cnt = -1
                break
            i+=1
        return (query,res_cnt)
    except Exception as e:
        return (query,-1)

def keywordShoppinPanNumberForMultiProcessing(query:str,rlist):
    try:
        t = keywordShoppinPanNumber(query)
        rlist.append(t)
    except Exception as e:
        print(e)
        pass

import os 
pp = r'/home/fakeblocker/code/python/Auc/naver'
if __name__ == '__main__':
    num_cores = multiprocessing.cpu_count() 
    print('cpu nums : ',num_cores)
    manager = Manager()
    i = 1
    chunks = pd.read_csv('keys.txt',chunksize=100)
    for df in chunks:
        reslist = manager.list()
        keywords = df['keyword'].to_list()
        parmap.map(keywordShoppinPanNumberForMultiProcessing,keywords,reslist,pm_pbar=True,pm_processes=num_cores)
        tmp_df = pd.DataFrame(list(reslist),columns=['keyword','pos'])
        tmp_df.head()
        filepath = os.path.join(pp,f'{str(i)}.txt')
        tmp_df.to_csv(filepath)
        print(i*100)
        i+=1