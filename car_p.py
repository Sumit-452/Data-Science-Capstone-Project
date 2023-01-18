import pandas as pd
import numpy as np
from sklearn.preprocessing import *

df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst


#deleting uncessary rows and columns
d1=df['manufacturer'].value_counts()
w=d1[d1.values<10].index
q=list(w)
q

for i in q:
    w=df[df['manufacturer']==i].index
    for j in list(w):
      df.drop(j,inplace=True)

#converting years into years old column
df['years_old']=2023-df['year']
df['years_old']
df.drop(columns=['name','year'],axis=1,inplace=True)
df.drop_duplicates(inplace=True)



# get dummies
df=pd.get_dummies(data=df,columns=['fuel','seller_type','owner','transmission','manufacturer'])

#separating dependent and independent variable
x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']



# model building
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

ad=AdaBoostRegressor(base_estimator=DecisionTreeRegressor())
ad.fit(x,y)

#model saving
import pickle
pickle.dump(ad,open('best_model.pkl','wb'))
