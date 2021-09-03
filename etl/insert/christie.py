class Art(object):
    def __init__(self):  
        self.auction_site:str = ''
        self.lot:str = ''
        self.auction_date:str = ''
        self.name_en:str = ''
        self.title_eng:str = ''
        self.currency:str = ''             
        self.money:str = ''                
        self.estimate_high:float = ''            
        self.estimate_low:float = '' 
        self.image_name:str = '' 
        self.description_txt:str = ''    
        self.file:str =''

import os
import json
from typing import NamedTuple
import pandas as pd
from collections import namedtuple
# from models.artinfo import art,Art
from pprint import pprint
# from utils.dbcon import engine


def parseDataForInsert(f:str, data:dict):  
    print(f)    
    art_list = []
#     for art in arts:    
    try:
        arts =  data['lots']['data']['lots']
        
    except:      
        
        arts =  data['data']['lots']    
        
    for art in arts: 
        a = Art()
        a.auction_site = 'christies'   
        a.lot = art['lot_id_txt']
        a.auction_date = art['end_date']
        a.name_en = art['title_primary_txt']
        a.title_eng = art['title_secondary_txt']
        a.currency = art['estimate_txt'].split(' ')[0]      
        money_split = art['price_realised_txt'].split(' ')
        if money_split[0]: a.money = money_split[1] 
        else: a.money = '' 
        a.estimate_high = art['estimate_high']        
        a.estimate_low = art['estimate_low']

        images = art['image']
        a.image_name = images.get('image_mobile_src','')        
        a.description_txt = art['description_txt']        
        a.file = f
        art_list.append(a.__dict__)

    print(len(art_list))

    return art_list

p = '/mnt/auc/datas/que/christies'
rows_list=[]


for f in os.listdir(p):
    try:
        path = p+'/'+f
        print(path)
        with open(path,'rt', encoding='UTF8') as jf:
            data = json.load(jf)
        rows = parseDataForInsert(f,data)
        rows_list.extend(rows)    
    except Exception as e:
        pass

import matplotlib.pyplot as plt

df = pd.DataFrame(rows_list)

from bs4 import BeautifulSoup
df['desc'] = df['description_txt'].apply(lambda c :' '.join(BeautifulSoup(c, "html.parser").findAll(text=True)).split('\n'))
df['desc_len'] = df['desc'].apply(lambda x : len(x))
print(df[df['desc_len']==166].iloc[0]['description_txt'])
df['desc_len'].min()
df['desc'].dtype
print()
from collections import Counter

Counter(df['desc_len'].tolist()

for i in df.iloc[69548]['desc']:
    print(i)

df.iloc[69548]['description_txt']