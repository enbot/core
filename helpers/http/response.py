from flask import jsonify


class Response:

    @staticmethod
    def success(data):
        return jsonify(
            {
                'success': True,
                'data': data
            }
        ), 200

    @staticmethod
    def serverError():
        return jsonify(
            {
                'success': False,
                'errors': [
                    'Internal server error'
                ]
            }
        ), 500

    @staticmethod
    def badRequest(error):
        return jsonify(
            {
                'success': False,
                'errors': [
                    error
                ]
            }
        ), 400
