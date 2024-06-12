def add(a:int, b:int) -> int:
    return a+b

def substract(a:int, b:int) -> int:
    return b - a

def multiply(a:int, b:int) -> int:
    return a * b

def devide(a:int, b:int) -> int:
    return a // b


def test_add() -> None:
    assert add(2, 4) == 6
    
def test_substruct() -> None:
    assert substract(3, 7) == 4
    
def test_multiply() -> None:
    assert multiply(2, 4) == 8

def test_devide() -> None:
    assert devide(12, 3) == 4