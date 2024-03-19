import matplotlib.pyplot as plt
from math import *
from simple_predict import Simple_Predict
from errors import Errors


class AdaptiveFilter(Errors):

    next_day = []
    next_week = []
    next_month = []
    next_6_months = []
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
        AdaptiveFilter.next_day = ([[1] * self.N] * self.N)
        AdaptiveFilter.next_week = ([[1] * self.N] * self.N)
        AdaptiveFilter.next_month = ([[1] * self.N] * self.N)
        AdaptiveFilter.next_6_months = ([[1] * self.N] * self.N)

    def adjustment(self, period=1):
        self.predict = [-1, -1]
        for i in range(2 * period, len(self.data)):
            a = round((self.data[i - period] - self.m) / self.step)
            b = round((self.data[i - 2 * period] - self.m) / self.step)
            next = self.data[i - period] + (self.data[i - period] - self.data[i - 2 * period])
            if period == 1:
                next *= AdaptiveFilter.next_day[a][b]
            elif period == 5:
                next *= AdaptiveFilter.next_week[a][b]
            elif period == 21:
                next *= AdaptiveFilter.next_month[a][b]
            else:
                next *= AdaptiveFilter.next_6_months[a][b]
            self.predict.append(next)
            err = self.data[i] - next
            delta = err / (self.data[i - period])
            self.errors.append(self.predict[-1] - self.data[i])
            if period == 1:
                AdaptiveFilter.next_day[a][b] += delta
            elif period == 5:
                AdaptiveFilter.next_week[a][b] += delta
            elif period == 21:
                AdaptiveFilter.next_month[a][b] += delta
            else:
                AdaptiveFilter.next_6_months[a][b] += delta


    def apply(self, p1, p2):
        a = round((p2 - self.m) / self.step)
        b = round((p1 - self.m) / self.step)
        return p1 + (p1 - p2) * AdaptiveFilter.next_day[a][b]

    def show_err_plot(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y = self.errors
        plt.plot(x, y)
        plt.show()


    def get_pr_err(self):
        print('AVG err of AF(%) = {}'.format(100 * sum(self.pr_err) / len(self.pr_err)))