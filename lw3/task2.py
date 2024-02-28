
def main():
    s = input('Enter number (4-digit, integer): ')

    while not s.isdigit() or len(s) != 4:
        s = input('Invalid number. Enter number (4-digit, integer): ')
    
    print(s.count('7'))


if __name__ == "__main__":
    main()