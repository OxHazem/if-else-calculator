# main.py

from utils.input_handler import get_float, get_choice

from arithmetic.basics import add, subtract, multiply, divide, power
from geometery.Areas import (
    triangle_area, circle_area, square_area, rectangle_area,
    cube_area, cuboid_area, cylinder_area, sphere_area
)
from geometery.Volumes import (
    cylinder_volume, sphere_volume, cuboid_volume,
    cube_volume, pyramid_volume, cone_volume
)
from geometery.Lateral_areas import (
    cone_lateral_area, pyramid_lateral_area,
    cube_lateral_area, cuboid_lateral_area, cylinder_lateral_area
)
from trignometry.trig import (
    sine, cosine, tangent, secant, cosecant, cotangent
)
from algebra.quadratic import solve_quadratic
from conversions.weight import (
    from_milligrams, from_grams, from_kilograms, from_tons
)
from conversions.Length import (
    from_millimeters, from_centimeters, from_meters, from_kilometers
)


def print_dict(result: dict):
    for k, v in result.items():
        print(f"{k}: {v}")




def arithmetic_menu():
    choice = get_choice(
        "\nArithmetic:\n"
        "a) add\nb) subtract\nc) multiply\nd) divide\ne) power\n> ",
        {"a", "b", "c", "d", "e"}
    )

    if choice == "e":
        base = get_float("Base: ")
        exp = get_float("Exponent: ")
        print(power(base, exp))
        return

    nums = input("Enter numbers separated by space: ").split()
    numbers = [float(n) for n in nums]

    ops = {
        "a": add,
        "b": subtract,
        "c": multiply,
        "d": divide,
    }

    print(ops[choice](numbers))


def areas_menu():
    choice = get_choice(
        "\nAreas:\n"
        "a) triangle\nb) circle\nc) square\nd) rectangle\n"
        "e) cube\nf) cuboid\ng) cylinder\nh) sphere\n> ",
        set("abcdefgh")
    )

    if choice == "a":
        a = get_float("a: "); b = get_float("b: "); c = get_float("c: ")
        print(triangle_area(a, b, c))
    elif choice == "b":
        print(circle_area(get_float("Radius: ")))
    elif choice == "c":
        print(square_area(get_float("Side: ")))
    elif choice == "d":
        print(rectangle_area(get_float("Length: "), get_float("Width: ")))
    elif choice == "e":
        print(cube_area(get_float("Side: ")))
    elif choice == "f":
        print(cuboid_area(
            get_float("Length: "),
            get_float("Width: "),
            get_float("Height: ")
        ))
    elif choice == "g":
        print(cylinder_area(
            get_float("Radius: "),
            get_float("Height: ")
        ))
    elif choice == "h":
        print(sphere_area(get_float("Radius: ")))


def volumes_menu():
    choice = get_choice(
        "\nVolumes:\n"
        "a) cylinder\nb) sphere\nc) cuboid\nd) cube\ne) pyramid\nf) cone\n> ",
        set("abcdef")
    )

    if choice == "a":
        print(cylinder_volume(get_float("Radius: "), get_float("Height: ")))
    elif choice == "b":
        print(sphere_volume(get_float("Radius: ")))
    elif choice == "c":
        print(cuboid_volume(
            get_float("Length: "),
            get_float("Width: "),
            get_float("Height: ")
        ))
    elif choice == "d":
        print(cube_volume(get_float("Side: ")))
    elif choice == "e":
        print(pyramid_volume(
            get_float("Length: "),
            get_float("Width: "),
            get_float("Height: ")
        ))
    elif choice == "f":
        print(cone_volume(get_float("Radius: "), get_float("Height: ")))


def lateral_areas_menu():
    choice = get_choice(
        "\nLateral Areas:\n"
        "a) cone\nb) pyramid\nc) cube\nd) cuboid\ne) cylinder\n> ",
        set("abcde")
    )

    if choice == "a":
        print(cone_lateral_area(get_float("Radius: "), get_float("Height: ")))
    elif choice == "b":
        print(pyramid_lateral_area(
            get_float("Length: "),
            get_float("Width: "),
            get_float("Height: ")
        ))
    elif choice == "c":
        print(cube_lateral_area(get_float("Side: ")))
    elif choice == "d":
        print(cuboid_lateral_area(
            get_float("Length: "),
            get_float("Width: "),
            get_float("Height: ")
        ))
    elif choice == "e":
        print(cylinder_lateral_area(
            get_float("Radius: "),
            get_float("Height: ")
        ))


def trigonometry_menu():
    choice = get_choice(
        "\nTrigonometry:\n"
        "a) sin\nb) cos\nc) tan\nd) sec\ne) csc\nf) cot\n> ",
        set("abcdef")
    )

    angle = get_float("Angle (degrees): ")

    funcs = {
        "a": sine,
        "b": cosine,
        "c": tangent,
        "d": secant,
        "e": cosecant,
        "f": cotangent,
    }

    print(funcs[choice](angle))


def quadratic_menu():
    a = get_float("a: ")
    b = get_float("b: ")
    c = get_float("c: ")

    result = solve_quadratic(a, b, c)
    print(result)


def conversions_menu():
    choice = get_choice(
        "\nConversions:\n"
        "a) weight\nb) length\n> ",
        {"a", "b"}
    )

    if choice == "a":
        sub = get_choice(
            "a) mg\nb) g\nc) kg\nd) ton\n> ",
            {"a", "b", "c", "d"}
        )
        value = get_float("Value: ")
        funcs = {
            "a": from_milligrams,
            "b": from_grams,
            "c": from_kilograms,
            "d": from_tons,
        }
        print_dict(funcs[sub](value))

    else:
        sub = get_choice(
            "a) mm\nb) cm\nc) m\nd) km\n> ",
            {"a", "b", "c", "d"}
        )
        value = get_float("Value: ")
        funcs = {
            "a": from_millimeters,
            "b": from_centimeters,
            "c": from_meters,
            "d": from_kilometers,
        }
        print_dict(funcs[sub](value))




MAIN_MENU = {
    "a": arithmetic_menu,
    "b": areas_menu,
    "c": volumes_menu,
    "d": lateral_areas_menu,
    "e": trigonometry_menu,
    "f": quadratic_menu,
    "g": conversions_menu,
}


def main():
    while True:
        choice = get_choice(
            "\nMAIN MENU:\n"
            "a) Arithmetic\n"
            "b) Areas\n"
            "c) Volumes\n"
            "d) Lateral Areas\n"
            "e) Trigonometry\n"
            "f) Quadratic Equation\n"
            "g) Unit Conversions\n"
            "x) Exit\n> ",
            set("abcdefgx")
        )

        if choice == "x":
            print("Goodbye 👋")
            break

        try:
            MAIN_MENU[choice]()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
