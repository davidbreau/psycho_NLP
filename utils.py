import re
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin
import emoji
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.punctuation = set(punctuation)
        self.stop_words = set(stopwords.words("english"))
        self.custom_stopwords = ['really', 'know', 'get', 'would', 'ive', 'still', 'even', 'want', 'way', 
                 'could', 'back', 'make', 'going', 'im', 'one', 'bit', 'much', 'dont', 'day', 
                 'one', 'always', 'something', 'today', 'go', 'cant', 'say', 'never', 'didnt', 
                 'made', 'someone', 'many', 'felt', 'feelings', 'though', 'also', 'need', 'every', 
                 'lot', 'around', "'s", 'look', 'every', 'new', 'year', 'able', 'got', 'also', 'less', 
                 'last', 'days', 'come', 'actually', 'makes', 'http', 't', 'don', 'm', 's', 'feeling', 'feel']
        self.lemmatizer = WordNetLemmatizer()
    
    
    def fit(self, X, y=None):
        return self
    
    
    def transform(self, X, y=None):
        """
        Preprocessing :
        tokenisation / lowercase / decontraction / demojize / depunctuation / stopwords / join
        """
        preprocessed_text = []
        for text in X:
            tokens = word_tokenize(text)                                   ### Tokenization
            
            tokens = [token.lower() for token in tokens]                   ### Convertir en minuscules
            
            tokens = re.sub(r" '", "'", tokens)                            ### Decontraction
            # specific
            tokens = re.sub(r"won\'t", "will not", tokens)
            tokens = re.sub(r"can\'t", "can not", tokens)
            # general
            tokens = re.sub(r"n\'t", " not", tokens)
            tokens = re.sub(r"\'re", " are", tokens)
            tokens = re.sub(r"\'s", " is", tokens)
            tokens = re.sub(r"\'d", " would", tokens)
            tokens = re.sub(r"\'ll", " will", tokens)
            tokens = re.sub(r"\'t", " not", tokens)
            tokens = re.sub(r"\'ve", " have", tokens)
            tokens = re.sub(r"\'m", " am", tokens)

            tokens = emoji.demojize(tokens)                                  ### Gestion des émojis
            
            tokens = [token for token in tokens if token not in punctuation] #### Supprimer la ponctuation

            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]  ### Ajout lemmatisation

            stop_words = set(stopwords.words("english"))                     ### Supprimer les stop words
            tokens = [token for token in tokens if token not in stop_words]
            tokens = [token for token in tokens if token not in self.custom_stopwords]

            preprocessed_text = " ".join(tokens)                           ### Rejoindre les tokens en une chaîne de texte

        return preprocessed_text

