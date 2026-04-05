# Insight-O-Matic 📊

A beautiful, AI-powered internal tool built with **Streamlit** and **Google Gemini** that allows users to upload a CSV file and ask natural language questions about their data. 

## Features
- **Effortless Upload:** Drag and drop your CSV datasets.
- **Instant Preview:** Examine your dataset inside a clean data frame UI.
- **AI Analysis:** Let Gemini analyze the schema and sample data to provide insightful answers and analytical perspectives on your datasets.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SaiReddy-Sr/InsightOMatic.git
   cd InsightOMatic
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup:**
   Create a `.env` file in the root directory with your Google Gemini API Key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Launch the App:**
   ```bash
   streamlit run app.py
   ```

## Why this is in my portfolio?
It demonstrates full-stack rapid prototyping (Python/Streamlit) and the ability to integrate cutting-edge LLM capabilities (Gemini) directly into data engineering and analytics workflows.

## Known Issues
- Currently, the prompt may struggle with extremely large dataset schemas or highly unstructured CSV edge cases. An issue has been created to track this.

## Future Roadmap
- [ ] Add support for Excel files (`.xlsx`)
- [ ] Implement caching to reduce Gemini API costs
- [ ] Incorporate vector search to allow chatting with multi-document data sources
