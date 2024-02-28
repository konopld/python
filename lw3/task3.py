from random import choice

def main():
    s = input('Enter string: ')

    words = [word for word in s.split() if word[0].lower() == 'к']
    print(choice(words))


if __name__ == "__main__":
    main()