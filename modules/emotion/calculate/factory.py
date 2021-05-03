from models.math import MathModel
from modules.emotion.calculate.controller import EmotionCalculateController
from modules.emotion.calculate.service import EmotionCalculateService


class EmotionCalculateFactory:

    @staticmethod
    def assemble():
        math_model = MathModel()
        service = EmotionCalculateService(math_model)
        controller = EmotionCalculateController(service)
        return controller
