import importlib
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

if __name__ == "__main__":
    # Fetch data related to a company from NEWS API
    try:
        cmd = ["python3", "news/data_ingestion_cron_job.py"]

        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Script execution failed.")
    except FileNotFoundError:
        print("Python interpreter or the script was not found.")

    # Run NEWS API
    host = os.environ.get("HOST", "172.18.135.165")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("backend.app")
    print("App Running")
    app_api.run(host=host, port=port)
