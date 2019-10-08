# Projet7-RickPyBot

## Présentation

Application réalisée dans le cadre de la formation "Développeur d'application spécialité Python" au sein d'OpenClassRooms.

**Résumé de l'application :**

Demandez par exemple à RickPyBot : "Bonjour Rick, donne moi l'adresse de Domfront en Poiraie"
Vous validez la demande, il réfléchie puis vous réplique qu'il n'a pas vraiment mais vous donne tout de même les informations voulues.
Il vous affiche une map google puis une histoire associée au lieu s'il en trouve une. 

Vous pouvez tester l'application [en cliquant ici](https://rickpybot.herokuapp.com/)

Vous pouvez également contribuer ou bien vous amusez avec le projet en suivant les instructions qui vont suivre. Have fun :)

## Prérequis :

- Clé API GMAP valide
- Un ordinateur ?


### 1 - Installation

Pour récupérer le projet, placer vous en ligne de commande dans le répertoire où vous souhaitez récupérer le projet puis effectuer la commande suivante : 

```
git clone https://github.com/subteno-it-mga/Projet7-GrandPyBot.git
```

Cela va télécharger le projet sur votre pc.

### 2 - Fichier secret

Pour que le programme fonctionne correctement il va falloir que vous renommiez le ficher *secret.py.exemple* en *secret.py*.
Ouvrez le et remplacez la variable *api_key = "Your API key"* par votre propre clé API entre les quotes.

### 3 - L'environnement virtuel

Pour avoir les dépences propres au projet vous devez mettre en place l'environnement virtuel avec ces lignes de commande à la racine du projet :

```
python3 -m venv env
source env/bin/activate
```

### 4 - Intaller les dépendances

Pour installer les dépendances requises au projet, tapez la ligne de commande suivante :
```
pip install -r requirements.txt
```

### 5 - Lancer les tests

Effectuer la commande suivante à la racine du projet :

```
pytest
```

Si tout les tests sont verts, vous pouvez y aller, ça fonctionne bien ! Sinon, n'hésitez pas à me reporter un bug en m'envoyant un message ;)


### 6 - Lancer flask

Pour lancer Flask, rien de plus simple, effectuez la commande suivante :
```
flask run
```

Cela va lancer l'application et vous pourrez la retrouver à cette adresse : http://127.0.0.1:5000  (C'est la 'adresse par défault)

### 7 - Mise à jour

Pour avoir la dernière version du projet n'hésitez pas de temps en temps à faire un 
```
git pull
```


# HAVE FUN 

**Réalisé par Martin Gaucher pour OpenClassRooms**
