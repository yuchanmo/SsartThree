from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
from bs4 import BeautifulSoup
import json
import os
import uncurl
import pandas as pd


# JSON_SAVE_PATH = '/mnt/auc/seoul'
# IMAGE_SAVE_PATH = '/mnt/auc/seoul/images'

# class SeoulAuctionRequester():
#     def __init__(self):
#         self.session = requests.Session()
#         self.__setSessionInfo()

#     def __setSessionInfo(self):
#         pass

#     def getAuctionResult(self,no,writeAsFile=True):
#         pass

#     @staticmethod
#     def downloadArtImages(no):
#         try:
#             data_path = f'{JSON_SAVE_PATH}/{no}.json'
#             with open(data_path) as f:
#                 data = json.load(f)
#             samples = data['tables']['LOTS']['rows']
#             for sample in samples:
#                 lot_no,image_path,image_name = sample['LOT_NO'],sample['LOT_IMG_PATH'],sample['LOT_IMG_NAME']
#                 image_full_path_urls = [f"https://www.seoulauction.com/nas_img{image_path}/{image_name}",f"https://www.seoulauction.com/nas_img{image_path}/list/{image_name}"]
#                 for u in image_full_path_urls:
#                     #print(u)
#                     response = requests.get(u,stream=True)
#                     #print('success to access to image')
#                     if response.status_code==200:
#                         dest_folder = f'{IMAGE_SAVE_PATH}/{no}'
#                         if not os.path.exists(dest_folder):
#                             os.makedirs(dest_folder,exist_ok=True)
#                         file_path = os.path.join(dest_folder,f'LOT{lot_no}_{image_name}')
#                         with open(file_path,'wb') as f:
#                             for chunk in response:
#                                 f.write(chunk)
#                     else:
#                         pass
#         except Exception as e:
#             print(e)
#             pass
        

IMAGE_SAVE_PATH = '/mnt/auc/phillips/images'
path = r'/home/fakeblocker/code/python/Auc/p.txt'
df = pd.read_csv(path,delimiter='\t')
df.head()
df.columns = ['idx', 'lot', 'name', 'title', 'date', 'image_url']

err=[]
for i,row in df[1958:].iterrows():
    try:
        idx,url = row['idx'], row['image_url']
        foldername = url.split('auctions/')[1].split('/')[0]
        img_name = url.split('/')[-1]
        response = requests.get(url,stream=True)
        #print('success to access to image')
        if response.status_code==200:
            dest_folder = f'{IMAGE_SAVE_PATH}/{foldername}'
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder,exist_ok=True)
            file_path = os.path.join(dest_folder,f'{img_name}')
            print(file_path)
            with open(file_path,'wb') as f:
                for chunk in response:
                    f.write(chunk)
    except Exception as e:
        print('no file : ',url)
        err.append(url)


print(err)