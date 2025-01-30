from plates import is_valid

def test_valid_letters(): #must start with 2 letters
    assert is_valid("CS50") == True
    assert is_valid("C50") == False
    assert is_valid("carro") == True
    assert is_valid("580") == False

def test_valid_lenght(): #must be 2-6 characteres
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("CSCSC50") == False
    assert is_valid("") == False

def test_valid_numbers(): #numbers at the end
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("CS50S") == False

def test_valid_zero():   #first number not zero
    assert is_valid("CS05") == False
    assert is_valid("CSF00") == False

def test_valid_specials():  #NO special characters
    assert is_valid("CS4 5") == False
    assert is_valid("CS45.") == False
    assert is_valid("CS5?") == False
    assert is_valid("*CS50") == False
    assert is_valid(" CS5") == False
    assert is_valid("CS,50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS#50") == False