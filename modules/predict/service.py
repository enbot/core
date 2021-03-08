class PredictService:

    def __init__(self, emotion_dictionary_model, emotion_label_model):
        self.__emotion_dictionary_model = emotion_dictionary_model
        self.__emotion_label_model = emotion_label_model

    def readTrainingData(self):
        return {
            'dictionaries': self.__emotion_dictionary_model.read(),
            'labels': self.__emotion_label_model.read()
        }

    def serializeTrainingData(self, trainingData):
        pass

    def getTrainingModel(self):
        pass


# readModelData
# serializeModelData
# serializeModelTensors
# getTrainingModel