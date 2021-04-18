class ResponseProcessService:

    def __init__(self, response_model):
        self.__response_model = response_model

    def getResponse(self, message, emotion):
        current_emotion = self.__response_model.getCurrentEmotion()

        if current_emotion is not emotion:
            self.__response_model.changeEmotion(emotion)

        response = self.__response_model.getResponse(message)

        return response
