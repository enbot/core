from helpers.http.request import Request
from helpers.http.response import Response


class PredictController:

    def __init__(self, service):
        trainingData = service.readTrainingData()
        serializedData = service.serializeTrainingData(trainingData)

        self.__service = service
        self.__dataset = serializedData

    def handle(self):
        try:
            body = Request.getBody()
            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            print(message)

            return Response.success({"input": message})
        except ValueError:
            return Response.serverError(ValueError)
