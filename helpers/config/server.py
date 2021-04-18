from flask import Blueprint
from flask import Flask
from modules.emotion.router import EmotionRouter
from modules.response.router import ResponseRouter


class Server:

    def __init__(self):
        self.__app = Flask(__name__)
        self.__modules = [
            EmotionRouter,
            ResponseRouter,
        ]

    def startApp(self):
        self.__app.run(
            host="127.0.0.1",
            debug=True,
            port=5000,
        )

    def startRoutes(self):
        app = self.__app
        modules = self.__modules

        for Module in modules:
            router = Module().router()
            blueprint = Blueprint(router["module"], __name__)

            for route in router["routes"]:
                blueprint.route(route["route"], methods=[route["method"]])(route["handler"])

            app.register_blueprint(blueprint, url_prefix='/api')
