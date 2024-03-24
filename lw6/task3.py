
def main():
    first_set = set(map(str, 'cd'))
    second_set = set(map(str, 'aeiouy'))

    result_set = first_set.union(second_set)
    print(result_set)


if __name__ == "__main__":
    main()
