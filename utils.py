import re
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

manual_filter = ['really', 'know', 'get', 'would', 'ive', 'still', 'even', 'want', 'way', 'could', 'back', 'make', 'going', 'im', 'one', 'bit', 'much', 'dont', 'day', 'one', 'always', 'something', 'today', 'go', 'cant', 'say', 'never', 'didnt', 'made', 'someone', 'many', 'felt', 'feelings', 'though', 'also', 'need', 'every', 'lot', 'around', "'s", 'look', 'every', 'new', 'year', 'able', 'got', 'also', 'less', 'last', 'days', 'come', 'actually', 'makes', 'http', 't', 'don', 'm', 's']
## Liste des mots qui ne sont pas dans les stopwords de NLTK mais que l'on souhaite tout de même retirer pour l'analyse et le modèle

def preprocess_text(text: str) -> str:
    """
    Preprocessing du text :
    Decontraction / tokenisation / lowercase / depunctuation / join
    """
    #### Decontraction
    # delete unnecessary spaces
    text = re.sub(r" '", "'", text)
    # specific
    text = re.sub(r"won\'t", "will not", text)
    text = re.sub(r"can\'t", "can not", text)
    # general
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    # 
    
    #### Tokenization
    tokens = word_tokenize(text) # Tokenization
    
    tokens = [token.lower() for token in tokens] #### Convertir en minuscules
    
    tokens = [token for token in tokens if token not in punctuation] #### Supprimer la ponctuation

    
    stop_words = set(stopwords.words("english")) #### Supprimer les stop words
    tokens = [token for token in tokens if token not in stop_words]
    
    tokens = [token for token in tokens if token not in manual_filter] #### Supprimer les mots spécifiques

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Ajout lemmatisation

    preprocessed_text = " ".join(tokens) #### Rejoindre les tokens en une chaîne de texte

    return preprocessed_text

