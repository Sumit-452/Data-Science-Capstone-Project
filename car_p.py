import pandas as pd

import numpy as np

from sklearn.preprocessing import *

df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

bg=AdaBoostRegressor(base_estimator=DecisionTreeRegressor())
bg.fit(x_train,y_train)

import pickle
pickle.dump(ad,open('best_model.pkl','wb'))
