# import pandas
import nltk


class EmotionModel:

    def __init__(self):
        self.__columns = ['Phrase', 'Emotion']
        self.__unique_words = []

    # def createDataframe(self, dataset):
    #     dataframe = pandas.DataFrame(dataset)
    #     dataframe.columns = self.__columns
    #     return dataframe

    def getTrainingDataset(self, emotion_base, unique_words):

        def findFeatures(document):
            words_set = set(document)
            features_set = {}
            for word in unique_words:
                features_set[word] = (word in words_set)
            return features_set

        training_dataset = nltk.classify.apply_features(findFeatures, emotion_base)

        return training_dataset
