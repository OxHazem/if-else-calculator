
import math
from utils.validators import validate_non_negative


def cylinder_volume(radius: float, height: float) -> float:
    validate_non_negative(radius, "Radius")
    validate_non_negative(height, "Height")
    return math.pi * radius ** 2 * height


def sphere_volume(radius: float) -> float:
    validate_non_negative(radius, "Radius")
    return (4 / 3) * math.pi * radius ** 3


def cuboid_volume(length: float, width: float, height: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    validate_non_negative(height, "Height")
    return length * width * height


def cube_volume(side: float) -> float:
    validate_non_negative(side, "Side")
    return side ** 3


def pyramid_volume(length: float, width: float, height: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    validate_non_negative(height, "Height")
    return (length * width * height) / 3


def cone_volume(radius: float, height: float) -> float:
    validate_non_negative(radius, "Radius")
    validate_non_negative(height, "Height")
    return (math.pi * radius ** 2 * height) / 3
