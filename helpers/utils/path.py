import os


class Path:

    @staticmethod
    def exists(path):
        return os.path.isfile(path)

    @staticmethod
    def aboslute(path):
        return os.path.abspath(path)

    @staticmethod
    def create(path):
        os.makedirs(path)
