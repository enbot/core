import nltk


class TextModel:

    def __init__(self):
        self.__stopwords = nltk.corpus.stopwords.words('english')
        self.__stemmer = nltk.stem.PorterStemmer()

    def applyModifiers(self, emotions_dataset):
        new_emotions_dataset = []

        for (phrase, emotion) in emotions_dataset:
            stopword_phrase = self.__removeStopwords(phrase)
            stemmer_phrase = self.__applyStemmer(stopword_phrase)
            new_emotions_dataset.append((stemmer_phrase, emotion))

        return new_emotions_dataset

    def __removeStopwords(self, phrase):
        lower_phrase = phrase.lower()
        lower_words = lower_phrase.split(" ")
        new_words = [word for word in lower_words if word not in self.__stopwords]
        new_phrase = ' '.join(new_words)

        return new_phrase

    def __applyStemmer(self, phrase):
        lower_phrase = phrase.lower()
        lower_words = lower_phrase.split()
        new_words = [self.__stemmer.stem(p) for p in lower_words]
        new_phrase = ' '.join(new_words)

        return new_phrase
