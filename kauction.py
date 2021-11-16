from etl.fetch.kauction import fetchDatas,downloadImages

if __name__=='__main__':
    JSON_BASE_PATH = r'F:\art\auc\datas\que\k'
    IMAGE_BASE_PATH = r'F:\art\auc\images\k'
    CHROME_DRIVER_PATH = r'D:\Programming\artpassion\aucetl\chromedriver.exe'
    data = list(range(1,300))
    for t in ['major','weekly','premium']:
        fetchDatas(t, data,JSON_BASE_PATH,useMultiProcessing=True)
    #downloadImages('major',data,JSON_BASE_PATH,IMAGE_BASE_PATH,True)