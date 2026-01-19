# geometry/lateral_areas.py
import math
from utils.validators import validate_non_negative


def cone_lateral_area(radius: float, height: float) -> float:
    validate_non_negative(radius, "Radius")
    validate_non_negative(height, "Height")
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * slant_height


def pyramid_lateral_area(length: float, width: float, height: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    validate_non_negative(height, "Height")
    slant_length = math.sqrt((width / 2) ** 2 + height ** 2)
    slant_width = math.sqrt((length / 2) ** 2 + height ** 2)
    return length * slant_length + width * slant_width


def cube_lateral_area(side: float) -> float:
    validate_non_negative(side, "Side")
    return 4 * side ** 2


def cuboid_lateral_area(length: float, width: float, height: float) -> float:
    validate_non_negative(length, "Length")
    validate_non_negative(width, "Width")
    validate_non_negative(height, "Height")
    return 2 * height * (length + width)


def cylinder_lateral_area(radius: float, height: float) -> float:
    validate_non_negative(radius, "Radius")
    validate_non_negative(height, "Height")
    return 2 * math.pi * radius * height
