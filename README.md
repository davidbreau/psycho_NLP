# PSYCHONLP

      ___           ___           ___           ___                       ___           ___     
     /__/\         /  /\         /  /\         /  /\          ___        /  /\         /  /\    
     \  \:\       /  /:/_       /  /:/_       /  /::\        /  /\      /  /:/_       /  /:/_   
      \__\:\     /  /:/ /\     /  /:/ /\     /  /:/\:\      /  /:/     /  /:/ /\     /  /:/ /\  
  ___ /  /::\   /  /:/ /::\   /  /:/ /::\   /  /:/~/:/     /__/::\    /  /:/ /:/_   /  /:/ /:/_ 
 /__/\  /:/\:\ /__/:/ /:/\:\ /__/:/ /:/\:\ /__/:/ /:/___  \__\/\:\  /__/:/ /:/ /\ /__/:/ /:/ /\
 \  \:\/:/__\/ \  \:\/:/~/:/ \  \:\/:/~/:/ \  \:\/:::::/     \  \:\ \  \:\/:/ /:/ \  \:\/:/ /:/
  \  \::/       \  \::/ /:/   \  \::/ /:/   \  \::/~~~~       \__\:\ \  \::/ /:/   \  \::/ /:/ 
   \  \:\        \  \:\/:/     \__\/ /:/     \  \:\            /  /:/  \  \:\/:/     \  \:\/:/  
    \  \:\        \  \::/        /__/:/       \  \:\          /__/:/    \  \::/       \  \::/   
     \__\/         \__\/         \__\/         \__\/          \__\/      \__\/         \__\/    


## Description

Ce projet comprend plusieurs aspects du traitement du langage naturel, dont l'analyse de texte, l'analyse de sentiments, l'utilisation de Hugging Face pour le fine-tuning des modèles, et le développement d'une application de suivi avec Django.

## Prérequis

* Python 3.8 ou plus récent
* Docker
* PostgreSQL
* ElasticSearch
* Django
* NLTK, Spacy, TextHero (si utilisés dans le projet)

## Installation

### Linux/MacOS

Cloner le répertoire du projet :
```sh
git clone https://github.com/davidbreau/psycho_NLP
cd votre_projet
```
Créer un environnement virtuel Python et l'activer :
```sh
python3 -m venv venv
source venv/bin/activate
```
Installer les dépendances du projet :
```sh
pip3 install -r requirements.txt
```

### Windows

Cloner le répertoire du projet :
```sh
git clone https://github.com/davidbreau/psycho_NLP
cd votre_projet
```
Créer un environnement virtuel Python et l'activer :
```sh
python -m venv venv
venv\Scripts\activate
```
Installer les dépendances du projet :
```sh
pip install -r requirements.txt
```

## Utilisation

Ici, vous expliqueriez comment exécuter les différentes parties du projet.

* Comment exécuter l'analyse des données et le développement initial du modèle dans le notebook Jupyter.
* Comment démarrer le conteneur Docker avec ElasticSearch et comment exécuter les commandes nécessaires pour configurer les données.
* Comment exécuter les requêtes sur les données ElasticSearch.
* Comment utiliser Hugging Face pour l'ajustement fin du modèle et l'évaluation.
* Comment exécuter l'application web Django.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces instructions :

* Forkez le projet
* Créez votre branche de fonctionnalités (git checkout -b feature/AmazingFeature)
* Committez vos changements (git commit -m 'Add some AmazingFeature')
* Poussez la branche (git push origin feature/AmazingFeature)
* Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE.md pour plus de détails.

