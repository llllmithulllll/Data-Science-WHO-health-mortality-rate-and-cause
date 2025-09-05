from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pandas as pd
import os
import joblib



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'output')
MODELS_DIR=os.path.join(BASE_DIR,'models')


df_data=pd.read_csv(os.path.join(OUTPUT_DIR,'data.csv'))
x=df_data[['Age Group','Region Name','Year','Sex','cause']]
x=pd.get_dummies(x,drop_first=True)
y=df_data['Death rate per 100 000 population']
print(df_data.columns)

x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=0.2,
                                               random_state=300)

model=model = RandomForestRegressor(n_estimators=200, random_state=300)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

r2=r2_score(y_test,y_pred)
print(r2)
os.makedirs(MODELS_DIR,exist_ok=True)
joblib.dump(model,os.path.join(MODELS_DIR,'my_model.pkl'))