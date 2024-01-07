# NEWS_GPT
AI app to find real-time latest market news from various News Articles using the NEWS API.

It also uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources, leverages OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses.



![NEWS_GPT APP](/assets/video_gif.gif)

## How to run the project

Example only supports Unix-like systems (such as Linux, macOS, BSD). If you are a Windows user,  highly recommend leveraging Windows Subsystem for Linux (WSL) or Dockerize the app to run as a container.

### Run with Docker

1. [Set environment variables](#step-2-set-environment-variables)
2. From the project root folder, open your terminal and run `docker compose up`.
3. Navigate to `localhost:8501` on your browser when docker installion is successful.

### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.
4. (Optional): if you use NEWS API as a data source, create an [NEWS API](https://newsapi.org/) account and get a new API Key. Refer to NEWS API [documentation](https://newsapi.org/docs).

Then, follow the easy steps to install and get started using the sample app.

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone [https://github.com/hardikp18/NEWS_GPT.git](https://github.com/hardikp18/NEWS_GPT.git)
```

Next,  navigate to the project folder:

```bash
cd NEWS_GPT
```

### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and add the `{OPENAI_API_KEY} value`  configuration value with your key & replace HOST with suitable value. 

```bash
OPENAI_API_KEY="..." 
HOST="..."
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
NEWS_API_KEY=           
NEWS_BASE_URL=https://newsapi.org/v2/everything
PARAMETER="Microsoft"


```

Optionally, you change other values.  If you need actual data, you need to specify also `{NEWS_BASE_URL}` and `{NEWS_API_KEY}`.

```bash
NEWS_BASE_URL={NEWS_BASE_URL}
NEWS_API_KEY={NEWS_API_KEY}
```

### Step 3: Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```
### Step 4 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv pw-env && source pw-env/bin/activate
```

### Step 5: Run and start to use it

You start the application by navigating to `llm_app` folder and running `main.py`:

```bash
python main.py
```

### Step 6: Run Streamlit UI for file upload

You can run the UI separately running Streamlit app
`streamlit run app.py` command. It connects to the NEWS_GPT backend API automatically and you will see the UI frontend is running http://localhost:8501/ on a browser:


