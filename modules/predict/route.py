from helpers.http.server import Server
from modules.predict.controller import PredictController
from modules.predict.service import PredictService
from models.emotion_test import EmotionTestModel
from models.emotion_train import EmotionTrainModel

emotion_test_model = EmotionTestModel()
emotion_train_model = EmotionTrainModel()

predict_service = PredictService(emotion_test_model, emotion_train_model)
predict_controller = PredictController(predict_service)

app = Server.getApp()

@app.route('/emotions', methods=['POST'])
def emotions():
    return predict_controller.handle()
