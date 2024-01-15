def is_prime_number(number: int) -> bool:
    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


print(is_prime_number(2))


def factorize_number(number: int) -> list:
    divisor = 2
    result = []

    while number > 1:
        if number % divisor == 0:
            result.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return result


print(factorize_number(999))
