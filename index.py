'''
This is the pincipal view. This trigger function in main.py and display informations threaten in the
template.
'''
# import all flask dependencies for the project
from flask import Flask, request, render_template

# import other python files to threat the input and return the result
from main import jsondata, sentence_parser, data_treatment

import secret

# Define the app
APP = Flask(__name__)

# variable for the gmap url
GMAP_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
REGION_PARAM = "&region=fr"
API_KEY = secret.API_KEY

# the app stop on this route(url/process) to threat the input
@APP.route("/process", methods=["POST"])
def process():
    '''
    This route threat the informations in the input form from the template.
    '''
    # get the input value
    request_form = request.form
    # read and get the json values and put it in a dictionary
    read_data = jsondata(request_form)

    # parse the input to get the information needed for the gmap and wikimedia
    parse = sentence_parser(read_data)

    # the gmap url to threat
    gmap_get_json = GMAP_URL + parse[0] + "&key=" + API_KEY + REGION_PARAM

    # call the main function to send back map and wiki information
    search_data = data_treatment(parse, gmap_get_json, API_KEY)

    # send back the response to trigger .done in ajax function
    return search_data


# the main route for our app
@APP.route("/")
def index():
    '''
        Return the template index.html
    '''
    return render_template("index.html")


# If the app is found, run it
if __name__ == "__main__":
    APP.run(debug=True)
