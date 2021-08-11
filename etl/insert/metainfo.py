import pandas as pd

sites = [('seoul','https://www.seoulauction.com/'),('k','https://www.k-auction.com/')]
df = pd.DataFrame(sites,columns=['auction_site','auction_url'])

from utils.dbcon import engine
df.to_sql('sites',engine,if_exists='append',index=False)