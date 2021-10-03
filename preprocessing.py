import numpy as np
import pandas as pd
import requests
import time, random
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import math

# df = pd.read_csv(r'D:\Programming\artpassion\aucetl\seoul_913.csv',encoding='utf-8-sig')
# df = df.drop('Unnamed: 0', 1)
def makeFeature(df:pd.DataFrame):
    df['auction_date'] = pd.to_datetime(df['auction_date'])   
    conditions = [
    (df['size_length'] > df['size_width']),
    (df['size_length'] < df['size_width']),
    (df['size_length'] == df['size_width']),
    ]
    choices = [df['size_length'], df['size_width'], df['size_width']]
    df['max_size'] = np.select(conditions, choices, default='black')
    df['max_size'] = df['max_size'].astype(float)    


    #canvas_size
    conditions = [    
        (df['max_size']<=20),
        (df['max_size']>20) & (df['max_size']<=25.5), (df['max_size']>25.5) & (df['max_size']<=30), (df['max_size']>30) & (df['max_size']<=34),
        (df['max_size']>34) & (df['max_size']<=38), (df['max_size']>38) & (df['max_size']<=43), (df['max_size']>43) & (df['max_size']<=50.5),
        (df['max_size']>50.5) & (df['max_size']<=58), (df['max_size']>58) & (df['max_size']<=63), (df['max_size']>63) & (df['max_size']<=69),
        (df['max_size']>69) & (df['max_size']<=77), (df['max_size']>77) & (df['max_size']<=88), (df['max_size']>88) & (df['max_size']<=97),
        (df['max_size']>97) & (df['max_size']<=110), (df['max_size']>110) & (df['max_size']<=125), (df['max_size']>125) & (df['max_size']<=139),
        (df['max_size']>139) & (df['max_size']<=154), (df['max_size']>154) & (df['max_size']<=163), (df['max_size']>163) & (df['max_size']<=195),
        (df['max_size']>195) & (df['max_size']<=240), (df['max_size']>240) & (df['max_size']<=270), (df['max_size']>270) & (df['max_size']<=300),
        (df['max_size']>300)
        ]
    choices = [1,2,3,4,5,6,8,10,12,15,20,25,30,40,50,60,80,100,120,150,200,300,500]
    df['canvas_size'] = np.select(conditions, choices, default='black').astype(float)


    #artwork_type
    conditions = [    
    (df['mix_cd'].str.contains('height')) & (df['mix_size'] != 0),
    (df['medium_eng'].str.contains("photo")) | (df['medium_eng'].str.contains("Photo")),
    (df['medium_eng'].str.contains("lithograph")) | (df['medium_eng'].str.contains("offset print")) | (df['medium_eng'].str.contains("lenticular")) | (df['medium_eng'].str.contains("silk screen")) | (df['medium_eng'].str.contains("silkscreen")) | 
    (df['medium_eng'].str.contains("mixed media")) | (df['medium_eng'].str.contains("drypoint")) | (df['medium_eng'].str.contains("serigraph")) | (df['medium_eng'].str.contains("etching")) | (df['medium_eng'].str.contains("litho")) | 
    (df['medium_eng'].str.contains("woodcut")) | (df['medium_eng'].str.contains("mezzotint")) | (df['medium_eng'].str.contains("aquatint")) | (df['medium_eng'].str.contains("collagraph")) | (df['medium_eng'].str.contains("monotype")) | 
    (df['medium_eng'].str.contains("monoprint")) | (df['medium_eng'].str.contains("mixograph")),
    (df['medium_eng'].str.contains("paper")) | (df['medium_eng'].str.contains("Paper")),
    (df['medium_eng'].str.contains("ink")) | (df['medium_eng'].str.contains("Ink")) | (df['medium_eng'].str.contains("oil")) | (df['medium_eng'].str.contains("Oil")) |
    (df['medium_eng'].str.contains("acrylic")) | (df['medium_eng'].str.contains("Acrylic")) | (df['medium_eng'].str.contains("Color")) | (df['medium_eng'].str.contains("color"))     
    ]
    choices = ['sculpture', 'photographs', 'print', 'work on paper', 'paintings']
    df['artwork_type'] = np.select(conditions, choices, default='other')


    #half_year
    conditions = [(df['auction_date'].dt.month > 6)]
    choices = [2]
    df['half_year'] = np.select(conditions, choices, default=1)


    #convert_inch
    df['size_length_inch'] = df['size_length']*0.393701
    df['size_width_inch'] = df['size_width']*0.393701
    df['mix_size_inch'] = df['mix_size']*0.393701


    #canvas_size_money    
    df['canvas_size_money'] = np.where((df['artwork_type'] == 'work on paper')|(df['artwork_type'] == 'paintings'), df['money']/df['canvas_size'], np.nan)
    df['canvas_size_money'] = df['canvas_size_money'].astype(float)
    return df
    #name+born
    #df['artist_name_kor_born'] = df['artist_name_kor'].astype(str) + ' (' + df['BORN_YEAR'].astype(str) +')'

