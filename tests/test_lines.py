"""
Tests set for lines.py
"""
from dg.lines import Lines
import numpy as np
import pytest


@pytest.fixture
def lines():
    return Lines()


@pytest.fixture(params=[0, 1])
def plot_lines(lines, request):
    if request.param == 0:
        x = []
        y = []
        title = ""
        x_label = ""
        y_label = ""
        labels = ""
        lines.plot(x=x,
                   y=y,
                   title=title,
                   xlabel=x_label,
                   ylabel=y_label,
                   labs=labels,
                   plot=True)
    else:
        x = np.arange(1, 100, 1)
        y = np.power(x, 2)
        title = "Some Title"
        x_label = "Some Values"
        y_label = "Some Values"
        labels = ["Some Label"]
        lines.plot(x=[x],
                   y=[y],
                   title=title,
                   xlabel=x_label,
                   ylabel=y_label,
                   labs=labels,
                   plot=True)
    return lines


@pytest.fixture
def multiple_lines(lines):
    x1 = np.arange(1, 100, 1)
    y1 = np.power(x1, 2)
    x2 = np.arange(1, 100, 1)
    y2 = np.power((x2 - 2), 2)
    title = "Some Title"
    x_label = "Some Values"
    y_label = "Some Values"
    labels = ["Some Label 1", "Some Label 2"]
    lines.plot(x=[x1, x2],
               y=[y1, y2],
               title=title,
               xlabel=x_label,
               ylabel=y_label,
               labs=labels,
               plot=True)
    return lines


def test_constructor(plot_lines):
    assert isinstance(plot_lines, Lines)
    assert len(plot_lines) == 2


def test_plot(plot_lines):
    assert len(plot_lines) == 2


def test_multiple_plots(multiple_lines):
    assert len(multiple_lines) == 2
