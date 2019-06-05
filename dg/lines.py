"""
Python module to create lines plots using matplotlib as backend
"""

import matplotlib.pyplot as plt


class Lines():
    def __init__(self):
        self._data = []

    def plot(self, x: list, y: list, plot: bool, title="Some Title",
             xlabel=["Some Label"], ylabel="Some Label", labs="Some Label"):
        if len(x) == len(y):
            self._data = [x, y]
            for i in range(len(x)):
                plt.plot(x[i], y[i])
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
            plt.legend(labs)
            if plot:
                plt.show()
        else:
            return "Series sizes should match!: \
                    x is {} and y is {}".format(len(x), len(y))

    def __len__(self):
        return len(self._data)

    def save(self, name):
        plt.savefig(name)
