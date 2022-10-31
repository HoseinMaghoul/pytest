def add(x, y):
    return x + y 


def subtarct(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError('cant division by zero')
    return x / y 

