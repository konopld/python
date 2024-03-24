def input_array():
    """ Input array with int elements """
    while True:
        try:
            array_raw = input('Enter array integer elements separated by a space: ')
            return [int(i) for i in array_raw.split()]
        except ValueError:
            print('ERROR. Array elements must be integers. Example: 0 3 6')

def prod_odd_indices(arr):
    """ Find product of elements with odd indices """
    prod = 1
    for i in range(1, len(arr), 2):
        prod *= arr[i]
    return prod

def main():
    arr = input_array()
    print(f'Entered array with length N = {len(arr)}: {arr}')
    print(f'Product of elements with odd indices: {prod_odd_indices(arr)}')


if __name__ == "__main__":
    main()