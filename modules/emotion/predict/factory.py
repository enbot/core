from models.emotion import EmotionModel
from models.dataset import DatasetModel
from models.text import TextModel
from modules.emotion.predict.controller import EmotionPredictController
from modules.emotion.predict.service import EmotionPredictService


class EmotionPredictFactory:

    @staticmethod
    def assemble():
        dataset_model = DatasetModel()
        emotion_model = EmotionModel()
        text_model = TextModel()
        service = EmotionPredictService(dataset_model, emotion_model, text_model)
        controller = EmotionPredictController(service)
        return controller
