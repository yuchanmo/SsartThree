import os
import json
from typing import NamedTuple
import pandas as pd
from collections import namedtuple
from models.artinfo import art,Art
from pprint import pprint
from utils.dbcon import engine


def parseDataForInsert(f:str, data:dict):
    arts =  data['tables']['LOTS']['rows']
    sales = data['tables']['SALE']['rows']
    art_list = []
    sale = sales[0]
    for art in arts:
        try:
            a = Art()
            a.auction_site = 'seoul'
            a.auction_url_num = int(f.split('/')[-1].split('.')[0])
            a.auction_place = sale['PLACE_JSON']['en'] if 'en' in sale['PLACE_JSON'].keys() else ''
            a.auction_date = sale['PREVIEW_JSON'][0].get('TO_DT',"") if (sale['PREVIEW_JSON']!=None and type(sale['PREVIEW_JSON']) == list) else ''
            a.artist_name_kor = art['ARTIST_NAME_JSON'].get('ko','') if (art['ARTIST_NAME_JSON']!=None and type(art['ARTIST_NAME_JSON']) == dict) else ''
            a.artist_name_eng = art['ARTIST_NAME_JSON'].get('en','') if (art['ARTIST_NAME_JSON']!=None and type(art['ARTIST_NAME_JSON']) == dict) else ''
            a.artist_comment = ''
            a.lot_no =art['LOT_NO']
            a.make_year = art['MAKE_YEAR_JSON'].get('ko','TBD') if (art['MAKE_YEAR_JSON']!=None and type(art['MAKE_YEAR_JSON']) == dict) else ''
            a.title_kor = art['TITLE_JSON'].get('ko','') if (art['TITLE_JSON']!=None and type(art['TITLE_JSON']) == dict) else ''
            a.title_eng = art['TITLE_JSON'].get('en','') if (art['TITLE_JSON']!=None and type(art['TITLE_JSON']) == dict) else ''
            a.currency = art['CURR_CD']
            a.money = art['LAST_PRICE']
            lotsize = art['LOT_SIZE_JSON'][0]
            a.unit_cd = lotsize.get('UNIT_CD','')
            a.size_length = lotsize.get('SIZE1',0.0)
            a.size_width = lotsize.get('SIZE2',0.0)
            a.mix_cd = lotsize.get('MIX_CD',0.0)
            a.mix_size =lotsize.get('SIZE3',0.0)
            a.canvas = lotsize.get('CANVAS',0.0)
            a.medium_eng = art['MATE_NM_EN']
            a.medium_kor = art['MATE_NM']
            a.description = art['SIGN_INFO_JSON']
            a.estimate_high = art['EXPE_PRICE_TO_JSON'].get(a.currency,0.0)  if (art['EXPE_PRICE_TO_JSON']!=None and type(art['EXPE_PRICE_TO_JSON']) == dict) else 0.0
            a.estimate_low = art['EXPE_PRICE_FROM_JSON'].get(a.currency,0.0) if (art['EXPE_PRICE_FROM_JSON']!=None and type(art['EXPE_PRICE_FROM_JSON']) == dict) else 0.0
            a.edition = art['EDITION']
            a.image_name = art['LOT_IMG_NAME']
            art_list.append(a.__dict__)
        except Exception as e:
            print(e)
            pass
    print(len(art_list))
    return art_list


#if __name__ == '__main__':
p = r'/mnt/auc/datas/que/seoul'
files = [(i,os.path.join(p,str(i)+'.json')) for i in range(1,653)]
rows_list=[]
for i,f in files:
    try:
        with open(f,'r') as jf:
            data = json.load(jf)
        rows = parseDataForInsert(f,data)
        rows_list.extend(rows)
    except Exception as e:
        pass
df = pd.DataFrame(rows_list)

df.head()
df.iloc[0]
df['auction_url'] = 'https://www.seoulauction.com/'

#1. sites
sites_df = df[['auction_site','auction_url']].drop_duplicates()
sites_db_df = pd.read_sql('select * from sites',engine)
join_key = ['auction_site','auction_url']
filterkey = 'site_id'
merged_df = pd.merge(sites_df,sites_db_df,left_on=join_key,right_on=join_key,suffixes=['','_y'],how='left')
new_site_df,exist_site_df = merged_df[merged_df[filterkey].isnull()],merged_df[merged_df[filterkey].notnull()]

if len(new_site_df)>0:
    new_site_df.to_sql('sites',engine,if_exists='append',index=False)

sites_db_df = pd.read_sql('select * from sites',engine)
join_key = ['auction_site','auction_url']
filterkey = 'site_id'
sites_merged_df = pd.merge(df,sites_db_df,left_on=join_key,right_on=join_key,suffixes=['','_y'],how='left')
new_sites_merged_df,exist_site_mereged_df = merged_df[merged_df[filterkey].isnull()],merged_df[merged_df[filterkey].notnull()]

#2.artists
artist_df = exist_site_mereged_df[['artist_name_kor','artist_name_eng','artist_comment']].drop_duplicates()
arists_db_df = pd.read_sql('select * from artists',engine)
artist_join_key = ['artist_name_kor','artist_name_eng']
artist_filterkey = 'artist_id'
aritst_merged_df = pd.merge(artist_df,arists_db_df,left_on=artist_join_key,right_on=artist_join_key,suffixes=['','_y'],how='left')
new_artists_df,exist_artists_df = aritst_merged_df[aritst_merged_df[artist_filterkey].isnull()],aritst_merged_df[aritst_merged_df[artist_filterkey].notnull()]

if len(new_artists_df)>0:
    new_artists_df[['artist_name_kor','artist_name_eng','artist_comment']].to_sql('artists',engine,if_exists='append',index=False)

arists_db_df = pd.read_sql('select * from artists',engine)
artist_join_key = ['artist_name_kor','artist_name_eng']
artist_filterkey = 'artist_id'
aritst_merged_df = pd.merge(exist_site_mereged_df,arists_db_df,left_on=artist_join_key,right_on=artist_join_key,suffixes=['','_y'],how='left')
new_artists_merged_df,exist_artists_merged_df = aritst_merged_df[aritst_merged_df[artist_filterkey].isnull()],aritst_merged_df[aritst_merged_df[artist_filterkey].notnull()]


#3. auctions
auction_df = exist_artists_merged_df[['site_id','auction_url_num','auction_place','auction_date']].drop_duplicates()
auction_db_df = pd.read_sql('select * from auctions',engine)
auction_join_key = ['site_id','auction_url_num','auction_place','auction_date']
auction_filterkey = 'auction_id'
auction_merged_df = pd.merge(auction_df,auction_db_df,left_on=auction_join_key,right_on=auction_join_key,suffixes=['','_y'],how='left')
new_auction_df,exist_auction_df = auction_merged_df[auction_merged_df[auction_filterkey].isnull()],auction_merged_df[auction_merged_df[auction_filterkey].notnull()]
new_auction_df['auction_date']=pd.to_datetime(new_auction_df['auction_date'])
if len(new_auction_df)>0:
    new_auction_df[['site_id','auction_url_num','auction_place','auction_date']].to_sql('auctions',engine,if_exists='append',index=False)

auction_db_df = pd.read_sql('select * from auctions',engine)
auction_join_key = ['site_id','auction_url_num','auction_place','auction_date']
exist_artists_merged_df['auction_date'] = pd.to_datetime(exist_artists_merged_df['auction_date'] )
auction_db_df['auction_date'] = pd.to_datetime(auction_db_df['auction_date'] )
auction_filterkey = 'auction_id'
auction_merged_df = pd.merge(exist_artists_merged_df,auction_db_df,left_on=auction_join_key,right_on=auction_join_key,suffixes=['','_y'],how='left')
new_auction_merged_df,exist_auction_merged_df = auction_merged_df[auction_merged_df[auction_filterkey].isnull()],auction_merged_df[auction_merged_df[auction_filterkey].notnull()]


#4. arts
arts_columns = ['auction_id', 'artist_id',  'lot_no',
       'make_year', 'title_kor', 'title_eng', 'currency', 'money', 'unit_cd',
       'size_length', 'size_width', 'mix_cd', 'mix_size', 'canvas',
       'medium_eng', 'medium_kor', 'description', 'estimate_high',
       'estimate_low', 'edition', 'image_name', ]
exist_auction_merged_df['description'] = exist_auction_merged_df['description'].apply(lambda x : str(x))
arts_df = exist_auction_merged_df[arts_columns].drop_duplicates()
arts_df['make_year'] = arts_df[arts_df['make_year'].isnull()]['make_year'] = 0
arts_df.to_sql('arts',engine,if_exists='append',index=False)
arts_df.iloc[0]
arts_df['mix_cd'].unique()
# len(rows)

# df.head()


# df = pd.DataFrame(rows_list)
# df.to_csv('seoul_final.csv',encoding='utf-8-sig')
# df = pd.read_csv('seoul_final.csv',encoding='utf-8-sig')