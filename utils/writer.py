import json


def writeDataAsFile(filepath,data):
    try:
        with open(filepath,'w') as f:
            if type(data) == dict:
                f.write(json.dumps(data))
            elif type(data) == str:
                f.write(data)
            else:
                raise Exception
        print('success')
        return True
    except Exception as e:
        print('fail')
        return False
    
