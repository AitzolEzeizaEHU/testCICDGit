"""A simple demo application."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    """Main function."""
    print("Hello, World!")
    print(greet("Alice"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
