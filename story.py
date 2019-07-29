import urllib.request, json 
import unidecode
def ask_wiki(research_story):

    research_story = str(research_story)
    research_story_formated = research_story.replace(" ","%20")
    unaccented_research = unidecode.unidecode(research_story_formated)

    test_url = "https://fr.wikipedia.org/w/api.php?"

    test_action_type = "query"
    test_action = "action=%s"%(test_action_type)

    test_format_type = "json"
    test_format ="&format=%s"%(test_format_type)

    test_list_type = "search"
    test_list = "&list=%s"%(test_list_type)

    test_your_research = unaccented_research
    test_search = "&srsearch=%s"%(test_your_research)

    test_final_url = test_url+test_action+test_format+test_list+test_search

    with urllib.request.urlopen(test_final_url, timeout=4) as url:
        data = json.loads(url.read().decode())
    data_story_page_id = data['query']['search'][0]["pageid"]

    page_id = data_story_page_id
    test_param = "&prop=extracts&exsentences=2&exlimit=max"

    test_final_second_url = test_url+test_action+test_format+"&pageids="+str(page_id)+test_param
    with urllib.request.urlopen(test_final_second_url, timeout=4) as url_extract:
        data_second = json.loads(url_extract.read().decode())

    data_story = data_second['query']['pages'][str(page_id)]["extract"]
    data_page = data_second['query']['pages'][str(page_id)]
        
    data_list = [data_story,data_page]

    return data_list