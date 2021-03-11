from helpers.http.server import Server
from models.emotion import EmotionModel
from models.dataset import DatasetModel
from models.text import TextModel
from modules.predict.controller import PredictController
from modules.predict.service import PredictService

test_dataset_model = DatasetModel('test', 'txt')
train_dataset_model = DatasetModel('train', 'txt')

emotion_model = EmotionModel()
text_model = TextModel()

predict_service = PredictService(test_dataset_model, train_dataset_model, emotion_model, text_model)

predict_controller = PredictController(predict_service)

app = Server.getApp()

@app.route('/emotions', methods=['POST'])
def emotions():
    return predict_controller.handle()
