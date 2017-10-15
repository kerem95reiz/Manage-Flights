from flask import Flask
from ProvideLatestSituation import ProvideLatestSituation as prolasit
import json
app = Flask(__name__)

"""
Here is the place, where the web server is going to run
incoming and outgoing requests will be processed here
"""


@app.route('/check')
def check_last_situation():
    provide_sit = prolasit()
    return provide_sit.provide_lat_sit()


@app.route('/test')
def test_response():

    with open('./source/example_response.json') as data_file:
        response = json.load(data_file)

    print(response)
    return response.__str__()


@app.route('/')
def main_page():

    return "Here is the main page!!!"


