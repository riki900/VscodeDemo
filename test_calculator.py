import pytest
from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(2, 3) == 5


def test_subtract():
    c = Calculator()
    assert c.subtract(6, 3) == 3


def test_multiply():
    c = Calculator()
    assert c.multiply(6, 3) == 18


def test_divide():
    c = Calculator()
    assert c.divide(6, 3) == 2


def test_add_operand1_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.add("one", 2)

    assert str(e.value) == '"one" is not a number.'


def test_add_operand2_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.add(1, "two")

    assert str(e.value) == '"two" is not a number.'

def test_subtract_operand1_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.subtract("one", 2)

    assert str(e.value) == '"one" is not a number.'


def test_subtract_operand2_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.subtract(1, "two")

    assert str(e.value) == '"two" is not a number.'

def test_multiply_operand1_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.multiply("one", 2)

    assert str(e.value) == '"one" is not a number.'


def test_multiply_operand2_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.multiply(1, "two")

    assert str(e.value) == '"two" is not a number.'

def test_divide_operand1_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.divide("one", 2)

    assert str(e.value) == '"one" is not a number.'
    
def test_divide_operand2_invalid():
    c = Calculator()
    with pytest.raises(ValueError) as e:
        assert c.divide(1, "two")

    assert str(e.value) == '"two" is not a number.'



