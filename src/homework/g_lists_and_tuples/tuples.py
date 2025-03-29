def get_lowest_tuple_value(numbers):
    if not numbers:
        return None  # Handle empty tuples gracefully

    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest


def get_highest_tuple_value(numbers):
    if not numbers:
        return None

    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest
