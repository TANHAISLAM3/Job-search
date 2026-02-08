from flask import Flask, request, render_template
import http.client
import json
import datetime
from urllib.parse import quote
import os
from dotenv import load_dotenv
from pathlib import Path


# Get current folder
cwd = Path.cwd()
print("Current folder:", cwd)

# Path to .env
env_path = cwd / ".env"
print(".env exists?", env_path.exists())

# Load .env
load_dotenv(dotenv_path=r"C:\Users\tanha\OneDrive\Desktop\job_search_project\.env")

# Load key
API_KEY = os.getenv("RAPIDAPI_KEY")
print("Loaded API_KEY:", API_KEY)
app = Flask(__name__)

@app.route("/")
def home():
    # Pass empty jobs list on first load
    return render_template("index.html", jobs=[])

@app.route("/jobs")
def get_jobs():
    search_term = request.args.get("query")
    if not search_term:
        return render_template("index.html", jobs=[])

    safe_query = quote(search_term)

    # Connect to JSearch API
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    conn.request(
        "GET",
        f"/search?query={safe_query}&page=1&num_pages=10&country=gb&date_posted=all",
        headers=headers
    )

    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode("utf-8"))

    jobs = []
    for job in response.get("data", []):
        # Handle posted date
        posted = job.get("job_posted_human_readable")
        if not posted:
            dt_str = job.get("job_posted_at_datetime_utc")
            if dt_str:
                dt = datetime.datetime.fromisoformat(dt_str.replace("Z",""))
                posted = dt.strftime("%d %b %Y, %H:%M")
            else:
                posted = "N/A"

        # Append job dictionary
        jobs.append({
            "title": job.get("job_title", "N/A"),
            "company": job.get("employer_name", "N/A"),
            "posted": posted,
            "publisher": job.get("job_publisher", "N/A"),
            "location": job.get("job_city", "N/A"),
            "link": job.get("job_apply_link", "#")
        })

    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
