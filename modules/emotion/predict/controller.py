from helpers.http.request import Request
from helpers.http.response import Response


class EmotionPredictController:

    def __init__(self, service):
        database = service.readTrainingData()
        datasets = service.createTrainingDataset(database)
        model = service.createTrainingModel(datasets)
        self.__training_database = database
        self.__training_datasets = datasets
        self.__training_model = model
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            categorization = self.__getCategorization(message)
            classification = self.__getClassification(categorization)

            response = {
                "categorization": categorization,
                "classification": classification,
            }

            return Response.success(response)
        except:
            return Response.serverError()

    def __getCategorization(self, message):
        training_datasets = self.__training_datasets
        training_model = self.__training_model
        training_input = self.__service.createInputMessage(message, training_datasets)
        training_result = training_model.prob_classify(training_input)
        available_emotions = training_result.samples()

        predictions = {}

        for emotion in available_emotions:
            emotion_probability = training_result.prob(emotion)
            emotion_rounded = float("{:.2f}".format(emotion_probability))
            predictions[emotion] = emotion_rounded

        return predictions

    def __getClassification(self, categorization):
        return {
            "neutral" : categorization["surprise"] + categorization["fear"],
            "positive" : categorization["joy"] + categorization["love"],
            "negative" : categorization["anger"] + categorization["sadness"],
        }
