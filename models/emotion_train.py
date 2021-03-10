from helpers.utils.path import Path


class EmotionTrainModel:
    
    def __init__(self):
        self.__dataset = Path.read('/data/emotionsDatasetForNlp/train.txt')
        print(self.__dataset)

    def read(self):
        pass
