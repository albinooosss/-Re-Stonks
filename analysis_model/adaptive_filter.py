import matplotlib.pyplot as plt
from math import *
from simple_predict import Simple_Predict
from errors import Errors


class AdaptiveFilter(Errors):

    w = []
    def __init__(self, data, N=None):
        self.N = N
        self.errors = []
        self.pr_err = []
        prices = []
        for i in range(len(data)):
            prices.append((data[i][0] + data[i][1] + data[i][2] + data[i][3])/4)
        self.data = prices
        self.step = (max(self.data) - min(self.data)) // (self.N - 1) + 1
        self.m = min(self.data)
        AdaptiveFilter.w = ([[1] * self.N] * self.N)

    def adjustment(self):
        self.predict = [-1, -1]
        for i in range(2, len(self.data) - 1):
            a = round((self.data[i - 2] - self.m) / self.step)
            b = round((self.data[i - 1] - self.m) / self.step)
            if a >= self.N or b >= self.N:
                print(a, b)
            next = self.data[i - 1] + (self.data[i - 1] - self.data[i - 2]) * AdaptiveFilter.w[a][b]
            self.predict.append(next)
            err = self.data[i] - next
            delta = err / (self.data[i - 1]) if self.data[i - 1] != self.data[i - 2] else 0
            self.errors.append(self.predict[-1] - self.data[i + 1])
            self.pr_err.append(abs(1 - next / self.data[i]))
            AdaptiveFilter.w[a][b] += delta

    def apply(self, p1, p2):
        a = (round(p2) - self.m) / self.step
        b = (round(p1) - self.m) / self.step
        return p1 + (p1 - p2) * AdaptiveFilter.w[a][b]

    def show_err_plot(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y = self.errors
        plt.plot(x, y)
        plt.show()


    def get_pr_err(self):
        print('AVG err of AF(%) = {}'.format(100 * sum(self.pr_err) / len(self.pr_err)))