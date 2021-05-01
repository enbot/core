import aiml


class ResponseModel:

    def __init__(self):
        self.__current_emotion = None
        self.__kernel = aiml.Kernel()
        self.__kernel.bootstrap(learnFiles=['aiml/start.xml'], commands=['load aiml b'])

    def getCurrentEmotion(self):
        return self.__current_emotion

    def changeEmotion(self, emotion):
        self.__kernel.respond('turn your emotion into {}'.format(emotion))
        self.__current_emotion = emotion

    def getResponse(self, message):
        return self.__kernel.respond(message)
