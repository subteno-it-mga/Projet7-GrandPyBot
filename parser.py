import unidecode
import json


def sentence_parser(sentence):
    words = sentence.split()
    extracted_stopwords = []

    with open('dist/stopword.json', 'r') as stopwords_from_file:

        data_stop = json.load(stopwords_from_file)

    new_sentence = []

    for word in words:
        if word not in data_stop:
            word_without_accent = unidecode.unidecode(word)
            new_sentence.append(word_without_accent)

    new_sentence_str = ''.join(str(i) for i in new_sentence)
    unaccented_sentence = unidecode.unidecode(new_sentence_str)

    sentence_for_geolocate = unaccented_sentence
    sentence_for_story = new_sentence

    sentence_list = [sentence_for_geolocate,sentence_for_story]

    return sentence_list
