import urllib.request

from io import BytesIO
import json

import main as script
import secret

import pytest


############################
#                          #
#           TESTS          #
#                          #
############################


def test_sentence_parser():
    test_sentence = script.sentence_parser('bonjour où se situe domfront')
    assert test_sentence == ['domfront', ['domfront']]


def test_get_quote():
    test_quote = type(script.get_quote())
    assert test_quote == str


def test_returnLocation():

    assert script.ask_wiki(['domfront']) == ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>', {
        'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


def test_ask_wiki():

    assert script.returnLocation(
        'https://maps.googleapis.com/maps/api/geocode/json?address=domfront&key='+secret.api_key+'&region=fr') == 'ChIJLbE8JP-CCUgR4DdXgUA_6kY'


############################
#                          #
#           MOCK           #
#                          #
############################


def place_value(research_story):
    return ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>',
            {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


@pytest.fixture
def gh_patched_wiki(monkeypatch):
    import main
    monkeypatch.setattr(main, 'ask_wiki', place_value)


def test_send_back_good_wiki_place(gh_patched_wiki):
    from main import ask_wiki
    assert ask_wiki(['domfront']) == ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>',
                                      {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


def gmap_place(reasearch):
    return ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>',
            {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


@pytest.fixture
def gh_patched_gmap(monkeypatch):
    import main
    monkeypatch.setattr(main, 'returnLocation', gmap_place)


def test_send_back_good_gmap_place(gh_patched_gmap):
    from main import returnLocation
    assert returnLocation('https://maps.googleapis.com/maps/api/geocode/json?address=domfront&key=AIzaSyDQRt34q30uEv2kbukcbrmORJXwvBS3fI0&region=fr') == ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>',
            {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]
