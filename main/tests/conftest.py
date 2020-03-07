"""Create fixtures for unit tests"""

# %%########################################################################### import modules

import matplotlib.pyplot as plt
import numpy as np
import pytest

# %%########################################################################### set parameters

# set seed
SEED = 42

# %%########################################################################### define fixtures


# tmpdir_factory is used to create temporary directory, see:
# http://doc.pytest.org/en/latest/tmpdir.html#the-tmp-path-factory-fixture
# scope='session' so that a new directory is created only once per test session
@pytest.fixture(scope='session')
def fake_temp(tmpdir_factory):
    """Return temporary directory"""
    fake_temp = str(tmpdir_factory.mktemp('temp'))
    return fake_temp


@pytest.fixture
def fake_array():
    """Return fake array"""
    np.random.seed(seed=SEED)
    fake_array = np.random.rand(30, 20)
    fake_array[fake_array > 0.95] = np.nan
    return fake_array


# scope='function' so that a new axis is created for each test and
# modifications do not affect subsequent tests
@pytest.fixture(scope='function')
def fake_plot():
    """Return axis object"""
    fake_plot = plt.subplots(nrows=1, ncols=1)
    return fake_plot


# %%########################################################################### end file
