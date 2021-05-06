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
        print('path')
        print(path)
        print(Path.resource(path))
        try:
            with open(Path.resource(path), 'r') as file:
                return file.readlines()
        except IOError:
            print('IOError: system will exit now')
            sys.exit(1)

    @staticmethod
    def resource(path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, path)
        return os.path.join(os.path.abspath("."), path)
