from modules.emotion.predict.factory import EmotionPredictFactory


class EmotionRouter:

    def __init__(self):
        self.__emotionController = EmotionPredictFactory.assemble()

    def route(self, app):
        app.route('/api/emotions', methods=['POST'])(self.__emotionController.handle)
