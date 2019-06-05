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
import pytest


@pytest.fixture
def lines():
    return Lines()


def test_constructor(lines):
    assert isinstance(lines, Lines)
    assert len(lines) == 0


def test_plot(lines):
    x1 = np.arange(1, 100, 1)
    y1 = np.power(x1, 2)
    title = "Some Title"
    x_label = "Some Values"
    y_label = "Some Values"
    labels = "Some Label"
    x = [x1]
    y = [y1]
    lines.plot(x=x,
               y=y,
               title=title,
               xlabel=x_label,
               ylabel=y_label,
               labs=labels)
    assert len([x, y]) == len(lines)
