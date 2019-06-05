"""
Tests set for lines.py

lines1 = lines(x = x, y = y)
lines1.plot(title = "Prueba",
            xlabel = "Some Numbers",
            ylabel = "Some Numbers",
            labels = labels)
"""
from dg.lines import Lines
import numpy as np


class TestLines():

    def test_constructor(self):
        x1 = np.arange(1, 100, 1)
        y1 = np.power(x1, 2)
        x = [x1]
        y = [y1]
        l1 = Lines(x=x, y=y)
        assert isinstance(l1, Lines)
        assert len([x, y]) == len(l1)
