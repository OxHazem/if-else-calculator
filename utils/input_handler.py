def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")


def get_choice(prompt: str, choices: set[str]) -> str:
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print("Invalid choice, try again.")