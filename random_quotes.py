# function to get random quotes

import random

quotes = [
    "<p class='quote'>Wubba Lubba Dub Dub ! J'ai trouvé ! Tient : </p>",
    "<p class='quote'>Tu m'embêtes avec tes questions mais dans cette réalité voici le résultat: </p>",
    "<p class='quote'>A quoi ça te sert de connaître ça ? Tu vas mourir un jour avec cette information de toute façon. Mais tient, si ça peut t'amuser :</p>",
    "<p class='quote'>T'aurais pas autre chose à faire comme profiter de ton existence au lieu de me demander ça ? Mais bon, voilà ce que j'ai trouvé :</p>",
    "<p class='quote'>T-tu me déranges alors que je bois un coup BUUURRP. C-comment ça je bois tout le temps ? Prend ça et file:</p>"

]

def get_quote():
    random_number = random.randint(0,len(quotes))
    random_quote = quotes[random_number]
    return random_quote
