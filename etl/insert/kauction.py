import os
import json
from typing import NamedTuple
import pandas as pd
from collections import namedtuple
from models.artinfo import art,Art
from pprint import pprint
import re


def parseDataForInsert(f:str, data:list):    
    art_list = []    
    for k,e in data:
        try:
            a = Art()
            a.auction_site = 'k'
            a.auction_url_num = int(f.split('/')[-1].split('.')[0])
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
            art_list.append(a.__dict__)
        except Exception as e:
            print(e)
            pass
    print(len(art_list))
    return art_list


if __name__ =='__main__':

    p = r'/mnt/auc/k'
    files = [(i,os.path.join(p,str(i)+'.json')) for i in range(1,274)]
    rows_list=[]
    for i,f in files:
        try:
            with open(f,'r') as jf:
                data = json.load(jf)
            pairs = [(k,e) for k,e in zip(data['kor'],data['eng'])]
            rows = parseDataForInsert(f,pairs)        
            rows_list.extend(rows)
        except Exception as e:
            pass



df = pd.DataFrame(rows_list)
df.to_csv('k_final.csv',encoding='utf-8-sig')

