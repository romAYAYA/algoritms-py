x = 2
base = 2

while x > 0:  # пока есть цифры
    digit = x % base  # бери последнюю цифру и печатай
    print(digit, end='')
    x //= base  # отрывай последнюю цифру от числа

print(x)
