import math

def solve_quadratic(a: float, b: float, c: float):

    if a == 0 and b == 0 and c == 0:
        return ("all_real", None, None)

    if a == 0 and b == 0:
        return ("no_solution", None, None)

 
    if a == 0:
        x = -c / b
        return ("linear", x, None)

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return ("two_real", x1, x2)

    if discriminant == 0:
        x = -b / (2 * a)
        return ("one_real", x, None)

    real = -b / (2 * a)
    imag = math.sqrt(-discriminant) / (2 * a)
    return ("complex", complex(real, -imag), complex(real, imag))
