from numb3rs import validate

def test_validate():
    assert validate("127.0.0.0") == True
    assert validate("127.0.0.255") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.256") == False
    assert validate("255.1") == False
    assert validate("cat") == False
