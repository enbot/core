from helpers.http.request import Request
from helpers.http.response import Response


class EmotionPredictController:

    def __init__(self, service):
        database = service.readTrainingData()
        datasets = service.createTrainingDataset(database)
        # model = service.createTrainingModel(datasets)
        self.__training_database = database
        self.__training_datasets = datasets
        # self.__training_model = model
        self.__training_model = None
        self.__service = service

    def handle(self):
        try:
            body = Request.getBody()

            if not body:
                return Response.badRequest('Missing param: JSON body')

            message = body.get('message')

            if not message:
                return Response.badRequest('Missing param: Message')

            prediction = self.__getPrediction(message)
            result = self.__getResult(prediction)

            response = {
                "message": message,
                "prediction": prediction,
                "result": result,
            }

            return Response.success(response)
        except Exception as error:
            return Response.serverError(error)

    def __getPrediction(self, message):
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

    def __getResult(self, prediction):
        result_emotion = ''
        result_percentage = 0

        for prediction_emotion in prediction:
            prediction_percentage = prediction[prediction_emotion]
            if prediction_percentage > result_percentage:
                result_emotion = prediction_emotion
                result_percentage = prediction_percentage

        return result_emotion