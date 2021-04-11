from helpers.http.request import Request
from helpers.http.response import Response


class ResponseProcessController:

    def __init__(self, service):
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            emotion = body.get('message')

            if not emotion:
                return Response.badRequest('Missing param: Emotion')

            response = self.__service.getResponse(message, emotion)

            result = {
                "response": response,
            }

            return Response.success(result)
        except ValueError:
            return Response.serverError(ValueError)
