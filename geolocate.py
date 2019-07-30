# function to get the place id in gmap API

import urllib.request, json 
def returnLocation(research):
    
    with urllib.request.urlopen(research, timeout=4) as url:
        data = json.loads(url.read().decode())
    data_place_id = data['results'][0]['place_id']

    return data_place_id