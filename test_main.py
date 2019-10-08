"""
This file testing the function in the code to verify in case of modifications if the app run
properly.
"""
import main
import secret

############################
#                          #
#           TESTS          #
#                          #
############################


def test_sentence_parser():
    """
        Test if the sentence parse send back the good keywords
    """
    test_sentence = main.sentence_parser("bonjour où se situe domfront")
    assert test_sentence == ["domfront", ["domfront"]]


def test_get_quote():
    """
        Verify if the quotes given is in a string format.
    """
    test_quote = type(main.get_quote())
    assert test_quote == str


def test_ask_wiki():
    """
        Test if the location returned by the wikipedia API is fine.
    """
    assert main.ask_wiki(["domfront"]) == ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>', {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


def test_return_location():
    """
        Test if the story returned by the gmap API is fine.
    """
    assert (
        main.return_location(
            "https://maps.googleapis.com/maps/api/geocode/json?address=domfront&key="
            + secret.API_KEY
            + "&region=fr"
        )
        == "ChIJLbE8JP-CCUgR4DdXgUA_6kY"
    )


############################
#                          #
#           MOCK           #
#                          #
############################


def test_send_back_good_wiki_place(monkeypatch):
    """
        Fake a request of wiki API with the monkeypatch.
    """

    def place_value(self):
        """
            Fake the response of the wiki API.
        """
        return ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>', {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]

    monkeypatch.setattr(main, "ask_wiki", place_value)

    assert main.ask_wiki(["domfront"]) == ['<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>', {'pageid': 38275, 'ns': 0, 'title': 'Domfront (Orne)', 'extract': '<p class="mw-empty-elt">\n</p>\n<p><b>Domfront</b> est une ancienne commune française, située dans le département de l\'Orne en région Normandie, devenue le <time class="nowrap date-lien" datetime="2016-01-01" data-sort-value="2016-01-01">1<sup>er</sup> janvier 2016</time> une commune déléguée au sein de la commune nouvelle de Domfront en Poiraie.\n</p><p>Elle est peuplée de 3&#160;486 habitants.</p>'}]


def test_send_back_good_gmap_place(monkeypatch):
    """
        Fake a request of gmap API with the monkeypatch.
    """

    def gmap_place(self):
        """
            Fake the response of the gmap API.
        """

        return "ChIJLbE8JP-CCUgR4DdXgUA_6kY"

    monkeypatch.setattr(main, "return_location", gmap_place)

    assert main.return_location(
        "https://maps.googleapis.com/maps/api/geocode/json?address=domfront&key="
        + secret.API_KEY
        + "&region=fr"
    ) == "ChIJLbE8JP-CCUgR4DdXgUA_6kY"
