from etl.fetch.seoulauction import downloadImages,fetchDatas

if __name__=='__main__':
    JSON_BASE_PATH = r'F:\art\auc\datas\que\seoul'
    IMAGE_BASE_PATH = r'F:\art\auc\images\seoul\online'
    CHROME_DRIVER_PATH = r'D:\Programming\artpassion\aucetl\chromedriver.exe'
    data = list(range(1,700))
    fetchDatas(data,JSON_BASE_PATH,CHROME_DRIVER_PATH,useMultiProcessing=True)
    #downloadImages(data,json_base_path=JSON_BASE_PATH,image_base_path=IMAGE_BASE_PATH,useMultiProcessing=True)