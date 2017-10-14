from flask import Flask
import requests as req
import FindAndSendFlightWithProblem as fas
import CheckDifferences as cd
app = Flask(__name__)

"""
Here is the place, where the web server is going to run
incoming and outgoing requests will be processed here
"""


@app.route('/check')
def check_last_situation():

    # After other two classes are created, they'll be put here in a corresponding logic
    # As if there is a new change in the system, so that at the end the appearance
    # is changed

    pass


@app.route('/')
def main_page():

    cd.CheckDifferences().read_file()

    return "Here is the main page!!!"


