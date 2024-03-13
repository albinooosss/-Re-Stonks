import matplotlib.pyplot as plt


class Simple_Predict:
    def __init__(self, data):
        prices = []
        for i in range(len(data)):
            prices.append((data[i][0] + data[i][1] + data[i][2] + data[i][3])/4)
        self.data = prices
        self.predicts = []
        self.errors = []
        for i in range(1, len(self.data) - 1):
            self.predicts.append(self.data[i])
            self.errors.append(abs(1 - self.predicts[-1] / self.data[i + 1]))

    def show_plots(self):
        x = [(i + 1) for i in range(len(self.errors))]
        y1 = self.predicts
        y2 = self.data[2:]
        plt.plot(x, y1, 'b', x, y2, 'r-')
        plt.show()

    def get_errors(self):
        print('AVG err of SP (%) = {}'.format(sum(self.errors) / len(self.errors)))
