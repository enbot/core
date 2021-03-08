from modules.predict.controller import PredictController
from modules.predict.service import PredictService
from models.emotion_dictionary import EmotionDictionaryModel
from models.emotion_label import EmotionLabelModel
from helpers.http.server import Server

emotion_dictionary_model = EmotionDictionaryModel()
emotion_label_model = EmotionLabelModel()
predict_service = PredictService(emotion_dictionary_model, emotion_label_model)
predict_controller = PredictController(predict_service)

app = Server.getApp()

@app.route('/emotions', methods=['POST'])
def emotions():
    return predict_controller.handle()
