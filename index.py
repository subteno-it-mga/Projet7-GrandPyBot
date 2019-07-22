# /index.py
from flask import Flask, request, jsonify, render_template, redirect, make_response
from parser import sentence_parser
from geolocate import returnLocation
from story import ask_wiki
import os
import dialogflow
import requests
import json
import pusher

# https://maps.googleapis.com/maps/api/geocode/json?address=2placeAlbertChristophleDomfrontenPoiraieFR&key=AIzaSyB0ljmd8zC5jJoMmKbVHjdq02FGbFix6t8

app = Flask(__name__)

gmap_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
api_key = "&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0"


@app.route('/process', methods=['POST'])
def process():
    receive_input = request.form['text']
    receive_input_processed = sentence_parser(receive_input)
    gmap_get_json = gmap_url+receive_input_processed+api_key
    returnJson_place_id = returnLocation(gmap_get_json)
    the_url = "https://www.google.com/maps/embed/v1/place?q=place_id:%s&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0" % (
        returnJson_place_id)
    route = '<iframe class="col-md-12" height="600px" frameborder="0" style="border:0" src=%s allowfullscreen></iframe></div>' % (
        the_url)
    get_story = ask_wiki(receive_input)
    return render_template('index.html',testgmap = route,teststory=get_story)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
