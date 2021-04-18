class EmotionPredictService:

    def __init__(self, dataset_model, emotion_model, text_model):
        self.__dataset_model = dataset_model
        self.__emotion_model = emotion_model
        self.__text_model = text_model

    def readTrainingData(self):
        file_dir = '/data/emotionsDatasetForNlp/'
        test_file_name = 'test'
        train_file_name = 'train'
        file_extension = '.txt'

        train_dataset = self.__dataset_model.readEmotionDataset(train_file_name, file_extension, file_dir) 
        test_dataset = self.__dataset_model.readEmotionDataset(test_file_name, file_extension, file_dir)

        return {
            "train": train_dataset,
            "test": test_dataset,
        }

    def createTrainingDataset(self, database):
        train_database = database["train"]
        test_database = database["test"][20:]
        # train_database = database["train"][:100]
        # test_database = database["test"][:20]

        train_base = self.__text_model.applyDatasetModifiers(train_database)
        test_base = self.__text_model.applyDatasetModifiers(test_database)

        train_unique_words = self.__text_model.getDatasetUniqueWords(train_base)
        test_unique_words = self.__text_model.getDatasetUniqueWords(test_base)

        complete_train_dataset = self.__emotion_model.createTrainingDataset(train_base, train_unique_words)
        complete_test_dataset = self.__emotion_model.createTrainingDataset(test_base, test_unique_words)

        return {
            "train": complete_train_dataset,
            "test": complete_test_dataset,
            "words": train_unique_words,
        }

    def createTrainingModel(self, datasets):
        train_dataset = datasets["train"]
        test_dataset = datasets["test"]

        training_model = self.__emotion_model.createTrainingModel(train_dataset, test_dataset)

        return training_model

    def createInputMessage(self, input_message, datasets):
        train_dataset = datasets["words"]

        train_message = self.__text_model.applyTextModifiers(input_message)
        train_input = self.__emotion_model.createTrainingInput(train_message, train_dataset)

        return train_input