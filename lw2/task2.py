from prod_service import calc_prod

def main():
    n = int(input('Enter n: '))
    print(f'Prod = {calc_prod(n)}')


if __name__ == "__main__":
    main()