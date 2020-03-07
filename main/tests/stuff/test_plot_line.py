import pytest

import main
import main.stuff


@pytest.mark.mpl_image_compare(savefig_kwargs={'dpi': 90}, tolerance=1e-1)
def test_plot_line(mocker, fake_plot):

    # set variable
    steps = 3

    # pytest-mock must be installed for 'mocker' to be used!
    fake_fig, fake_axis = fake_plot
    mock_subplots = mocker.patch('main.stuff.plt.subplots')
    mock_subplots.return_value = (fake_fig, fake_axis)

    # without axis
    res = main.stuff.plot_line(steps, axis=None)
    assert res

    # with axis
    res = main.stuff.plot_line(steps, axis=fake_axis)
    assert res

    # important for decorator mpl_image_compare
    # test function must return a matplotlib figure object
    return fake_fig
