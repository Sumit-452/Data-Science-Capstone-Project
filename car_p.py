import pandas as pd
import numpy as np
from sklearn.preprocessing import *

df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst


#deleting uncessary rows and columns
for i in q:
    w=df[df['manufacturer']==i].index
    for j in list(w):
      df.drop(j,inplace=True)
df.drop_duplicates(inplace=True)
df.drop(columns=['name'],axis=1,inplace=True)




# get dummies
df=pd.get_dummies(data=df,columns=['fuel','seller_type','owner','transmission','manufacturer'])

#separating dependent and independent variable
x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']

#sclarization
from sklearn.preprocessing import StandardScaler,MinMaxScaler
xmm = MinMaxScaler().fit_transform(x)


# model building
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

ad=AdaBoostRegressor(base_estimator=DecisionTreeRegressor())
ad.fit(xmm,y)

#model saving
import pickle
pickle.dump(ad,open('adaboost.pkl','wb'))
