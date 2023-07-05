import re
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

custom_stopwords = ['really', 'know', 'get', 'would', 'ive', 'still', 'even', 'want', 'way', 
                 'could', 'back', 'make', 'going', 'im', 'one', 'bit', 'much', 'dont', 'day', 
                 'one', 'always', 'something', 'today', 'go', 'cant', 'say', 'never', 'didnt', 
                 'made', 'someone', 'many', 'felt', 'feelings', 'though', 'also', 'need', 'every', 
                 'lot', 'around', "'s", 'look', 'every', 'new', 'year', 'able', 'got', 'also', 'less', 
                 'last', 'days', 'come', 'actually', 'makes', 'http', 't', 'don', 'm', 's', 'feeling', 'feel', 'wa',
                 'like','time', 'thing', 'people', 'life', 'little', 'ha', 'right', 'see', 'work',
                 'think', 'week', 'enough', 'sure', 'le', 'quite', 'pretty']

class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.punctuation = set(punctuation)
        self.stop_words = set(stopwords.words("english"))
        self.custom_stopwords = custom_stopwords
        self.lemmatizer = WordNetLemmatizer()
    
    
    def fit(self, X, y=None):
        return self
    
    
    def transform(self, X):
        """
        Preprocessing :
        tokenisation / lowercase / decontraction / demojize / depunctuation / stopwords / join
        """
        preprocessed_text = []
        for text in X:

            tokens = word_tokenize(text)                                   ### Tokenization

            tokens = [token.lower() for token in tokens]                   ### Convertir en minuscules
            
            tokens = [token for token in tokens if token not in self.punctuation] #### Supprimer la ponctuation

            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]  ### Ajout lemmatisation

            stop_words = set(stopwords.words("english"))                     ### Supprimer les stop words
            tokens = [token for token in tokens if token not in self.stop_words]
            tokens = [token for token in tokens if token not in self.custom_stopwords]

            preprocessed_text.append(' '.join(tokens))                             ### Rejoindre les tokens en une chaîne de texte

        return preprocessed_text

text_t = TextPreprocessor()

print(text_t.transform(['text as example ']))
