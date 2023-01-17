import pandas as pd
import numpy as np
from sklearn.preprocessing import *

df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst

df=pd.get_dummies(data=df,columns=['fuel','seller_type','owner','transmission','manufacturer'])

x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']

from sklearn.preprocessing import StandardScaler,MinMaxScaler
xmm = MinMaxScaler().fit_transform(x)



from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

bg=AdaBoostRegressor(base_estimator=DecisionTreeRegressor())
bg.fit(xmm,y)

import pickle
pickle.dump(ad,open('best_model.pkl','wb'))
