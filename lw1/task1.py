
def main():
    a = int(input('Enter a (a > 0): '))
    
    while a <= 0:
        a = int(input('Enter a (a > 0): '))
    
    b = int(input('Enter b (b > 0): '))

    while b <= 0:
        b = int(input('Enter b (b > 0): '))

    if a > b:
        x = a * b - 1
    elif a == b:
        x = 255
    else:
        x = (a - 5) / b
    
    print(f'X = {x}')

if __name__ == '__main__':
    main()
