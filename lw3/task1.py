
def main():
    s = input('Enter string: ')

    while len(s) < 7:
        s = input('String length must be >= 7. Enter string: ')

    print(s[6::7])



if __name__ == "__main__":
    main()