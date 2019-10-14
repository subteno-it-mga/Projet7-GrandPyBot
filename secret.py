'''
This file contain the secret GMAP API KEY
'''
import os
API_KEY_HEROKU = os.environ.get('API_KEY')

if API_KEY_HEROKU:
    API_KEY = os.environ.get('API_KEY')
else:
    API_KEY = "AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0"
