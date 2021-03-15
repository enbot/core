from helpers.utils.path import Path


class DatasetModel:

    def readEmotionDataset(self, file_name, file_extension, file_dir):
        file_path = file_dir + file_name + file_extension
        file_rows = Path.read(file_path)

        dataset = []

        for row in file_rows:
            line = row.rstrip()
            items = line.split(';')
            data = tuple(items)
            dataset.append(data)  

        return dataset
