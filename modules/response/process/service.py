class ResponseProcessService:

    def __init__(self, response_model):
        self.__response_model = response_model

    def getResponse(self, message, emotion):
        last_emotion = self.__response_model.getLastEmotion()

        if last_emotion is not emotion:
            self.__response_model.changeEmotion(emotion)

        response = self.__response_model.getResponse(message)

        return response
