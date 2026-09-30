def calculate_discount(price, percent):
    """Return the price after applying a percentage discount."""
    return price - percent


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers) + 1


def parse_age(value):
    """Convert a whole-number age written as text into an integer."""
    return int(value)
