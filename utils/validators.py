def validate_non_negative(value: float, name: str = "Value") -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def validate_positive(value: float, name: str = "Value") -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def validate_triangle(a: float, b: float, c: float) -> None:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle inequality not satisfied")