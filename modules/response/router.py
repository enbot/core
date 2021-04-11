from modules.response.process.factory import ResponseProcessFactory


class ResponseRouter:

    def __init__(self):
        self.__responseProcessController = ResponseProcessFactory.assemble()

    def route(self, app):
        app.route('/api/response', methods=['POST'])(self.__responseProcessController.handle)
