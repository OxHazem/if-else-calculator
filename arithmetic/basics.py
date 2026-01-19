def add(numbers: list[float]) -> float:
    return sum(numbers)




def subtract(numbers: list[float]) -> float:
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result
    


def multiply(numbers: list[float]) -> float:
    result = 1
    for n in numbers:
        result *= n
    return result




def divide(numbers: list[float]) -> float:
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= n
    return result


def power(base: float, exponent: float) -> float:
    return base ** exponent