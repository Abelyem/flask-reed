from flask import Flask, render_template, request
import requests, os
from reed_api import ReedAPI

app = Flask(__name__)

reed_api = ReedAPI()

@app.route('/', methods=['GET'])
def home():
    """
    Render the homepage with job listings based on search criteria.
    """
    # If search parameters are provided, fetch results
    if 'job-title' in request.args and 'location' in request.args:
        job_title = request.args['job-title']
        location = request.args['location']
        response = reed_api.search_jobs(job_title, location)
        return render_template('search_details.html', response=response)

    # Default search for junior developer jobs in London
    response = reed_api.search_jobs("software engineer", "london")
    return render_template('main.html', response=response)


if __name__ == "__main__":
    app.run(debug=True)

