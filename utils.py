import re
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from sklearn.base import BaseEstimator, TransformerMixin
import emoji
import nltk
nltk.download('punkt')
custom_stopwords = ['really', 'know', 'get', 'would', 'ive', 'still', 'even', 'want', 'way', 
                 'could', 'back', 'make', 'going', 'im', 'one', 'bit', 'much', 'dont', 'day', 
                 'one', 'always', 'something', 'today', 'go', 'cant', 'say', 'never', 'didnt', 
                 'made', 'someone', 'many', 'felt', 'feelings', 'though', 'also', 'need', 'every', 
                 'lot', 'around', "'s", 'look', 'every', 'new', 'year', 'able', 'got', 'also', 'less', 
                 'last', 'days', 'come', 'actually', 'makes', 'http', 't', 'don', 'm', 's', 'feeling', 'feel']
## Liste des mots qui ne sont pas dans les stopwords de NLTK mais que l'on souhaite tout de même retirer pour l'analyse et le modèle
class Text_Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def preprocess_text(text: str) -> str:
        """
        Preprocessing :
        tokenisation / lowercase / decontraction / demojize / depunctuation / stopwords / join
        """
        tokens = word_tokenize(text) ### Tokenization
        
        tokens = [token.lower() for token in tokens] #### Convertir en minuscules
        
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

        text = emoji.demojize(text) ### Gestion des émojis
        
        tokens = [token for token in tokens if token not in punctuation] #### Supprimer la ponctuation

        stop_words = set(stopwords.words("english")) #### Supprimer les stop words
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [token for token in tokens if token not in custom_stopwords]

        preprocessed_text = " ".join(tokens) #### Rejoindre les tokens en une chaîne de texte

        return preprocessed_text
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        pass

