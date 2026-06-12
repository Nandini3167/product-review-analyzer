import streamlit as st
import json
from sentiment_chain import analyze_review

st.title("Product Review Analyzer")

review = st.text_area("Enter Product Review")

if st.button("Analyze"):

    if review.strip():

        result = analyze_review(review)

        try:
            data = json.loads(result)
            st.json(data)

        except Exception:
            st.write(result)