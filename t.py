# import os
# import json
# from typing import NamedTuple
# import pandas as pd
# from collections import namedtuple
# from models.artinfo import art,Art
# from pprint import pprint


# def parseDataForInsert(f:str, data:dict):
#     arts =  data['tables']['LOTS']['rows']
#     sales = data['tables']['SALE']['rows']
#     art_list = []
#     sale = sales[0]
#     for art in arts:
#         try:
#             a = Art()
#             a.auction_site = 'seoul'
#             a.auction_url_num = int(f.split('/')[-1].split('.')[0])
#             a.auction_place = sale['PLACE_JSON']['en'] if 'en' in sale['PLACE_JSON'].keys() else ''
#             a.auction_date = sale['PREVIEW_JSON'][0].get('TO_DT',"") if (sale['PREVIEW_JSON']!=None and type(sale['PREVIEW_JSON']) == list) else ''
#             a.artist_name_kor = art['ARTIST_NAME_JSON'].get('ko','') if (art['ARTIST_NAME_JSON']!=None and type(art['ARTIST_NAME_JSON']) == dict) else ''
#             a.artist_name_eng = art['ARTIST_NAME_JSON'].get('en','') if (art['ARTIST_NAME_JSON']!=None and type(art['ARTIST_NAME_JSON']) == dict) else ''
#             a.artist_comment = ''
#             a.lot_no =art['LOT_NO']            
#             a.make_year = art['MAKE_YEAR_JSON'].get('ko','TBD') if (art['MAKE_YEAR_JSON']!=None and type(art['MAKE_YEAR_JSON']) == dict) else ''
#             a.title_kor = art['TITLE_JSON'].get('ko','') if (art['TITLE_JSON']!=None and type(art['TITLE_JSON']) == dict) else ''
#             a.title_eng = art['TITLE_JSON'].get('en','') if (art['TITLE_JSON']!=None and type(art['TITLE_JSON']) == dict) else ''
#             a.currency = art['CURR_CD']
#             a.money = art['LAST_PRICE']
#             lotsize = art['LOT_SIZE_JSON'][0]
#             a.unit_cd = lotsize.get('UNIT_CD','')
#             a.size_length = lotsize.get('SIZE1',0.0)
#             a.size_width = lotsize.get('SIZE2',0.0)
#             a.mix_cd = lotsize.get('MIX_CD',0.0)
#             a.mix_size =lotsize.get('SIZE3',0.0)
#             a.canvas = lotsize.get('CANVAS',0.0)
#             a.medium_eng = art['MATE_NM_EN']
#             a.medium_kor = art['MATE_NM']
#             a.description = art['SIGN_INFO_JSON']
#             a.estimate_high = art['EXPE_PRICE_TO_JSON'].get(a.currency,0.0)  if (art['EXPE_PRICE_TO_JSON']!=None and type(art['EXPE_PRICE_TO_JSON']) == dict) else 0.0
#             a.estimate_low = art['EXPE_PRICE_FROM_JSON'].get(a.currency,0.0) if (art['EXPE_PRICE_FROM_JSON']!=None and type(art['EXPE_PRICE_FROM_JSON']) == dict) else 0.0
#             a.edition = art['EDITION']        
#             art_list.append(a.__dict__)
#         except Exception as e:
#             print(e)
#             pass
#     return art_list

# p = r'/mnt/auc/seoul'
# files = [(i,os.path.join(p,str(i)+'.json')) for i in range(1,653)]
# rows=[]
# for i,f in files:
#     try:
#         with open(f,'r') as jf:
#             data = json.load(jf)
#         row = parseDataForInsert(f,data)
#         rows.extend(row.__dict__)
#     except Exception as e:
#         pass
  





import os
import pandas as pd

p = r'/home/fakeblocker/code/python/Auc/naver'
files = os.listdir(p)

dfs = [pd.read_csv(os.path.join(p,f)) for f in files]
total = pd.concat(dfs)
total.to_csv('8130000.csv')
