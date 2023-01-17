import pickle

import streamlit as st


st.title('car prediction model')
transmission = st.radio("Select Transmission: ", ('Automatic', 'Manual'))


owner = st.selectbox("owner: ",
                     ['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])
                         
manufacturer = st.selectbox("manufacturer: ",
                     ['Maruti','Hyundai','Mahindra','Tata','Ford','Honda','Toyota','Chevrolet','Renault',
                      'Volkswagen','Nissan','Skoda','Fiat','Audi','Datsun','BMW','Mercedes-Benz'])

seller_type = st.radio("select seller type: ",
                     ('Individual','Dealer','Trustmark Dealer'))

fuel = st.selectbox("fuel: ",
                     ['Diesel','Petrol','CNG','LPG','Electric'])
