import pickle

import streamlit as st

Trans = st.radio("Select Transmission: ", ('Automatic', 'Manual'))


owner = st.selectbox("owner: ",
                     ['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])
                         
st.title('car prediction model')
