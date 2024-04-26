def is_prime(number):
    limit = number
    divisor = 2
    while limit > divisor:
        if number % divisor == 0:
            return False
        else:
            limit = number / divisor
            divisor += 1
    return True
