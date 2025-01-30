import pytest
import um

def test_convert():
    assert um.count("um") == 1
    assert um.count(" um,") == 1
    assert um.count("umm") == 0
    assert um.count("Um, thanks for the album") == 1
    assert um.count("um, thanks um...") == 2
    assert um.count("umm, are you um serious about the umbrella? um? ok..") == 2

