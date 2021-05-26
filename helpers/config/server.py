from flask_cors import CORS
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
            host="0.0.0.0",
            debug=False,
            port=5000,
        )

    def setupCors(self):
        CORS(self.__app, resources={r"*": {"origins": "*"}})

    def startRoutes(self):
        app = self.__app
        modules = self.__modules

        for Module in modules:
            router = Module().router()
            for index in range(len(router["routes"])):
                route = router["routes"][index]
                blueprint = Blueprint(router["module"] + str(index), __name__)
                blueprint.route(route["route"], methods=[route["method"]])(route["handler"])
                app.register_blueprint(blueprint, url_prefix="/api")
