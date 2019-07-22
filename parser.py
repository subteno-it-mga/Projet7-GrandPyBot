from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import unidecode


def sentence_parser(sentence):
    stop_words = set(stopwords.words('french'))
    words = word_tokenize(sentence)

    new_sentence = []

    for word in words:
        if word not in stop_words:
            new_sentence.append(word)

    new_sentence_str = ''.join(str(i) for i in new_sentence)
    unaccented_sentence = unidecode.unidecode(new_sentence_str)
    return unaccented_sentence
