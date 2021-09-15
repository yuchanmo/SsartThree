from sqlalchemy import create_engine

id = 'root'
pwd = '1'
ip = '20.85.245.228'
port = 3306
database='auction'

engine = create_engine(f"mysql+pymysql://{id}:"+f"{pwd}"+f"@{ip}:{port}/{database}?charset=utf8", encoding='utf-8')

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
coninfo = {
    'user': 'sa',
    'pwd': '1',
    'host': 'DESKTOP-VP3C86M',
    'database': 'ArtMania'
}
sqlserver = create_engine(
    f"mssql+pymssql://{coninfo['user']}:{coninfo['pwd']}@{coninfo['host']}/{coninfo['database']}", echo=False)

# Base = automap_base()
# Base.prepare(sqlserver, reflect=True)
# jobque = Base.classes.job_que
# product = Base.classes.product
# #maria_engine = create_engine('mysql+pymysql://sa:1q2w3e4r5t6y@dwemaria.westus.cloudapp.azure.com/jackpotman')

# session = Session(sqlserver)