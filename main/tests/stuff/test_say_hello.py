import main
import main.stuff


def test_say_hello():
    txt = 'blabla'
    out = main.stuff.say_hello(txt)
    assert txt == out
