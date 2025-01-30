import seasons as s
from datetime import date
import pytest

def test_validateDateFormatSysExit():
    #Letters
    with pytest.raises(SystemExit):
        s.validateDateFormat("a999-12-12")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999-1a-12")

    with pytest.raises(SystemExit):
        s.validateDateFormat("September 12, 1999")


    #No dash
    with pytest.raises(SystemExit):
        s.validateDateFormat("1999,12,12")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999.12.12")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999-12,12")


    #Wrong size
    with pytest.raises(SystemExit):
        s.validateDateFormat("99-12-12")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999-2-12")

    with pytest.raises(SystemExit):
        assert s.validateDateFormat("1999-12-4")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999-12-004")

    with pytest.raises(SystemExit):
        s.validateDateFormat("1999-012-04")


def test_validateDateFormatRight():
    assert s.validateDateFormat("1985-07-12") == ('1985', '07', '12')
    assert s.validateDateFormat("2004-01-25") == ('2004', '01', '25')


def test_calculateDeltaMinutes():
    assert s.calculateDeltaMinutes(date(1985, 7, 13), date(1985, 7, 12)) == 1440
    assert s.calculateDeltaMinutes(date(2024, 10, 23), date(2022, 10, 23)) == 1052640
