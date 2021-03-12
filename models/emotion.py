import pandas


class EmotionModel:

    def __init__(self):
        self.__columns = ['Phrase', 'Emotion']

    def createDataframe(self, dataset):
        dataframe = pandas.DataFrame(dataset)
        dataframe.columns = self.__columns
        return dataframe