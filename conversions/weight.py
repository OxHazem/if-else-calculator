
from utils.validators import validate_non_negative


def from_milligrams(mg: float) -> dict:
    validate_non_negative(mg, "Milligrams")
    return {
        "milligrams": mg,
        "grams": mg / 1_000,
        "kilograms": mg / 1_000_000,
        "tons": mg / 1_000_000_000,
    }


def from_grams(g: float) -> dict:
    validate_non_negative(g, "Grams")
    return {
        "milligrams": g * 1_000,
        "grams": g,
        "kilograms": g / 1_000,
        "tons": g / 1_000_000,
    }


def from_kilograms(kg: float) -> dict:
    validate_non_negative(kg, "Kilograms")
    return {
        "milligrams": kg * 1_000_000,
        "grams": kg * 1_000,
        "kilograms": kg,
        "tons": kg / 1_000,
    }


def from_tons(tons: float) -> dict:
    validate_non_negative(tons, "Tons")
    return {
        "milligrams": tons * 1_000_000_000,
        "grams": tons * 1_000_000,
        "kilograms": tons * 1_000,
        "tons": tons,
    }
