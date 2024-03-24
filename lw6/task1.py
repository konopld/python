def split_by_index(arr: list, index: int):
    """ Splits array by index """
    return [
        arr[:index],
        arr[index:]
    ]

def input_index(arr):
    """ Validates entered index """
    while True:
        try:
            index = int(input('Enter splitter index: '))
            print(f'Element {arr[index]} with index {index}')
            return index
        except (ValueError, IndexError):
            print(f'Invalid index. Length of array: {len(arr)}')


def main():
    arr = input('Enter array elements separated by a space: ').split(' ')
    index = input_index(arr)

    print(f'Entered array: {arr}')

    result = split_by_index(arr, index)
    print(f'Splitted arrays: {result}')


if __name__ == "__main__":
    main()
