from sqlalchemy import create_engine

id = 'root'
pwd = '1'
ip = '20.85.245.228'
port = 3306
database='auction'

engine = create_engine(f"mysql+pymysql://{id}:"+f"{pwd}"+f"@{ip}:{port}/{database}?charset=utf8", encoding='utf-8')