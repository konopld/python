from math import sqrt, exp


def calc_z(x):
    return exp(sqrt(x)) / sqrt(1 - x)

def calc_prod(n):
    res = 1

    for i in range(2 - n % 2, n + 1, 2):  # якщо n парне - початок з 2, інакше з 1
        res *= i

    return res


def main():
    # 1 function
    x = float(input('Enter x: '))
    print(f'z = {calc_z(x)}')

    # 2 function
    n = int(input('Enter n: '))
    print(f'Prod = {calc_prod(n)}')


if __name__ == "__main__":
    main()
