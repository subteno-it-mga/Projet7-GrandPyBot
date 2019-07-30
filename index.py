# /index.py

# import all flask dependencies for the project
from flask import Flask, request, jsonify, render_template, redirect, make_response

# import other python files to threat the input and return the result
from parser import sentence_parser
from geolocate import returnLocation
from story import ask_wiki
from random_quotes import get_quote

# import others dependencies
import json
import os
import sys

# Define the app
app = Flask(__name__)

# variable for the gmap url
gmap_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
api_key = "&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0"
region_param = "&region=fr"

# the app stop on this route(url/process) to threat the input 
@app.route('/process', methods=['POST'])
def process():
    # get the input value
    rf = request.form

    #read and get the json values and put it in a dictionary
    for key in rf.keys():
        data=key
    data_dic=json.loads(data)

    # parse the input to get the information needed for the gmap and wikimedia
    parse = sentence_parser(data_dic)

    # the gmap url to threat
    gmap_get_json = gmap_url+parse[0]+api_key+region_param

    # declare the variables needed to stock information in the try/except
    returnJson_place_id = ""
    the_url = ""
    route = ""
    get_story = ""
    get_story_final=""

    # try data to return the map
    try:
        # search and return for the location id
        returnJson_place_id = returnLocation(gmap_get_json)
        the_url = "https://www.google.com/maps/embed/v1/place?q=place_id:%s&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0" % (
        returnJson_place_id)

        # return the url route
        route = '<iframe height="300px" frameborder="0" style="border:0" src=%s allowfullscreen></iframe></div>' % (
        the_url)

    # if no place is found return an error message
    except:
        route = "Pas de correspondance"

    # try data to return the wiki page
    try:

        # search and return a wiki page about the place
        get_story = ask_wiki(parse[1])

        # return a random quote from Rick
        random_sentence = get_quote()

        #return the wikipedia place
        get_story_final = random_sentence+get_story[0]+"<a target='_blank' href='http://fr.wikipedia.org/?curid=%s'>EN SAVOIR PLUS SUR WIKIPEDIA</a>"%(get_story[1]['pageid'])

    # if there is no story to tell return an error message    
    except:
        print("Unexpected error:", sys.exc_info()[0])
        get_story_final = "Pas d'histoire à raconter"
    
    # jsonify the response for the query treatment
    resp = jsonify(phrase = parse, map = route, story = get_story_final)

    # send back the response to trigger .done in ajax function
    return resp

# the main route for our app
@app.route('/')
def index():
    return render_template('index.html')

# If the app is found, run it
if __name__ == "__main__":
    app.run(debug=True)

