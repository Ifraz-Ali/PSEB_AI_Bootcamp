import pytest

# print("start")
def isAgeValid(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 18:
        return True
    else:
        return False

def test_age_17():
    assert isAgeValid(17) == False

def test_age_18():
    assert isAgeValid(18) == True

def test_age_negative():
    with pytest.raises(ValueError):
        isAgeValid(-1)
