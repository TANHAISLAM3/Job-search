
from flask import Flask, jsonify, request, render_template
import http.client
import json
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jobs")
def get_jobs():
    # Step 1: Connect to RapidAPI
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "9816876905msh4e3d99d3bf83b12p12f157jsnf3725b388ebd",
        'x-rapidapi-host': "jsearch.p.rapidapi.com"
    }
    search_term = request.args.get("query")
    safe_query = quote(search_term)

    # Step 2: Send request
    conn.request(
        "GET",
        "/search?query=" + safe_query + "&page=1&num_pages=1&country=us&date_posted=all",
        headers=headers
    )
    res = conn.getresponse()
    data = res.read()

    # Step 3: Convert JSON string to Python dictionary
    response = json.loads(data.decode("utf-8"))

    # Step 4: Extract job titles from response['data'] (you already know the structure)
    job_titles = [job['job_title'] for job in response['data']]

    # Step 5: Return as JSON response
    return jsonify(job_titles)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)