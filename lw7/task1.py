
def display_items(obj: dict):
    """
    Виведення на екран всіх значень словника
    """
    for k, v in obj.items():
        print(f'{k}: {v}')

def add_to_dict(obj: dict):
    """
    Додавання нового запису до словника
    """
    name = input('Enter car name: ')
    power = float(input('Enter car power: '))
    price = float(input('Enter car price: '))

    obj[name] = {'power': power, 'price': price}

    print(f'Car "{name}" added successfully!')

def remove_from_dict(obj: dict):
    """
    Видалення запису зі словника
    """
    name = input('Enter car name that you want to remove: ')

    try:
        obj.pop(name)
    except KeyError:
        print(f'Car with name "{name}" does not exist')
        return False

    print(f'Car "{name}" removed successfully!')
    return True

def display_sorted_items(obj: dict):
    """
    Перегляд вмісту словника за відсортованими ключами
    """
    sorted_items = sorted(obj.items())

    for k, v in sorted_items:
        print(f'{k}: {v}')

def display_power_more_100(obj: dict):
    # Задано дані про потужність двигуна (в кінських силах – к.с.) і вартість n=10 
    # легкових автомобілів. Скласти програму, яка визначає загальну вартість автомобілів,
    # у яких потужність двигуна перевищує 100 к.с.

    for k, v in obj.items():
        if v['power'] >= 100:
            print(f'\n--- {k} ---')
            display_sorted_items(v)

def main():
    cars = {
        'Car 1': {'power': 120, 'price': 7000},
        'Car 2': {'power': 80, 'price': 5000},
        'Car 3': {'power': 95, 'price': 10000},
        'Car 4': {'power': 98, 'price': 15000},
        'Car 5': {'power': 70, 'price': 5000},
        'Car 6': {'power': 75, 'price': 5500},
        'Car 7': {'power': 90, 'price': 6000},
        'Car 8': {'power': 180, 'price': 12000},
        'Car 9': {'power': 220, 'price': 18000},
        'Car 10': {'power': 280, 'price': 25000},
    }

    while True:
        print(
            "\nChoose the action: \n"
            "1 - Display all cars\n"
            "2 - Add new car\n"
            "3 - Remove a car\n"
            "4 - Display cars sorted by name\n"
            "5 - Display cars with power more than 100\n"
            "exit - Exit the program\n"
        )

        action = input('Action: ')

        if action == '1':
            display_items(cars)
        elif action == '2':
            add_to_dict(cars)
        elif action == '3':
            remove_from_dict(cars)
        elif action == '4':
            display_sorted_items(cars)
        elif action == '5':
            display_power_more_100(cars)
        elif action == 'exit':
            print('Bye!')
            quit()
        else:
            print('Wrong action. Choose action (1-5)')

if __name__ == "__main__":
    main()