import math
from utils.validators import validate_non_negative, validate_triangle


def triangle_area(a: float, b: float, c: float) -> float:
    validate_triangle(a, b, c)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def circle_area(radius: float) -> float:
    validate_non_negative(radius, "Radius")
    return math.pi * radius ** 2


def square_area(side: float) -> float:
    validate_non_negative(side, "Side")
    return side ** 2


def rectangle_area(length: float, width: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    return length * width


def cube_area(side: float) -> float:
    validate_non_negative(side, "Side")
    return 6 * side ** 2


def cuboid_area(length: float, width: float, height: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    validate_non_negative(height, "Height")
    return 2 * (length * width + width * height + height * length)


def cylinder_area(radius: float, height: float) -> float:
    validate_non_negative(radius, "Radius")
    validate_non_negative(height, "Height")
    return 2 * math.pi * radius * (radius + height)


def sphere_area(radius: float) -> float:
    validate_non_negative(radius, "Radius")
    return 4 * math.pi * radius ** 2
