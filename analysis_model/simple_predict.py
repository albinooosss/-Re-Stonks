import matplotlib.pyplot as plt
from errors import Errors


class Simple_Predict(Errors):
    def __init__(self, data, period=1):
        prices = []
        for i in range(len(data)):
            prices.append((data[i][0] + data[i][1] + data[i][2] + data[i][3])/4)
        self.data = prices
        self.predict = []
        self.errors = []
        for i in range(period, len(self.data)):
            self.predict.append(self.data[i - period])
            self.errors.append(self.predict[-1] - self.data[i])


    def get_errors(self):
        print('AVG err of SP (%) = {}'.format(100 * sum(self.errors) / len(self.errors)))
