import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("cv.pkl", "rb"))

st.title("Spam Comment Detection")
comment = st.text_input("Comment")

if st.button("Detect"):
	test = cv.transform([comment]).toarray()
	res = model.predict(test)
	print(res)
	st.success("Detected: " + str(res[0]))
