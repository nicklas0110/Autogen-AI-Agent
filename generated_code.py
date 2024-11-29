def average(numbers):
    """
    Returns the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers.
    """

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)