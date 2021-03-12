class PredictService:

    def __init__(self, test_dataset_model, train_dataset_model, emotion_model, text_model):
        self.__test_dataset_model = test_dataset_model
        self.__train_dataset_model = train_dataset_model
        self.__emotion_model = emotion_model
        self.__text_model = text_model

    def createTrainingModel(self):
        emotion_model = self.__emotion_model
        text_model = self.__text_model

        test_dataset = self.__test_dataset_model.read()
        train_dataset = self.__train_dataset_model.read()

        test_base = text_model.applyModifiers(test_dataset)
        train_base = text_model.applyModifiers(train_dataset)

        test_dataframe = emotion_model.createDataframe(test_dataset)
        train_dataframe = emotion_model.createDataframe(train_dataset)

        # print(test_dataset)
        # print(train_dataset)

        return 'soon'

    def createInputMessage(self, text):
        pass