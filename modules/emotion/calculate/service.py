class EmotionCalculateService:

    def __init__(self, math_model):
        self.__math_model = math_model

    def calculateNewCurrent(self, current, new):
        new_highest_emotion = self.getHighestSetValue(new)
        current_highest_emotion = self.getHighestSetValue(current)

        new_highest_emotion_name = new_highest_emotion["name"]
        new_highest_emotion_amount = new_highest_emotion["amount"]
        current_highest_emotion_name = current_highest_emotion["name"]

        new_highest_emotion_amount_sigmoid = self.__math_model.sigmoid(new_highest_emotion_amount)

        for new_emotion_name in new:
            for current_emotion_name in current:
                if new_emotion_name is current_emotion_name:
                    new_emotion_amount_sigmoid = self.__math_model.sigmoid(new[new_emotion_name])
                    if not current_highest_emotion_name and new_emotion_name is new_highest_emotion_name:
                        current[new_emotion_name] += new_emotion_amount_sigmoid * 1.2
                    elif new_emotion_name is current_highest_emotion_name and new_emotion_name is new_highest_emotion_name:
                        current[new_emotion_name] += new_emotion_amount_sigmoid * 2
                    elif new_emotion_name is current_highest_emotion_name and new_emotion_name is not new_highest_emotion_name:
                        current[new_emotion_name] -= new_emotion_amount_sigmoid * 0.6
                    elif new_emotion_name is not current_highest_emotion_name and new_emotion_name is new_highest_emotion_name:
                        current[new_emotion_name] += new_emotion_amount_sigmoid * 0.6
                    elif new[new_emotion_name] != 0:
                        current[new_emotion_name] -= new_highest_emotion_amount_sigmoid - new_emotion_amount_sigmoid
                    else:
                        current[new_emotion_name] -= new_emotion_amount_sigmoid

        return current

    def getHighestSetValue(self, key_value_set):
        all_are_same = len(list(set(list(key_value_set.values())))) == 1
        value_key_set = {v: k for k, v in key_value_set.items()}

        name = value_key_set.get(max(value_key_set))
        amount = max(value_key_set)

        if all_are_same:
            name = None

        return {
            "name": name,
            "amount": amount,
        }
