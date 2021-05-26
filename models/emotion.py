import nltk
from nltk.classify.util import accuracy


class EmotionModel:

    def createTrainingDataset(self, emotion_base, unique_words):
        training_base = [(phrase.split(" "), emotion) for (phrase, emotion) in emotion_base]
        find_features_function = self.__getFindFeaturesFunction(unique_words)
        training_dataset = nltk.classify.apply_features(find_features_function, training_base)
        return training_dataset

    def createTrainingInput(self, input_phrase, unique_words):
        input_words = input_phrase.split(" ")
        find_features_function = self.__getFindFeaturesFunction(unique_words)
        training_input = find_features_function(input_words)
        return training_input

    def createTrainingModel(self, complete_train_dataset):
        training_model = nltk.NaiveBayesClassifier.train(complete_train_dataset)
        print(training_model.show_most_informative_features(40))
        return training_model

    def __getFindFeaturesFunction(self, unique_words):
        def findFeatures(document):
            words_set = set(document)
            features_set = {}
            for word in unique_words:
                features_set[word] = (word in words_set)
            return features_set

        return findFeatures
