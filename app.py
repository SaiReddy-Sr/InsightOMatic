import streamlit as st
import pandas as pd
from src.analyzer import analyze_data

st.set_page_config(page_title="Insight-O-Matic", page_icon="📊", layout="wide")

st.title("📊 Insight-O-Matic - Chat with your CSV")
st.markdown("Upload a CSV dataset and ask questions about your data. The AI will analyze it for you!")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about this data:")
    if st.button("Analyze") and question:
        with st.spinner("Analyzing..."):
            response = analyze_data(df, question)
            st.write("### AI Insights")
            st.markdown(response)
else:
    st.info("Awaiting CSV file to be uploaded.")
