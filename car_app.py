import pickle

import streamlit as st

Trans = st.radio("Select Transmission: ", ('Automatic', 'Manual'))
#model = pickle.load(open('best_model.pkl','rb'))

owner = st.selectbox("owner: ",
                     ['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])
                         
st.title('car prediction model')
