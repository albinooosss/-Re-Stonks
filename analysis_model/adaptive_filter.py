import matplotlib.pyplot as plt
from math import *
from simple_predict import Simple_Predict

class AdaptiveFilter():

    w = []
    def __init__(self, data, N=None):
        #пока что считаем что data - это список из 5 списков: максимальные цены, минимальные цены,
        #цены открытия, цены закрытия, объем сделок
        s = Simple_Predict(data)
        self.s_pr = s.predicts


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
        for i in range(2, len(self.data)):
            a = round((self.data[i - 2] - self.m) / self.step)
            b = round((self.data[i - 1] - self.m) / self.step)
            if a >= self.N or b >= self.N:
                print(a, b)
            next = self.data[i - 1] + (self.data[i - 1] - self.data[i - 2]) * AdaptiveFilter.w[a][b]
            self.predict.append(next)
            err = self.data[i] - next
            delta = err / (self.data[i - 1]) if self.data[i - 1] != self.data[i - 2] else 0
            self.errors.append(abs(err / self.data[i]))
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

    def show_plots(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y1 = self.predict[2:]
        y2 = self.data[2:]

        y3 = self.s_pr

        plt.plot(x, y1, 'b', x, y2, 'r-', x, y3, 'g')
        plt.show()

    def get_pr_err(self):
        print('AVG err of AF(%) = {}'.format(sum(self.pr_err) / len(self.pr_err)))