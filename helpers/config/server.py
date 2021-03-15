from flask import Flask
from modules.emotion.router import EmotionRouter


class Server:

    def __init__(self):
        self.__app = Flask(__name__)
        self.__routes = [
            EmotionRouter,
        ]

    def startApp(self):
        self.__app.run(
            host="127.0.0.1",
            debug=True,
            port=5000,
        )

    def startRoutes(self):
        app = self.__app
        routes = self.__routes

        for Module in routes:
            Module().route(app)

