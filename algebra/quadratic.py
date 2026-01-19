# algebra/quadratic.py
import math


def solve_quadratic(a: float, b: float, c: float):


    if a == 0 and b == 0 and c == 0:
        return "all_real"

    if a == 0 and b == 0:
        return None


    if a == 0:
        return -c / b


    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return root1, root2

    if discriminant == 0:
        root = -b / (2 * a)
        return root

    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    return (
        complex(real_part, -imaginary_part),
        complex(real_part, imaginary_part)
    )
