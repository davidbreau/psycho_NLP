import re
from nltk.corpus import stopwords
from string import punctuation

manual_filter = [',', 'really', 'know', 'get', 'would', 'ive', 'still', 'even', 'want', 'way', 'could', 'back', 'make', 'going', 'im', 'one', 'bit', 'much', 'dont', 'day', 'one', 'always', 'something', 'today', 'go', 'cant', 'say', 'never', 'didnt', 'made', 'someone', 'many', 'felt', 'feelings', 'though', 'also', 'need', 'every', 'lot', 'around', "'s", 'look', 'every', 'new', 'year', 'able', 'got', 'also', 'less', 'last', 'days', 'come', 'actually', 'makes', 'http', 't', 'don', 'm', 's']
## Liste des mots qui ne sont pas dans les stopwords de NLTK mais que l'on souhaite tout de même retirer pour l'analyse et le modèle

def preprocess_text(text):
    text = text.lower()                 # met en minuscule
    
    text = re.sub(r'[^\w\s]', '', text) #enlève la ponctuation

    # Supprimer les stop words
    stop_words = set(stopwords.words("english"))
    text = " ".join(word for word in text.split() if word not in stop_words)
    text = " ".join(word for word in text.split() if word not in manual_filter)

    return text
