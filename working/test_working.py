import pytest
import working as w

def test_convert():
    assert w.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert w.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert w.convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert w.convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_exceptions():
    with pytest.raises(ValueError):
        w.convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        w.convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        w.convert("9 AM to 15 PM")
    with pytest.raises(ValueError):
        w.convert("9 A to 5")
