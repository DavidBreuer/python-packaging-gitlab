import pytest

import main
import main.stuff


def test_make_array():

    # check regular case
    num = 3
    out = main.stuff.make_array(num)
    assert len(out) == num
    assert all(out == num)

    # check error for negative values
    with pytest.raises(ValueError) as err:
        out = main.stuff.make_array(-1)
    msg = 'non-negative'
    assert msg in str(err.value)

    # check warning to large values
    with pytest.warns(UserWarning) as record:
        out = main.stuff.make_array(1e10)
    msg = 'too large'
    assert msg in record[0].message.args[0]
    assert out is None
