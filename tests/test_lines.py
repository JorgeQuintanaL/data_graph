"""
Tests set for lines.py
"""
from dg.lines import Lines
import numpy as np
import pytest
import os


@pytest.fixture
def generate_x1():
    return np.arange(1, 100, 1)


@pytest.fixture
def generate_x2():
    return np.arange(1, 100, 1)


@pytest.fixture
def generate_y1(generate_x1):
    return np.power(generate_x1, 2)


@pytest.fixture
def generate_y2(generate_x2):
    return np.power((generate_x2 - 2), 2)


@pytest.fixture
def lines():
    return Lines()


@pytest.fixture(params=[0, 1])
def plot_lines(generate_x1, generate_y1, lines, request):
    if request.param == 0:
        x = np.empty([2, 2])
        y = np.empty([2, 2])
        lines.plot(x=[x],
                   y=[y])
    else:
        x = generate_x1
        y = generate_y1
        lines.plot(x=[x],
                   y=[y])
    return lines


@pytest.fixture
def multiple_lines(generate_x1, generate_x2, generate_y1, generate_y2, lines):
    x1 = generate_x1
    y1 = generate_y1
    x2 = generate_x2
    y2 = generate_y2
    labels = ["Some Label 1", "Some Label 2"]
    lines.plot(x=[x1, x2],
               y=[y1, y2],
               labs=labels)
    return lines


def test_constructor(lines):
    assert isinstance(lines, Lines)
    assert lines.x is None
    assert lines.y is None
    assert lines.f is None
    assert lines.axs is None


def test_different_types(lines):
    with pytest.raises(ValueError):
        x = ["Jorge", 2, 3]
        y = x
        lines.plot(x=[x], y=[y])


def test_plot(plot_lines):
    assert isinstance(plot_lines, Lines)
    assert plot_lines.axs.title.get_text() == "Some Title"
    assert plot_lines.axs.xaxis.label.get_text() == "Some Label"
    assert plot_lines.axs.yaxis.label.get_text() == "Some Label"
    plot_lines.show()


def test_multiple_plots(multiple_lines):
    assert isinstance(multiple_lines, Lines)
    assert multiple_lines.axs.title.get_text() == "Some Title"
    assert multiple_lines.axs.xaxis.label.get_text() == "Some Label"
    assert multiple_lines.axs.yaxis.label.get_text() == "Some Label"
    multiple_lines.show()


def test_apply_layout(plot_lines):
    plot_lines.load_template(path="./template.yml")
    plot_lines.apply_template()
    assert len(plot_lines.template) != 0
    plot_lines.show()


def test_save_images(plot_lines):
    plot_lines.save("./result_images/test_lines/test_save_images.png")
    assert os.path.isfile("./result_images/test_lines/test_save_images.png")


def test_get_data(lines, generate_x1, generate_y1):
    x = generate_x1
    y = generate_y1
    lines.plot(x=[x], y=[y])
    assert len(lines.get_data()) == len([x, y])
