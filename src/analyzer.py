import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def analyze_data(df, question):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ Error: GEMINI_API_KEY is not set in the .env file."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Convert a sample of the dataframe and its structure to string
    data_sample = df.head(5).to_string()
    columns_info = str(df.dtypes)

    prompt = f"""
    You are an expert Data Analyst. I am going to ask you a question about a dataset.
    Here is the schema of the dataset:
    {columns_info}
    
    Here is a sample of the first 5 rows:
    {data_sample}
    
    User Question: {question}
    
    Based on the available context, provide a helpful and analytical answer. If the question requires executing code to get the exact answer, explain how one would compute it or provide the insight based on the sample. Keep it concise, engaging, and markdown styled.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ An error occurred during analysis: {e}"
