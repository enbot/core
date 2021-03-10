from helpers.utils.path import Path


class EmotionTestModel:
    
    def __init__(self):
        self.__dataset = Path.read('/data/emotionsDatasetForNlp/test.txt')
        print(self.__dataset)

    def read(self):
        pass
