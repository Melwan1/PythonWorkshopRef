import sys

def add(x: int, y: int) -> int:
    result : int = x + y
    print(f"{x} + {y} = {result}")
    return result

def sub(x: int, y: int) -> int:
    result : int = x - y
    print(f"{x} - {y} = {result}")
    return result

def mul(x: int, y: int) -> int:
    result : int = x * y
    print(f"{x} * {y} = {result}")
    return result

def div(x: int, y: int) -> int:
    if (y == 0):
        print("Detected a division by zero", file=sys.stderr)
    else:
        result : int = x // y
        print(f"{x} // {y} = {result}")
        return result

def mod(x: int, y: int) -> int:
    if (y == 0):
        print("Detected a modulo by zero", file=sys.stderr)
    else:
        result : int = x % y
        print(f"{x} % {y} = {result}")
        return result

def pow(x: int, y: int) -> int:
    result : int = x ** y
    print(f"{x} ** {y} = {result}")
    return result

