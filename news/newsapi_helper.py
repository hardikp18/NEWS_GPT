import os
import requests
import json
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

api_key = os.environ.get("NEWS_API_KEY", "")
# Mock NEWS API response if base_url is not specified
base_url = os.environ.get("NEWS_BASE_URL", "https://newsapi.org/v2/everything?")

base_params = {
    "apiKey": api_key,
}


def get_url(params):
    query_parameters = {**params, **base_params}
    encode = urlencode(query_parameters)
    return f"{base_url}?{encode}"


def send_request(data_dir,params):
    response = requests.get(get_url(params))
    print(get_url(params))
    if response.status_code == 200:
        data = response.json()

        news_results = data.get('articles', [])
        
        # Create a single JSON file for  news items
        json_file_path = data_dir

        # with open(json_file_path, 'a') as json_file:
        #         json_file.write("[\n")
        result=[]
        with open(json_file_path+"/news.jsonl", 'w') as json_file:
            for idx,news in enumerate(news_results):
                title = news.get('title', '')
                description = news.get('description', '')
                content = news.get('content', '')
                url = news.get('url', '')
                publishedAt= news.get('publishedAt', '')
                
                result={"title": title, "description": description, "content": content,"url":url,"publishedAt":publishedAt}
                # print(idx)
                doc_object = {"doc": str(result)}
                json_file.write(json.dumps(doc_object) + '\n')
                # Store title, description, and content in the JSON file
                # json.dump({"title": title, "description": description, "content": content}, json_file)
                #     # print(index)
                # json_file.write("\n")
                #     # if(idx!=99):
                #     #     json_file.write(",\n")
                    
        
               
        # with open(json_file_path, 'a') as json_file:
        #         json_file.write("\n]")
        
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")



