import pytest
from jar import Jar


def test_init():
    jar_1 = Jar(16, 1)
    jar_2 = Jar(9, 8)

    assert str(jar_1) == "🍪"
    assert jar_1.size == 1
    assert jar_1.capacity == 16
    assert str(jar_2) == "🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar_2.size == 8
    assert jar_2.capacity == 9
    with pytest.raises(ValueError) as exc:
        jar_3 = Jar(2, 3)
    assert str(exc.value) == "Jar can not contain that many cookies"


def test_deposit():
    jar = Jar(10, 4)
    jar.deposit(1)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    with pytest.raises(ValueError) as exc:
        jar.deposit(3)
    assert str(exc.value) == "That many cookies does not fit into the jar"


def test_withdraw():
    jar = Jar (10, 5)
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError) as exc:
        jar.withdraw(2)
    assert str(exc.value) == "Jar does not have that many cookies"



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



