import pandas as pd
from utils.dbcon import sqlserver
import json


cols = ['auction_site', 'auction_url_num', 'auction_place',      
       'auction_date', 'artist_name_kor', 'artist_name_eng', 'artist_comment',
       'lot_no', 'make_year', 'title_kor', 'title_eng', 'currency', 'money',  
       'unit_cd', 'size_length', 'size_width', 'mix_cd', 'mix_size', 'canvas',
       'medium_eng', 'medium_kor', 'description', 'estimate_high',
       'estimate_low', 'edition', 'image_name', 'art_info_source_id',
       'auction_cate']

conditions = {
    'artists':{
        'table':'artists',
        'schema':'dbo',
        'sql':'select * from artists',
        'join_key' :['artist_name_kor','artist_name_eng'],
        'columns':['artist_name_kor','artist_name_eng','artist_comment'],
        'filter_key' : 'artist_id',
        'final_columns': cols + ['artist_id',]
    },
    'art_infos' :{
        'table':'art_infos',
        'schema':'dbo',
        'sql':'select * from art_infos',
        'join_key' :['artist_id','art_info_source_id','make_year','title_kor','title_eng','edition' ,'image_name'  ],
        'columns':['artist_id'
        ,'art_info_source_id'
        ,'make_year'
        ,'title_kor'
        ,'title_eng'
        ,'unit_cd'
        ,'size_length'
        ,'size_width'
        ,'mix_cd'
        ,'mix_size'
        ,'canvas'
        ,'medium_eng'
        ,'medium_kor'
        ,'description'
        ,'edition'
        ,'image_name'        
        ],
        'filter_key' : 'art_info_id',
        'final_columns' : cols + ['art_info_id' ,'artist_id' ,'art_info_source_id']            
    },
    'sites':{
        'table':'sites',
        'schema':'dbo',
        'sql':'select * from sites',
        'join_key' :['auction_site'],
        'columns':['auction_site'],
        'filter_key' : 'site_id',
        'final_columns': cols +  ['site_id','art_info_id' ,'artist_id' ,'art_info_source_id',]      
    },
    'auctions':{
        'table':'auctions',
        'schema':'dbo',
        'sql':'select * from auctions',
        'join_key' :['site_id','auction_url_num','auction_cate'],
        'columns':['site_id','auction_url_num','auction_place','auction_date','auction_cate'],
        'filter_key' : 'auction_id',
        'final_columns': cols +  ['auction_id','site_id','art_info_id' ,'artist_id' ,'art_info_source_id',]             
    },
    'auction_arts':{      
        'table':'auction_arts',
        'schema':'dbo',
        'sql':'select * from auction_arts',
        'join_key' :['auction_id','art_info_id','lot_no'],
        'columns':['auction_id','art_info_id','lot_no','currency','money','estimate_high','estimate_low'],
        'filter_key' : 'auction_art_id',
        'final_columns': cols +  ['auction_art_id','auction_id','site_id','art_info_id' ,'artist_id' ,'art_info_source_id',]                   
    }    
}

def filterNaNRows(tbl,cols):
    return tbl[~tbl[cols].isna().all(axis=1)]


def filterNewExistData(left_df,right_df,join_key,filter_key):
    try:
        
        merged_df = pd.merge(left_df,right_df,left_on=join_key,right_on=join_key,suffixes=['','_y'],how='left')
        new_rows,exist_rows = merged_df[merged_df[filter_key].isnull()],merged_df[merged_df[filter_key].notnull()]
        return new_rows,exist_rows
    except Exception as e:
        print(e)
        pass

#1. aritsts


def insertNewRows(original_df,table_key,val):
    try:
        sql_df = pd.read_sql(val['sql'],sqlserver)
        data_df = original_df[val['columns']].drop_duplicates()     
        new,exist = filterNewExistData(data_df,sql_df,val['join_key'],val['filter_key'])
        new = new[val['columns']].drop_duplicates()
        if len(new)>0:
            new.to_sql(val['table'],sqlserver,val['schema'],if_exists='append',index=False)
            print(f'table : {table_key}, new rows : {len(new)}')
        else:
            print(f'table : {table_key}, new rows : 0')
        sql_df = pd.read_sql(val['sql'],sqlserver)
        new,exist = filterNewExistData(original_df,sql_df,val['join_key'],val['filter_key'])
        return exist[val['final_columns']]
    except Exception as e:
        print(e)
        pass

#2. art_infos



#def loadData(path:str):
path = r'seoul_913.csv'
df = pd.read_csv(path,encoding='utf-8-sig')

df['art_info_source_id'] = 1
df['auction_cate'] = 'online'

for k,v in conditions.items():
    print(f'insert {k} table')
    df = insertNewRows(df,k,v)
    print(len(df))
    

if __name__ =='__main__':
    pass
