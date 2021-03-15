from models.emotion import EmotionModel
from models.dataset import DatasetModel
from models.text import TextModel
from modules.emotion.predict.controller import PredictController
from modules.emotion.predict.service import PredictService


class EmotionPredictFactory:

    @staticmethod
    def assemble():
        dataset_model = DatasetModel()
        emotion_model = EmotionModel()
        text_model = TextModel()
        service = PredictService(dataset_model, emotion_model, text_model)
        controller = PredictController(service)
        return controller
