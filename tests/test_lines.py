"""
Tests set for lines.py
"""
from dg.lines import Lines
import numpy as np
import pytest
import os


@pytest.fixture
def generate_x():
    return np.arange(1, 100, 1)


@pytest.fixture
def generate_y(generate_x):
    return np.power(generate_x, 2)


@pytest.fixture
def lines():
    return Lines()


@pytest.fixture(params=[0, 1])
def plot_lines(generate_x, generate_y, lines, request):
    if request.param == 0:
        x = []
        y = []
        lines.plot(x=[x],
                   y=[y],
                   plot=True)
    else:
        x = generate_x
        y = generate_y
        lines.plot(x=[x],
                   y=[y],
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


def test_constructor(lines):
    assert isinstance(lines, Lines)


def test_plot(plot_lines):
    assert isinstance(plot_lines, Lines)
    assert len(plot_lines) == 2
#    assert plot_lines.shape("x") == plot_lines.shape("y")


def test_multiple_plots(multiple_lines):
    assert isinstance(multiple_lines, Lines)
    assert len(multiple_lines) == 2
#    assert multiple_lines.shape("x") == multiple_lines.shape("y")


def test_save_images(plot_lines):
    plot_lines.save("./result_images/test_lines/test_save_images.png")
    assert os.path.isfile("./result_images/test_lines/test_save_images.png")
