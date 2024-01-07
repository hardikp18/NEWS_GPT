import os
import json
import shutil
import pandas as pd
import streamlit as st
import requests
from dotenv import load_dotenv
from enum import Enum
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

with st.sidebar:
    st.markdown(
        "## How to use\n"
        "1. Choose data sources you can choose NEWS API and CSV.\n"
        "2. If NEWS API is chosen as a data source, latest news of the company is availaible .\n"
        "3. Ask a question about a Company.\n"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app to find real-time latest market news from various News Articles using the NEWS API. "
        "It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) "
        "to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources\n"

    )
    st.markdown("[View the source code on GitHub]()")

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "")
api_port = int(os.environ.get("PORT", 8080))
parameter= os.environ.get("PARAMETER",)

# Paths for data files
csv_path = "./data/csv.jsonl"
news_path="./news/news.jsonl"


# Enum for data sources
class DataSource(Enum):
    NEWS_API = 'NEWS API'
    CSV = 'CSV'


# Streamlit UI elements
st.title("NEWS_GPT")
data_sources = st.multiselect(
    'Choose data sources',
    [source.value for source in DataSource]
)

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=("csv"),
    disabled=(DataSource.CSV.value not in data_sources)
)

# Handle CSV upload
if uploaded_file and DataSource.CSV.value in data_sources:
    df = pd.read_csv(uploaded_file)

    # Start progress bar
    progress_bar = st.progress(0, "Processing your file. Please wait.")
    total_rows = len(df)

    # Format the DataFrame rows and write to a jsonlines file
    formatted_rows = []

    for _, row in df.iterrows():
        # Format each row and append to the list
        formatted_rows.append(
            {"doc": ', '.join([f"{title}: {value}" for title, value in row.items()])}
        )

    # Write the formatted rows to the jsonlines file
    with open(csv_path, 'w') as outfile:
        for obj in formatted_rows:
            # Update the progress bar
            time.sleep(0.1)
            current_progress = (len(formatted_rows) / total_rows)
            progress_bar.progress(current_progress)
            outfile.write(json.dumps(obj) + '\n')

    # Finish progress bar when done
    progress_bar.progress(1.0, "Your file is uploaded successfully")

company=st.text_input(
    "Enter name of company you would like Market News for.",
    placeholder="Company Name",
    disabled=not data_sources
)

if parameter:
    os.environ['PARAMETER'] = company

question = st.text_input(
    "Search for something.",
    placeholder="Look for recent news related to a company ?",
    disabled=not data_sources
)

# Handle data sources
if DataSource.NEWS_API.value in data_sources:
    shutil.copy("news.jsonl", news_path)
elif os.path.exists(news_path):
    os.remove(news_path)

if DataSource.CSV.value not in data_sources and os.path.exists(csv_path):
    os.remove(csv_path)

# Handle Discounts API request if data source is selected and a question is provided
if data_sources and question:
    if not os.path.exists(news_path):
        st.error("Failed to process News File")

    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = session.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:    
        st.error(f"Failed to send data to NEWS API. Status code: {response.status_code}")
