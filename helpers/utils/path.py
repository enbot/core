import os
import sys


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

    @staticmethod
    def read(path):
        try:
            with open(os.path.abspath(os.getcwd() + path), 'r') as file:
                print(file)
                return file.readlines()
        except IOError:
            print('IOError: system will exit now')
            sys.exit(1)
