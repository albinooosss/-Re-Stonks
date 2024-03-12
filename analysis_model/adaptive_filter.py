import matplotlib.pyplot as plt


class AdaptiveFilter():
    def __init__(self, data, N):
        #пока что считаем что data - это список из 5 списков: максимальные цены, минимальные цены,
        #цены открытия, цены закрытия, объем сделок
        self.N = N
        self.errors = []
        prices = []
        for i in range(len(data)):
            prices.append((data[i][0] + data[i][1] + data[i][2] + data[i][3])/4)
        self.data = prices
        self.step = (max(self.data) - min(self.data)) // N + 1
        self.m = min(self.data)
        self.w = [[1] * N] * N

    def adjustment(self):
        self.predict = [-1, -1]
        for i in range(2, len(self.data)):
            a = round((self.data[i - 2] - self.m) / self.step)
            b = round((self.data[i - 1] - self.m) / self.step)
            next = self.data[i - 1] + (self.data[i - 1] - self.data[i - 2]) * self.w[a][b]
            self.predict.append(next)
            err = self.data[i] - next
            delta = err / (self.data[i - 1] - self.data[i - 2]) if self.data[i - 1] != self.data[i - 2] else 0
            self.errors.append(abs(err / self.data[i]))
            self.w[a][b] += delta

    def apply(self, p1, p2):
        a = (round(p2) - self.m) / self.step
        b = (round(p1) - self.m) / self.step
        return p1 + (p1 - p2) * self.w[a][b]

    def show_err_plot(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y = self.errors
        plt.plot(x, y)
        plt.show()

    def show_plots(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y1 = self.predict[2:]
        y2 = self.data[2:]
        plt.plot(x, y1, 'b', x, y2, 'r-')
        plt.show()
