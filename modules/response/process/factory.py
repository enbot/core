from models.response import ResponseModel
from modules.response.process.controller import ResponseProcessController
from modules.response.process.service import ResponseProcessService


class ResponseProcessFactory:

    @staticmethod
    def assemble():
        response_model = ResponseModel()
        service = ResponseProcessService(response_model)
        controller = ResponseProcessController(service)
        return controller
