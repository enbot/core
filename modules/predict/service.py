class PredictService:

    def __init__(self, test_dataset_model, train_dataset_model, emotion_model, text_model):
        self.__test_dataset_model = test_dataset_model
        self.__train_dataset_model = train_dataset_model
        self.__emotion_model = emotion_model
        self.__text_model = text_model

    def getTrainingModel(self):
        test_dataset_model = self.__test_dataset_model
        train_dataset_model = self.__train_dataset_model
        emotion_model = self.__emotion_model
        text_model = self.__text_model

        test_dataset = test_dataset_model.read()
        train_dataset = train_dataset_model.read()

        print(test_dataset)
        print(train_dataset)

        return '{'

    def getTextMessage(self, text):
        pass