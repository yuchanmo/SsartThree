import os
import json
from typing import NamedTuple
import pandas as pd
from collections import namedtuple
from models.artinfo import art,Art
from pprint import pprint
import re


def parseDataForInsert(f:str, data:list,cate:str):    
    art_list = []    
    for k,e in data:
        try:
            a = Art()
            a.auction_site = 'k'
            a.auction_url_num = int(f.split('\\')[-1].split('.')[0])
            a.auction_place = ''
            a.auction_date = k.get('auc_end_date','') 
            a.artist_name_kor = k.get('artist_name','') 
            a.artist_name_eng = e.get('artist_name','') 
            a.artist_comment = ''
            a.lot_no =k.get('lot_no',0)
            a.make_year = k.get('make_date','TBD')
            a.title_kor = k.get('title','')
            a.title_eng = e.get('title','')
            a.currency = k.get('currency','')
            a.money = k.get('price_hammer',0.0)
            size = k.get('size','')
            size_pattern = r'[\d\.]+'
            nums = re.findall(size_pattern,size)
            length = nums[0] if len(nums)>=2 else 0.0
            width = nums[1] if len(nums)>=2 else 0.0
            a.unit_cd = 'cm' if 'cm' in size else ''
            a.size_length =length
            a.size_width =width
            a.mix_cd = 0.0
            a.mix_size =0.0
            a.canvas = k.get('size','')
            a.medium_eng = e.get('material','')
            a.medium_kor = k.get('material','')
            a.description = ''# k.get('desc','')
            a.estimate_high = k.get('price_estimated_high',0.0)
            a.estimate_low = k.get('price_estimated_low',0.0)
            a.edition = k.get('edition','')      
            a.image_name = k.get('img_file_name','') 
            a.auction_cate = cate
            direct_date = k.get('direct_date','')
            direct_date = direct_date.replace('b.','').replace('/',',').replace('·',',').replace('&',',') if type(direct_date) == str else ' '
            direct_date = direct_date.split(',')[0] if ',' in direct_date else direct_date
            birth,death = direct_date.split('-') if '-' in direct_date else [direct_date,' ']
            a.birth = birth
            a.death = death
            tmp = a.__dict__            
            art_list.append(tmp)
        except Exception as e:
            print(e)
            pass
    print(len(art_list))
    return art_list


#if __name__ =='__main__':
from glob import glob
p = r'F:\art\auc\datas\que\k'
folders = [(c,os.path.join(p,c)) for c in os.listdir(p)]


rows_list=[]

for c,folder in folders:
    tmp = folder +'/*'
    files = glob(tmp)
    for f in  list(filter(lambda x : '110.json',files)):
        try:
            print(f)
            with open(f,'r') as jf:
                data = json.load(jf)
            pairs = [(k,e) for k,e in zip(data['kor'],data['eng'])]
            rows = parseDataForInsert(f,pairs,c)        
            rows_list.extend(rows)
        except Exception as e:
            pass

len(rows_list)

df = pd.DataFrame(rows_list)
df.to_csv('k_20211003.csv',encoding='utf-8-sig')

