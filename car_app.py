import pickle

import streamlit as st

model = pickle.load(open('best_model.pkl','rb'))


                         
st.title('car prediction model')
