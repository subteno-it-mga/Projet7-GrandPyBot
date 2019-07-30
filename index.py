# /index.py
from flask import Flask, request, jsonify, render_template, redirect, make_response
from parser import sentence_parser
from geolocate import returnLocation
from story import ask_wiki
from random_quotes import get_quote
import os
import json
import pusher

app = Flask(__name__)

gmap_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
api_key = "&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0"
region_param = "&region=fr"


@app.route('/process', methods=['POST'])
def process():
    rf = request.form
    for key in rf.keys():
        data=key
    data_dic=json.loads(data)
    parse = sentence_parser(data_dic)
    gmap_get_json = gmap_url+parse[0]+api_key+region_param
    returnJson_place_id = ""
    the_url = ""
    route = ""
    get_story = ""
    get_story_final=""
    try:
        returnJson_place_id = returnLocation(gmap_get_json)
        the_url = "https://www.google.com/maps/embed/v1/place?q=place_id:%s&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0" % (
        returnJson_place_id)
        route = '<iframe height="300px" frameborder="0" style="border:0" src=%s allowfullscreen></iframe></div>' % (
        the_url)
    except IndexError as index_err:
        route = "Pas de correspondance"

    try:
        get_story = ask_wiki(parse[1])
        random_sentence = get_quote()
        get_story_final = random_sentence+get_story[0]+"<a target='_blank' href='http://fr.wikipedia.org/?curid=%s'>EN SAVOIR PLUS SUR WIKIPEDIA</a>"%(get_story[1]['pageid'])
    except IndexError as index_err:
        get_story_final = "Pas d'histoire à raconter"
    
    resp = jsonify(phrase = parse, map = route, story = get_story_final)

    return resp


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

