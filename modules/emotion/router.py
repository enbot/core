from modules.emotion.calculate.factory import EmotionCalculateFactory
from modules.emotion.predict.factory import EmotionPredictFactory


class EmotionRouter:

    def __init__(self):
        self.__emotionCalculateFactory = EmotionCalculateFactory.assemble()
        self.__emotionPredictController = EmotionPredictFactory.assemble()

    def router(self):
        return {
            "module": "emotion",
            "routes": [
                { "method" : "POST", "route" : "/emotion/calculate", "handler": self.__emotionCalculateFactory.handle },
                { "method" : "POST", "route" : "/emotion/predict", "handler": self.__emotionPredictController.handle },
            ]
        }
