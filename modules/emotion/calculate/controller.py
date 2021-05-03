from helpers.http.request import Request
from helpers.http.response import Response


class EmotionCalculateController:

    def __init__(self, service):
        pass

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            current = body.get('current')

            if not current:
                return Response.badRequest('Missing param: Current')

            classification = body.get('classification')

            if not classification:
                return Response.badRequest('Missing param: Classification')

            amount = body.get('amount')

            if not amount:
                return Response.badRequest('Missing param: Amount')

            result = {
                "current": current,
                "classification": classification,
                "amount": amount,
            }

            return Response.success('response')
        except:
            return Response.serverError()
