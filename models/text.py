import nltk
import re

from nltk.sentiment.util import mark_negation


class TextModel:

    def __init__(self):
        self.__allowed_characters = re.compile('[^a-zA-Z0-9 ]')
        self.__stemmer = nltk.stem.SnowballStemmer("english", ignore_stopwords=True)
        self.__lemmatizer = nltk.WordNetLemmatizer()

        default_stopwords = nltk.corpus.stopwords.words("english") 
        custom_stopwords = ["wouldnt", "wont", "werent", "shouldnt", "shant", "neednt", "mustnt", "mightnt", "isnt", "havent", "hadnt", "hasnt", "hadnt", "doesnt", "couldnt", "arent", "aint", "shouldve", "shes", "her's", "youll", "youd", "youre", "ill", "mine", "didnt", "im", "ive", "ha", "dont", "wasnt", "wa"]

        self.__stopwords = default_stopwords + custom_stopwords

    def getDatasetUniqueWords(self, emotions_dataset):
        all_phrases = " ".join(phrase for (phrase, emotion) in emotions_dataset)
        all_words = nltk.word_tokenize(all_phrases)
        words_frequency_distribution = nltk.FreqDist(all_words)
        unique_words = words_frequency_distribution.keys()
        return unique_words

    def applyDatasetModifiers(self, emotions_dataset):
        new_emotions_dataset = []
        for (phrase, emotion) in emotions_dataset:
            new_phrase = self.applyTextModifiers(phrase)
            new_emotions_dataset.append((new_phrase, emotion))
        return new_emotions_dataset

    def applyTextModifiers(self, phrase):
        phrase = self.__normalizeText(phrase)
        phrase = self.__applyStemmer(phrase)
        phrase = self.__applyLemmatizer(phrase)
        phrase = self.__removeStopwords(phrase)
        return phrase

    def __normalizeText(self, phrase):
        phrase = phrase.lower()
        phrase = self.__allowed_characters.sub('', phrase)
        return phrase

    def __removeStopwords(self, phrase):
        words = nltk.word_tokenize(phrase)
        new_words = [word for word in words if word not in self.__stopwords]
        new_phrase = ' '.join(new_words)
        return new_phrase

    def __applyStemmer(self, phrase):
        words = nltk.word_tokenize(phrase)
        new_words = [self.__stemmer.stem(w) for w in words]
        new_phrase = ' '.join(new_words)
        return new_phrase

    def __applyLemmatizer(self, phrase):
        words = nltk.word_tokenize(phrase)
        new_words = [self.__lemmatizer.lemmatize(w) for w in words]
        new_phrase = ' '.join(new_words)
        return new_phrase
