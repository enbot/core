from helpers.http.request import Request
from helpers.http.response import Response


class PredictController:

    def __init__(self, service):
        self.__service = service
        self.__training_model = service.createTrainingModel()

        # teste1 = EmotionTestModel()
        # teste2 = EmotionTrainModel()

    def handle(self):
        try:
            body = Request.getBody()
            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            return Response.success({"input": message})
        except ValueError:
            return Response.serverError(ValueError)
