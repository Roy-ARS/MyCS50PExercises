import pytest
import fuel

def test_convert():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/2") == 100
    assert fuel.convert("10/20") == 50
    assert fuel.convert("3/11") == 27


def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(88) == "88%"
    assert fuel.gauge(10) == "10%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"


def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0")
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
