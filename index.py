# /index.py

# import all flask dependencies for the project
from flask import Flask, request, jsonify, render_template, redirect, make_response

# import other python files to threat the input and return the result
from main import *

import secret

# import others dependencies
import json
import os
import sys

# Define the app
app = Flask(__name__)

# variable for the gmap url
gmap_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
region_param = "&region=fr"
api_key = secret.api_key

# the app stop on this route(url/process) to threat the input 
@app.route('/process', methods=['POST'])
def process():
    # get the input value
    rf = request.form
    
    #read and get the json values and put it in a dictionary
    read_data = jsondata(rf)

    # parse the input to get the information needed for the gmap and wikimedia
    parse = sentence_parser(read_data)

    # the gmap url to threat
    gmap_get_json = gmap_url+parse[0]+"&key="+api_key+region_param

    # call the main function to send back map and wiki information
    search_data = data_treatment(parse,gmap_get_json,api_key)

    # send back the response to trigger .done in ajax function
    return search_data

# the main route for our app
@app.route('/')
def index():
    return render_template('index.html')

# If the app is found, run it
if __name__ == "__main__":
    app.run(debug=True)

