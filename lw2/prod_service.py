def calc_prod(n):
    res = 1

    for i in range(2 - n % 2, n + 1, 2):  # якщо n парне - початок з 2, інакше з 1
        res *= i

    return res
