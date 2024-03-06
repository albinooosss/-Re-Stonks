import matplotlib.pyplot as plt


class AdaptiveFilter():
    def __init__(self, data, N):
        #пока что считаем что data - это список из 5 списков: максимальные цены, минимальные цены,
        #цены открытия, цены закрытия, объем сделок
        self.N = N
        self.errors = []
        prices = []
        for i in range(len(data[0])):
            prices.append((data[0][i] + data[1][i] + data[2][i] + data[3][i])/4)
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
            delta = err / (self.data[i - 1] - self.data[i - 2])
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
