"""
Python module to create lines plots using matplotlib as backend
"""

import matplotlib.pyplot as plt


class Plot():
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.axs = None
        self.layout = None

    def apply_layout(self):
        self.layout = [{"background_color": "#c5eff7",
                        "grid_color": '#aea8d3'}]
        self.f.patch.set_facecolor("#c5eff7")
        self.axs.set_facecolor('#aea8d3')

    def save(self, name):
        self.f.savefig(name)

    def show(self):
        self.f.show()


class Lines(Plot):
    def __init__(self):
        Plot.__init__(self)

    def plot(self, x: list, y: list, title="Some Title",
             xlabel="Some Label", ylabel="Some Label", labs="Some Label"):

        self.x = x
        self.y = y
        self.f, self.axs = plt.subplots(1, 1)
        for i in range(len(x)):
            self.axs.plot(x[i], y[i])
            self.axs.set_title(title)
            self.axs.set_xlabel(xlabel)
            self.axs.set_ylabel(ylabel)
            self.axs.legend(labs)
