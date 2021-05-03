from modules.emotion.calculate.controller import EmotionCalculateController
from modules.emotion.calculate.service import EmotionCalculateService


class EmotionCalculateFactory:

    @staticmethod
    def assemble():
        service = EmotionCalculateService()
        controller = EmotionCalculateController(service)
        return controller
