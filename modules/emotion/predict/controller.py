from helpers.http.request import Request
from helpers.http.response import Response


class PredictController:

    def __init__(self, service):
        datasets = service.readTrainingData()
        model = service.createTrainingModel(datasets)
        self.__training_datasets = datasets
        self.__training_model = model
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            return Response.success({"input": message})
        except ValueError:
            return Response.serverError(ValueError)
