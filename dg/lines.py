"""
Python module to create lines plots using matplotlib as backend
"""

import matplotlib.pyplot as plt
import yaml


class Plot():
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.axs = None
        self.template = None

    def load_template(self, path):
        with open(path, 'r') as f:
            self.template = yaml.load(f, Loader=yaml.FullLoader)

    def apply_template(self):
        self.f.patch.set_facecolor(self.template["background-color"]["figure-background"])
        self.axs.set_facecolor(self.template["background-color"]["grid_background"])

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
