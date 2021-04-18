from flask import render_template
from flask import jsonify


class Response:

    @staticmethod
    def success(data):
        return jsonify(
            {
                'success': True,
                'data': data
            }
        ) , 200

    @staticmethod
    def serverError(error):
        return jsonify(
            {
                'success': False,
                'errors': [
                    error
                ]
            }
        ) , 500

    @staticmethod
    def badRequest(error):
        return jsonify(
            {
                'success': False,
                'errors': [
                    error
                ]
            }
        ) , 400
