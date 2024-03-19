import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Errors(ABC):
    @abstractmethod
    def __init__(self):
        self.errors = None
        self.data = None
        self.predict = None

    def MSE(self):
        return sum([i**2 for i in self.errors]) / len(self.errors)

    def RMSE(self):
        return math.sqrt(self.MSE())

    def MSPE(self):
        s = 0
        start = len(self.data) - len(self.errors)
        for i in range(len(self.errors)):
            s += (self.errors[i] / self.data[start + i]) ** 2
        return 100 / len(self.errors) * s

    def MAE(self):
        return sum([abs(i) for i in self.errors]) / len(self.errors)

    def MAPE(self):
        s = 0
        start = len(self.data) - len(self.errors)
        for i in range(len(self.errors)):
            s += (abs(self.errors[i]) / self.data[start + i])
        return 100 / len(self.errors) * s

    def MRE(self):
        return self.MAPE() / 100

    def show_plots(self):
        sp = len(self.predict) - len(self.errors)
        sd = len(self.data) - len(self.errors)
        x = [(i + 1) for i in range(len(self.errors))]
        y1 = self.predict[sp:]
        y2 = self.data[sd:]
        y3 = self.errors

        plt.plot(x, y1, 'b', x, y2, 'g', x, y3, 'r')
        plt.show()