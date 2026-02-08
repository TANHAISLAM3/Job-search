
from flask import Flask, jsonify, request, render_template
import http.client
import json
import datetime
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jobs")
def get_jobs():
    
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "9816876905msh4e3d99d3bf83b12p12f157jsnf3725b388ebd",
        'x-rapidapi-host': "jsearch.p.rapidapi.com"
    }
    search_term = request.args.get("query")
    safe_query = quote(search_term)

    
    conn.request(
        "GET",
        "/search?query=" + safe_query + "&page=1&num_pages=10&country=gb&date_posted=all",
        headers=headers
    )
    res = conn.getresponse()
    data = res.read()

    # Step 3: Convert JSON string to Python dictionary
    response = json.loads(data.decode("utf-8"))
    

    # Step 4: Extract job titles from response['data'] (you already know the structure)
    jobs = []
    for job in response.get("data", []):
    # Step 4a: Handle posted time
            posted = job.get("job_posted_human_readable")
            if not posted:
                dt_str = job.get("job_posted_at_datetime_utc")
                if dt_str:
                    import datetime
                    dt = datetime.datetime.fromisoformat(dt_str.replace("Z",""))
                    posted = dt.strftime("%d %b %Y, %H:%M")
            else:
                posted = "N/A"

    # Step 4b: Append job dictionary
            jobs.append({
                "title": job.get("job_title", "N/A"),
                "company": job.get("employer_name", "N/A"),
                "posted": posted,
                "publisher": job.get("job_publisher", "N/A"),
                "location": job.get("job_city", "N/A"),
                "link": job.get("job_apply_link", "#")
            })
    
    return render_template("index.html", jobs=jobs)
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)