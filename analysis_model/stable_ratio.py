from errors import Errors
import matplotlib.pyplot as plt


class Stable_Ratio(Errors):
    def __init__(self, data):
        prices = []
        for i in range(len(data)):
            prices.append((data[i][0] + data[i][1] + data[i][2] + data[i][3])/4)
        self.data = prices
        self.predict = []
        self.errors = []
        for i in range(2, len(self.data) - 1):
            self.predict.append(2 * self.data[i-1] - self.data[i-2])
            self.errors.append(self.predict[-1] - self.data[i + 1])

    def get_errors(self):
        print('AVG err of SP (%) = {}'.format(100 * sum(self.errors) / len(self.errors)))