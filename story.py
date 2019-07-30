# import needed dependencies
import urllib.request, json 
import unidecode

# function to search and return the story from a place
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