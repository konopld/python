def input_array():
    """ Input array with int elements """
    while True:
        try:
            array_raw = input('Enter array integer elements separated by a space: ')
            return [int(i) for i in array_raw.split()]
        except ValueError:
            print('ERROR. Array elements must be integers. Example: 0 3 6')

def bubble_sort(arr):
    unsorted = True

    while unsorted:
        unsorted = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                unsorted = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

def main():
    arr = input_array()
    print(f'Sorted array: {bubble_sort(arr)}')


if __name__ == "__main__":
    main()
