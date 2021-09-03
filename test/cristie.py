#크리스티

import numpy as np
import pandas as pd
import requests
import time, random
from bs4 import BeautifulSoup
from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime



path=r"C:\Users\ideam\chromedriver.exe"
df2 = pd.read_csv('./chiristies1.csv')
del df2['Unnamed: 0']
df2 = df2.url.tolist()
   


lst = []
# df1 = pd.DataFrame()
# df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()
df9 = pd.DataFrame()
df10 = pd.DataFrame()
df11 = pd.DataFrame()
df12 = pd.DataFrame()
df13 = pd.DataFrame()
df14 = pd.DataFrame()
df15 = pd.DataFrame()
df16 = pd.DataFrame()
df17 = pd.DataFrame()
total1 = pd.DataFrame()


options = Options()

# chrome을 전체화면으로 넓히는 옵션입니다.
# options.add_argument('--start-fullscreen')
driver = webdriver.Chrome(executable_path=path, chrome_options=options)
driver.set_window_size(1920, 1080)
#driver.get('https://www.christies.com/en/results?year=2020&month=1')

driver.get('https://www.christies.com/en/results?year=2020&month=12')
time.sleep(2)
button0 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/button')))
button0.click()  



button1 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/chr-header/header/div[1]/div/div/div/chr-button/button')))
button1.click() #result 클릭

time.sleep(2) 
 
# button1 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="christies-header"]/div/div[2]/div/ul/li[1]/button/span')))
# button1.click() #result 클릭

login = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="userName"]')))
login.click()
login.send_keys('ideamanjo@gmail.com')
login = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
login.click()
login.send_keys('Whdydghks1@#')
login.send_keys(Keys.RETURN)
# button1 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/html/body/div[1]/chr-modal-provider/chr-modal/div/div[2]/div/div/div/div[2]/chr-modal-login/div/chr-form/form/div[4]/chr-button/button')))
# button1.click() #result 클릭
# element = driver.find_element_by_xpath('/html/body/div[1]/chr-modal-provider/chr-modal/div/div[2]/div/div/div/div[2]/chr-modal-login/div/chr-form/form/div[4]/chr-button')
# driver.execute_script("arguments[0].click();", element)

time.sleep(2)


def doScrollDown(whileSeconds):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        time.sleep(0.1)
        if datetime.datetime.now() > end:
            break
            
for k in range(3,5):
    for i in df2[k:k+1]:#k*100:(k+1)*100]:
        df3 = pd.DataFrame()
        df11 = pd.DataFrame()
        driver.get(i)
        time.sleep(4.5)     

    #     find_href1 = driver.find_elements_by_xpath('/html/body/div[1]/chr-page-nav/nav/div/ul/li[1]/a')
    #     for my_href in find_href1:
    #         df11 = df11.append(pd.DataFrame({'real_count': find_href1[0].text}, index=[0]), ignore_index=True)     
    #     df11['real_count'] = df11['real_count'].str.replace('Browse lots \(', '')
    #     df11['real_count'] = df11['real_count'].str.replace('\)', '')
    #     print(df11)    
    #     if int(df11['real_count'][0]) < 30:
    #         doScrollDown(1)    

    #     elif int(df11['real_count'][0]) >= 30 and int(df11['real_count'][0]) < 60:
    #         doScrollDown(1)
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)

    #     elif int(df11['real_count'][0]) >= 60 and int(df11['real_count'][0]) < 140:        
    #         doScrollDown(1)
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1.5) 
    #         time.sleep(3.5)            
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  
    #         doScrollDown(1.5) 
    #         time.sleep(3.5) 
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(2)     

    #     elif int(df11['real_count'][0]) >= 140:        
    #         doScrollDown(1)
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1.5) 
    #         time.sleep(3.5)            
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  
    #         doScrollDown(1.5) 
    #         time.sleep(3.5) 
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(2)          
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1) 
    #         time.sleep(3.5)
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(1.5) 
    #         time.sleep(3.5)            
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  
    #         doScrollDown(1.5) 
    #         time.sleep(3.5) 
    #         driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
    #         doScrollDown(2)      
    #     else:
        doScrollDown(1)
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1) 
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1) 
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1.5) 
        time.sleep(3.5)            
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  
        doScrollDown(1.5) 
        time.sleep(3.5) 
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(2)          
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1) 
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1) 
        time.sleep(3.5)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(1.5) 
        time.sleep(3.5)            
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  
        doScrollDown(1.5) 
        time.sleep(3.5) 
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)                   
        doScrollDown(2) 



        if driver.find_elements_by_xpath('/html/body/div[1]/chr-auction-results-view/main/section/div/div/chr-infinite-scroll/div[1]/div/chr-lot-tile/a'):
            find_href = driver.find_elements_by_xpath('/html/body/div[1]/chr-auction-results-view/main/section/div/div/chr-infinite-scroll/div[1]/div/chr-lot-tile/a')
            for my_href in find_href:
                df3 = df3.append(pd.DataFrame({'url': my_href.get_attribute("href")}, index=[0]), ignore_index=True) 
        else:                
            find_href = driver.find_elements_by_xpath('/html/body/main/chr-auction-results-view/main/section/div/div/chr-infinite-scroll/div[1]/div/chr-lot-tile/div[1]/div[3]/div[3]/div[1]/h2/a')
            for my_href in find_href:
                df3 = df3.append(pd.DataFrame({'url': my_href.get_attribute("href")}, index=[0]), ignore_index=True) 

        find_href2 = driver.find_elements_by_xpath('/html/body/div[1]/chr-page-nav/nav/div/ul/li[1]/a')
        for my_href in find_href2:
            df5 = df5.append(pd.DataFrame({'real_count': find_href2[0].text}, index=[0]), ignore_index=True)               

        df6 = df6.append(pd.DataFrame({'count': len(df3)}, index=[0]), ignore_index=True) 
        df7 = df7.append(pd.DataFrame({'site': i}, index=[0]), ignore_index=True)     
        total = pd.merge(df7, df5, left_index=True, right_index=True,how='left')
        total = pd.merge(total, df6, left_index=True, right_index=True,how='left')

        df3['site'] = i
        df4 = df4.append(df3)        
    df4.to_csv('christies_work_list'+str(k)+'.csv')
    df4.to_csv('christies_work_list_sig'+str(k)+'.csv', encoding = 'utf-8-sig')
    df4.to_csv('christies_work_list_utf'+str(k)+'.csv', encoding = 'utf-8')