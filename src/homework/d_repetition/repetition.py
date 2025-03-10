def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    total = 0
    current = 1
    while current <= num:
        if current % 2 != 0:
            total += current
        current += 1
    return total
