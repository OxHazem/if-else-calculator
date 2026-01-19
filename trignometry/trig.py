import math
from utils.validators import validate_non_negative


def degrees_to_radians(degrees: float) -> float:
    validate_non_negative(degrees, "Angle")
    return math.radians(degrees)


def sine(degrees: float) -> float:
    validate_non_negative(degrees, "Angle")
    x = degrees_to_radians(degrees)
    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040


def cosine(degrees: float) -> float:
    validate_non_negative(degrees, "Angle")
    x = degrees_to_radians(degrees)
    return 1 - (x**2)/2 + (x**4)/24 - (x**6)/720


def tangent(degrees: float) -> float:
    validate_non_negative(degrees, "Angle")
    cos_val = cosine(degrees)
    if cos_val == 0:
        raise ZeroDivisionError("Tangent undefined for this angle")
    return sine(degrees) / cos_val


def secant(degrees: float) -> float:
    cos_val = cosine(degrees)
    if cos_val == 0:
        raise ZeroDivisionError("Secant undefined for this angle")
    return 1 / cos_val


def cosecant(degrees: float) -> float:
    sin_val = sine(degrees)
    if sin_val == 0:
        raise ZeroDivisionError("Cosecant undefined for this angle")
    return 1 / sin_val


def cotangent(degrees: float) -> float:
    tan_val = tangent(degrees)
    if tan_val == 0:
        raise ZeroDivisionError("Cotangent undefined for this angle")
    return 1 / tan_val
