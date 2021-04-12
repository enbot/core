import aiml


class ResponseModel:

    def __init__(self):
        self.__last_emotion = None
        self.__kernel = aiml.Kernel()
        self.__kernel.bootstrap(learnFiles=['aiml/start.xml'], commands=['load aiml b'])

    def getLastEmotion(self):
        return self.__last_emotion

    def changeEmotion(self, emotion):
        # self.__kernel.respond()
        pass

    def getResponse(self, message):
        self.__kernel.respond(message)
