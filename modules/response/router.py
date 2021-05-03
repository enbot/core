from modules.response.process.factory import ResponseProcessFactory


class ResponseRouter:

    def __init__(self):
        self.__responseProcessController = ResponseProcessFactory.assemble()

    def router(self):
        return {
            "module": "response",
            "routes": [
                { "method" : "POST", "route" : "/response/process", "handler": self.__responseProcessController.handle },
            ]
        }
