"""A simple demo application."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Kaixo, {name}!"


def main() -> None:
    """Main function."""
    print("Kaixo, Mundua!")
    print(greet("Aitzol"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
