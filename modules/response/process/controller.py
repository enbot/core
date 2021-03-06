from helpers.http.request import Request
from helpers.http.response import Response


class ResponseProcessController:

    def __init__(self, service):
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: body')

            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: message')

            emotion = body.get('emotion')

            if not emotion:
                return Response.badRequest('Missing param: emotion')

            response = self.__service.getResponse(message, emotion)

            result = {
                "response": response,
            }

            return Response.success(result)
        except:
            return Response.serverError()
