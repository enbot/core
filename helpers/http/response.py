from flask import render_template
from flask import jsonify


class Response:

    @staticmethod
    def success(data):
        return jsonify(
            {
                'status': 200,
                'data': data
            }
        )

    @staticmethod
    def serverError(error):
        return jsonify(
            {
                'status': 500,
                'error': error
            }
        )

    @staticmethod
    def badRequest(error):
        return jsonify(
            {
                'status': 400,
                'error': error
            }
        )
