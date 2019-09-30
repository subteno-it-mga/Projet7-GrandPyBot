import json
import os
import sys
import unidecode
import urllib.request
import random

from flask import jsonify

quotes = [
    "<p class='quote'>Wubba Lubba Dub Dub ! J'ai trouvé ! Tient : </p>",
    "<p class='quote'>Tu m'embêtes avec tes questions mais dans cette réalité voici le résultat: </p>",
    "<p class='quote'>A quoi ça te sert de connaître ça ? Tu vas mourir un jour avec cette information de toute façon. Mais tient, si ça peut t'amuser :</p>",
    "<p class='quote'>T'aurais pas autre chose à faire comme profiter de ton existence au lieu de me demander ça ? Mais bon, voilà ce que j'ai trouvé :</p>",
    "<p class='quote'>T-tu me déranges alors que je bois un coup BUUURRP. C-comment ça je bois tout le temps ? Prend ça et file:</p>"

]

def jsondata(request):

    for key in request.keys():
        data=key
    data_dic=json.loads(data)

    return data_dic

# This file is needed to parse the user input

def sentence_parser(sentence):
    # split the user input in an array
    words = sentence.split()

    extracted_stopwords = []

    # open the json file with the stopwords
    with open('dist/stopword.json', 'r') as stopwords_from_file:

        data_stop = json.load(stopwords_from_file)

    new_sentence = []

    # compare the words in sentence with words in the stopwords file
    for word in words:
        if word.lower() not in data_stop:
            # remove accent, punctuation, etc
            word_without_accent = unidecode.unidecode(word)
            # append the result in an array
            new_sentence.append(word_without_accent)

    # join the sentence for the gmap research
    new_sentence_str = ''.join(str(i) for i in new_sentence)
    unaccented_sentence = unidecode.unidecode(new_sentence_str)

    sentence_for_geolocate = unaccented_sentence
    sentence_for_story = new_sentence

    sentence_list = [sentence_for_geolocate,sentence_for_story]

    # return the data for the gmap and wiki page
    return sentence_list

def returnLocation(research):
    
    with urllib.request.urlopen(research, timeout=4) as url:
        data = json.loads(url.read().decode())
    data_place_id = data['results'][0]['place_id']

    return data_place_id

def get_quote():
    random_number = random.randint(0,len(quotes)-1)
    random_quote = quotes[random_number]
    return random_quote

def ask_wiki(research_story):

    research_story_formated = '%20'.join(str(i) for i in research_story)
    url_wiki = "https://fr.wikipedia.org/w/api.php?"

    action_type = "query"
    action = "action=%s"%(action_type)

    format_type = "json"
    final_format ="&format=%s"%(format_type)

    list_type = "search"
    final_list = "&list=%s"%(list_type)

    your_research = research_story_formated
    search = "&srsearch=%s"%(your_research)

    final_url = url_wiki+action+final_format+final_list+search

    # Go for the url to get json file
    with urllib.request.urlopen(final_url, timeout=4) as url:
        data = json.loads(url.read().decode())

    # the id for the wiki page. Then click on the wikipedia link to go for the entire page
    data_story_page_id = data['query']['search'][0]["pageid"]

    page_id = data_story_page_id
    param = "&prop=extracts&exsentences=2&exlimit=max"

    # only extract a part of the page and the 2 first sentences
    final_second_url = url_wiki + action + final_format + "&pageids=" + str(page_id) + param
    with urllib.request.urlopen(final_second_url, timeout=4) as url_extract:
        data_second = json.loads(url_extract.read().decode())

    data_story = data_second['query']['pages'][str(page_id)]["extract"]
    data_page = data_second['query']['pages'][str(page_id)]
        
    data_list = [data_story,data_page]

    # return the list of the wiki id and the piece of information of this wiki page
    return data_list

def data_treatment(parse,gmap_get_json,api_key):
    try:
        # search and return for the location id
        returnJson_place_id = returnLocation(gmap_get_json)
        the_url = "https://www.google.com/maps/embed/v1/place?q=place_id:%s&key=%s" % (
        returnJson_place_id,api_key)

        # return the url route
        route = '<iframe height="300px" frameborder="0" style="border:0" src=%s allowfullscreen></iframe></div>' % (
        the_url)

    # if no place is found return an error message
    except SyntaxError:
        route = "Un univers inconnu ? Impossible !"
    except IndexError:
        route = "Cet univers n'est pas connu de nos services !"

    # try data to return the wiki page
    try:

        # search and return a wiki page about the place
        get_story = ask_wiki(parse[1])

        # return a random quote from Rick
        random_sentence = get_quote()

        #return the wikipedia place
        get_story_final = random_sentence+get_story[0]+"<a target='_blank' href='http://fr.wikipedia.org/?curid=%s'>EN SAVOIR PLUS SUR WIKIPEDIA</a>"%(get_story[1]['pageid'])

    # if there is no story to tell return an error message    
    except IndexError:
        get_story_final = "J'ai pas d'histoire à te raconter là dessus. Peut être dans une prochaine aventure ?"
    except SyntaxError:
        get_story_final = "Je ne trouve pas ça dans ma base de donnée... Tu essaies de me dupper ??"
    
    # jsonify the response for the query treatment
    resp = jsonify(phrase = parse, map = route, story = get_story_final)

    return resp

