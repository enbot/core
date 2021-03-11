from helpers.utils.path import Path


class DatasetModel:

    def __init__(self, file_name, file_extension):
        self.__file_dir = '/data/emotionsDatasetForNlp/'
        self.__file_name = file_name
        self.__file_extension = file_extension

    def read(self):
        file_dir = self.__file_dir
        file_name = self.__file_name
        file_extension = self.__file_extension
        file_path = file_dir + file_name + file_extension
        file_rows = Path.read(file_path)

        dataset = []

        for row in file_rows:
            line = row.rstrip()
            items = line.split(';')
            data = tuple(items)
            dataset.append(data)  

        return dataset
