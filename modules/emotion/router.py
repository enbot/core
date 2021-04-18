from modules.emotion.predict.factory import EmotionPredictFactory


class EmotionRouter:

    def __init__(self):
        self.__emotionController = EmotionPredictFactory.assemble()

    def router(self):
        return {
            "module": "emotion",
            "routes": [
                { "method" : "POST", "route" : "/emotions", "handler": self.__emotionController.handle }
            ]
        }
