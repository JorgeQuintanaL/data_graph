"""
Python module to create lines plots using matplotlib as backend
"""

import matplotlib.pyplot as plt


class Lines():
    def __init__(self):
        self._data = []

    def plot(self, x: list, y: list, title: str, xlabel: str,
             ylabel: str, labs: str, plot: bool):
        self._data = [x, y]
        for i in range(len(x)):
            plt.plot(x[i], y[i])
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
        plt.legend(labs)
        if plot:
            plt.show()

    def __len__(self):
        return len(self._data)

    def save(self, name):
        plt.savefig(name)
