import pickle

import streamlit as st

model = pickle.load(open('best_pickle.pkl',rb'))
