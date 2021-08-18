

import pandas as pd

left_df = pd.DataFrame()
right_df = pd.DataFrame()
lefton = []
righton =[]
filterkey = ''
merged_df = pd.merge(left_df,right_df,left_on=lefton,right_on=righton,suffixes=['','_y'],how='left')
new_df,exist_df = merged_df[merged_df[filterkey].isnull()],merged_df[merged_df[filterkey].notnull()]
