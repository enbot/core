import numpy as np


class MathModel:

    def sigmoid(self, x): 
        target = self.__digest_flost(x)
        result = np.exp(-np.logaddexp(0, -target))
        return result

    def __digest_flost(self, x):
        def check_float(y):
            try:
                float(y)

                return True
            except ValueError:
                return False

        target = float(x) if check_float(x) else 0.0

        return target
