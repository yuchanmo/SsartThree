from etl.fetch.seoulauction import downloadImages,fetchDatas

if __name__=='__main__':
    downloadImages(list(range(654,661)),json_base_path='/mnt/auc/datas/que/seoul',image_base_path='/mnt/auc/images/seoul',useMultiProcessing=True)