
from utils.validators import validate_non_negative


def from_millimeters(mm: float) -> dict:
    validate_non_negative(mm, "Millimeters")
    return {
        "millimeters": mm,
        "centimeters": mm / 10,
        "meters": mm / 1_000,
        "kilometers": mm / 1_000_000,
    }


def from_centimeters(cm: float) -> dict:
    validate_non_negative(cm, "Centimeters")
    return {
        "millimeters": cm * 10,
        "centimeters": cm,
        "meters": cm / 100,
        "kilometers": cm / 100_000,
    }


def from_meters(m: float) -> dict:
    validate_non_negative(m, "Meters")
    return {
        "millimeters": m * 1_000,
        "centimeters": m * 100,
        "meters": m,
        "kilometers": m / 1_000,
    }


def from_kilometers(km: float) -> dict:
    validate_non_negative(km, "Kilometers")
    return {
        "millimeters": km * 1_000_000,
        "centimeters": km * 100_000,
        "meters": km * 1_000,
        "kilometers": km,
    }
