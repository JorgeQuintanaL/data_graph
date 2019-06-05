"""
Python module to create lines plots using matplotlib as backend
"""

import matplotlib.pyplot as plt


class Lines():
    def __init__(self, x: list, y: list):
        self._data = [x, y]
        self.x = x
        self.y = y

    def plot(self, title: str, xlabel: str,  ylabel: str, labels: str):
        for i in range(len(self.x)):
            plt.plot(self.x[i], self.y[i])
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
        plt.legend(labels)
        plt.show()

    def __len__(self):
        return len(self._data)
