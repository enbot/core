class PredictService:

    def __init__(self, dataset_model, emotion_model, text_model):
        self.__dataset_model = dataset_model
        self.__emotion_model = emotion_model
        self.__text_model = text_model

    def readTrainingData(self):
        file_dir = '/data/emotionsDatasetForNlp/'
        test_file_nasme = 'test'
        train_file_nasme = 'train'
        file_extension = '.txt'

        test_dataset = self.__dataset_model.readEmotionDataset(test_file_nasme, file_extension, file_dir)
        train_dataset = self.__dataset_model.readEmotionDataset(train_file_nasme, file_extension, file_dir) 

        return {
            "test": test_dataset,
            "train": train_dataset,
        }

    def createTrainingModel(self, datasets):
        train_dataset = datasets["train"]
        test_dataset = datasets["test"]

        train_base = self.__text_model.applyModifiers(train_dataset)
        test_base = self.__text_model.applyModifiers(test_dataset)

        train_unique_words = self.__text_model.getUniqueWords(train_base)
        test_unique_words = self.__text_model.getUniqueWords(test_base)

        complete_train_dataset = self.__emotion_model.getTrainingDataset(train_base, train_unique_words)
        complete_test_dataset = self.__emotion_model.getTrainingDataset(test_base, test_unique_words)

        # train_dataframe = self.__emotion_model.createDataframe(train_base)
        # test_dataframe = self.__emotion_model.createDataframe(test_base)

        # print(train_unique_words)
        # print(test_base)
        # print(train_base)

        # print(train_unique_words)
        # print(test_unique_words)

        print("soon")

        return 'soon'

    def createInputMessage(self, text):
        pass
