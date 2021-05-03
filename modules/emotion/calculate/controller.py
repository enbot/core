from helpers.http.request import Request
from helpers.http.response import Response


class EmotionCalculateController:

    def __init__(self, service):
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            current = body.get('current')

            if not current:
                return Response.badRequest('Missing param: Current')

            new = body.get('new')

            if not new:
                return Response.badRequest('Missing param: New')

            calculation = self.__service.calculateNewCurrent(current, new)
            emotion = self.__service.getHighestSetValue(calculation)

            result = {
                "calculation": calculation,
                "emotion" : emotion
            }

            return Response.success(result)
        except:
            return Response.serverError()
