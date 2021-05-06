import nltk


class Setup:

    def __init__(self):
        nltk.download("stopwords")
        nltk.download('punkt')
        nltk.download('wordnet')
