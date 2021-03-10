class PredictService:

    def __init__(self, emotion_test_model, emotion_train_model):
        self.__emotion_test_model = emotion_test_model
        self.__emotion_train_model = emotion_train_model

    def readTrainingData(self):
        return {
            'test': self.__emotion_test_model.read(),
            'train': self.__emotion_train_model.read(),
        }

    def serializeTrainingData(self, trainingData):
        pass

    def getTrainingModel(self):
        pass
