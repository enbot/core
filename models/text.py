import nltk
import re

from nltk.sentiment.util import mark_negation

class TextModel:

    def __init__(self):
        print('starting...')
        self.__allowed_characters = re.compile('[^a-zA-Z0-9 ]')
        self.__stemmer = nltk.stem.SnowballStemmer("english", ignore_stopwords=True)
        # self.__stemmer = nltk.stem.PorterStemmer()
        # self.__stemmer = nltk.stem.LancasterStemmer()
        self.__lemmatizer = nltk.WordNetLemmatizer()

        default_stopwords = nltk.corpus.stopwords.words("english") 
        custom_stopwords = ["feel", "wouldnt", "wont", "werent", "shouldnt", "shant", "neednt", "mustnt", "mightnt", "isnt", "havent", "hadnt", "hasnt", "hadnt", "doesnt", "couldnt", "arent", "aint", "shouldve", "shes", "her's", "youll", "youd", "youre", "ill", "mine", "didnt", "im", "ive", "ha", "dont", "wasnt", "wa"]
        negation_stopwords = [word + "_NEG" for word in default_stopwords + custom_stopwords]   

        self.__stopwords = default_stopwords + custom_stopwords + negation_stopwords

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
        phrase = self.__resolveNegation(phrase)
        phrase = self.__removeStopwords(phrase)
        # phrase = self.__posTag(phrase)
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

    def __resolveNegation(self, phrase):
        words = nltk.word_tokenize(phrase)
        new_words = mark_negation(words)
        new_phrase = ' '.join(new_words)
        return new_phrase

    def __posTag(self, phrase):
        words_with_neg = phrase.split(" ")
        words_without_neg = [word.replace('_NEG', '') for word in words_with_neg]
        words_tagged = nltk.pos_tag(words_without_neg)

        phrase_size = len(words_with_neg)

        ignored_tags = ["WDT", "CC", "DET", "CD", "PRP", "PRP$", "PDT", "SYM", ".", "X", "WP", "WP$", "WRB"]
        new_words = []

        for index in range(phrase_size):
            word_with_neg = words_with_neg[index]
            word_tagged = words_tagged[index]

            tag =  word_tagged[1]

            if tag not in ignored_tags:
                new_words.append(word_with_neg)
            # else:
            #     print(word_tagged)

        new_phrase = ' '.join(new_words)

        return new_phrase
