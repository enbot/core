from flask import request


class Request:

    @staticmethod
    def getBody():
        return request.get_json()
