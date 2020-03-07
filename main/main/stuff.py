"""Define stuff functions."""

# %%########################################################################### import modules

import warnings

import matplotlib.pyplot as plt

import sub
import sub.array

# %%########################################################################### define functions


def say_hello(txt):
    """Say hello (for unit testing).

    Parameters
    ----------
    txt : string
        input string

    Returns
    -------
    txt : string
        output string

    Examples
    --------
    # This first example is tested during doctests.
    # Use empty lines to separate examples.
    >>> txt = 'blu'
    >>> print(say_hello(txt) == txt)
    Hello blu
    True

    # This second example is displayed in docstring but not tested
    # (and would fail because 'Hello bla' != 'Hello nope').
    # https://stackoverflow.com/a/55002297/5350621
    >>>
    >> txt = 'bla'
    >> print(say_hello(txt) == txt)
    Hello nope
    True
    """
    print('Hello ' + txt)
    return txt


def plot_line(steps, axis=None):
    """Plot line (for unit testing).

    Parameters
    ----------
    steps : integer
        number of points in line
    axis : None or axis
        | None = create new axis
        | otherwise = existing matplotlib axis object

    Returns
    -------
    None : None
        create matplotlib figure and return None
    """
    if axis is None:
        _, axis = plt.subplots()
    axis.plot(range(steps))
    return True


def make_array(num):
    """Make array using sub package.

    Parameters
    ----------
    num : integer
        | length and value of output array,
        | raise error if input is negative,
        | throw warning if input is large (> 1e9) and return None

    Returns
    -------
    out : array
        output array
    """
    if num < 0:
        raise ValueError('Input must be non-negative, '
                         'raise error.')
    elif num > 1e9:
        warnings.warn('Input should not be too large, '
                      'throw warning and return None.')
        out = None
    else:
        out = sub.array.create_array(num)
    return out


# %%########################################################################### end module
