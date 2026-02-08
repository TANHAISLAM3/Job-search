## Job Search Web App Using Flask and RapidAPI
* Overview 

This project is a Python Flask web application that fetches and displays live job listings using the JSearch API from RapidAPI. Users can search for jobs by entering a job role along with a location (for example: python developer london, software engineer uk, frontend intern manchester). The app returns real-time job results with key information in a simple interface.

* Features

The application displays:
• Job title
• Company name
• Location
• Posted time and date
• Job publisher
• Direct apply link

## Technologies Used

Flask – Web framework for backend routing and rendering
Python – Core programming language
RapidAPI (JSearch API) – Live job data source
HTML – Frontend template rendering
python-dotenv – Secure API key handling

* Project Structure

main.py
templates/
.env
.gitignore
README.md

## Setup and Installation

* Prerequisites

Make sure Python is installed on your system.

* Install required packages:

pip install flask python-dotenv

 * Clone the Repository

git clone https://github.com/YOUR_USERNAME/Job-search.git

cd Job-search

## Create Virtual Environment (Optional but recommended)

python -m venv venv
venv\Scripts\activate

* Create Environment File

In the project root, create a file named .env and add:

RAPIDAPI_KEY=your_api_key_here

(Get your API key from rapidapi.com)

## Run the Application

python main.py

## Open in browser:

http://127.0.0.1:5001

How It Works

The Flask backend sends requests to the JSearch API based on the user’s query. The API response is processed, formatted, and displayed dynamically on the webpage. Posted time is handled using both human-readable values and UTC timestamp conversion for accuracy.

## Security

The API key is stored securely in a .env file and excluded from GitHub using .gitignore so users can safely add their own keys.


### Usage Tips

Always include both job role and location in the search query for best results.

Example searches:
python developer london
data analyst uk
software engineer manchester

## Author

Built by Tanha
