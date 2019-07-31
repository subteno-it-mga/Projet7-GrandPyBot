# This file is needed to parse the user input
import unidecode
import json


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
