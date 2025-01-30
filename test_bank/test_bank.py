from bank import value

def test_value0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("heLLo") == 0
    assert value("heLLo darkness my old friend") == 0

def test_value20():
    assert value("hi") == 20
    assert value("HEy") == 20
    assert value("How are you") == 20
    assert value("Halalalal") == 20


def test_value100():
    assert value("yo") == 100
    assert value("what's up") == 100
    assert value("sabasawa") == 100
    assert value("are you feeling alright") == 100