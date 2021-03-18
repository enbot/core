from helpers.http.request import Request
from helpers.http.response import Response


class PredictController:

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

            prediction = self.__predict(message)

            response = {
                "message": message,
                "prediction": prediction,
            }

            return Response.success(response)
        except ValueError:
            return Response.serverError(ValueError)

    def __predict(self, input_message):

        print('start prediction')

        training_datasets = self.__training_datasets
        training_model = self.__training_model
        training_input = self.__service.createInputMessage(input_message, training_datasets)

        test = training_model.prob_classify(training_input)

        for classe in test.samples():
            print('%s: %f' % (classe, test.prob(classe)))

        # distribuicao = training_model.prob_classify(novo)
        # for classe in distribuicao.samples():
        #     print('%s: %f' % (classe, distribuicao.prob(classe)))

        # self.__service.getEmotionPredcit(message, self.__training_model)
        return 'ss'