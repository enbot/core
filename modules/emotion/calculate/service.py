class EmotionCalculateService:

    def __init__(self, math_model):
        self.__math_model = math_model

    def calculateNewCurrent(self, current, new):
        highest_emotion = self.getHighestSetValue(new)
        highest_emotion_name = highest_emotion["name"]
        highest_emotion_amount = highest_emotion["amount"]
        highest_emotion_amount_sigmoid = self.__math_model.sigmoid(highest_emotion_amount)

        for new_emotion_name in new:
            for current_emotion_name in current:
                if new_emotion_name is current_emotion_name:
                    current_emotion_amount_sigmoid = self.__math_model.sigmoid(new[new_emotion_name])
                    if new_emotion_name is highest_emotion_name:
                        current[new_emotion_name] += current_emotion_amount_sigmoid
                    else:
                        current[new_emotion_name] -= highest_emotion_amount_sigmoid - current_emotion_amount_sigmoid

        return current

    def getHighestSetValue(self, key_value_set):
        value_key_set = {v: k for k, v in key_value_set.items()}

        name = value_key_set.get(max(value_key_set))
        amount = max(value_key_set)

        return {
            "name": name,
            "amount": amount,
        }
