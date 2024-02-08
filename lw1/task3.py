
def is_valid(s):
    """ Функція перевірки умови """
    try:
        n = int(s)
        return 1 <= n <= 9
    
    except ValueError:
        return False

def main():
    n = input('Enter N (1 <= N <= 9): ')

    while not is_valid(n):
        n = input('Invalid input. Enter N (1 <= N <= 9): ')

    n = int(n)

    for i in range(n):
        for j in range(n * 2):
            if j < n - 1 or j > n - 1 + i:
                print(' ', end=' ')
            else:
                print(j + 1 - i, end=' ')
        print('')
    
    for i in range(n):
        for j in range(n * 2):
            if j > n - 1 or i < n - 1 - j:
                print(' ', end=' ')
            else:
                print(n - j, end=' ')
        print('')

if __name__ == '__main__':
    main()
