
import pandas as pd
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'output')

df_data=pd.read_csv(os.path.join(OUTPUT_DIR,'data.csv'))
x=df_data['Age Group','Region Name','Year','Sex','Cause']
y=df_data['Numbers']
print(df_data.head())