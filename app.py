from flask import Flask, render_template, redirect, request
import requests, os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_PASS = os.getenv("API_PASS")


@app.route('/', methods=['GET'])
def home():

    if 'job-title' in request.args and 'location' in request.args:
        name = request.args['job-title']
        location = request.args['location']
        url = requests.get(f"https://www.reed.co.uk/api/1.0/search?keywords={name}&locationName={location}", auth=(API_KEY, API_PASS))
        response = url.json()
        return render_template ('search_details.html', response=response)
    
    x=requests.get("https://www.reed.co.uk/api/1.0/search?keywords=junior+developer&locationName=london", auth=(API_KEY, API_PASS))
    response= x.json()
    return render_template('main.html', response=response)


if __name__ == "__main__":
    app.run(debug=True)





# def home(request):
#    x=requests.get("https://www.reed.co.uk/api/1.0/search?keywords=junior+developer&locationName=london", auth=(API_KEY, API_PASS))
#    response= x.json()
#    if 'name' and 'locationName' in request.GET:
#       name = request.GET['name']
#       location = request.GET['locationName']
#       url = requests.get(f"https://www.reed.co.uk/api/1.0/search?keywords=junior+developer+{name}&locationName={location}", auth=(API_KEY, API_PASS))
#       response = url.json()
#       return render (request, 'job_details/details.html', {'response': response})
#    return render(request, 'reed_home/index.html', {'response': response})