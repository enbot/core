from flask import Flask


class Server:

    __app = Flask(__name__)

    @staticmethod
    def getApp():
        return Server.__app

    @staticmethod
    def startApp():
        Server.__app.run(
            host="127.0.0.1",
            debug=True,
            port=5000,
        )

    @staticmethod
    def startRoutes():
        import modules.predict.route
