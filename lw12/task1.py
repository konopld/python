import json
from generate_random_details import details_names
from datetime import datetime, timedelta

def display_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    print('\n--- Display JSON ---\n')

    print(json.dumps(data, indent=4))

def add_to_json(filename):
    with open(filename, 'r') as file:
        data: list = json.load(file)

    print('\n--- Add record to JSON ---\n')
    
    details = {name: int(input(f'Enter amount of {name}: ')) for name in details_names}
    date = input('Enter date (0 for now): ')

    record = {
        'details': details,
        'date': date if date != '0' else datetime.now().strftime('%d-%m-%Y')
    }

    data.append(record)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f'Added successfully! Record index: {len(data)-1}')

def remove_from_json(filename):
    """
    Видалення нового запису у JSON файл
    """
    with open(filename, 'r') as file:
        data: list = json.load(file)

    print('\n--- Remove record from JSON ---\n')
    
    value = int(input('Enter record index: '))
    data.pop(value)

    print(f'Record with index {value} has been removed successfully.')

def find_by_field(filename):
    """
    Пошук даних у JSON файлі за одним із полів на вибір
    """
    with open(filename, 'r') as file:
        data: list = json.load(file)

    print('\n--- Find record in JSON ---\n')

    print('Choose search mode:')
    print('1 - by detail name')
    print('2 - by date')
    print('3 - by index')

    mode = int(input('Mode (1-3): '))
    filtered_records = []
    record_index = None
    
    if mode == 1:
        key = input('Enter detail name: ')
        value = int(input('Enter amount of details: '))
        for record in data:
            if record['details'].get(key) == value:
                filtered_records.append(record)
                record_index = data.index(record)
    elif mode == 2:
        value = input('Enter date (dd-mm-yyyy): ')
        for record in data:
            if record['date'] == value:
                filtered_records.append(record)
                record_index = data.index(record)
    elif mode == 3:
        value = int(input('Enter record index: '))
        try:
            filtered_records.append(data[value])
            record_index = value
        except IndexError:
            print('There is not record with this index.')

    else:
        print('Invalid mode. Try again.')
    
    print(json.dumps(filtered_records, indent=4))
    print('Record index:', record_index)

def display_total_week_price(filename, details_prices):
    # Задано дані про кількість деталей п’яти видів, які випускав цех кожен день. 
    # Скласти програму, яка визначає загальну вартість деталей за один тиждень.
    with open(filename, 'r') as file:
        data: list = json.load(file)

    print('\n--- Main function ---\n')

    value = input('Enter start date of week (dd-mm-yyyy): ')
    start_date = datetime.strptime(value, '%d-%m-%Y')
    end_date = start_date + timedelta(days=6)
    
    active_days = 0
    total_price = 0

    for record in data:
        record_date = datetime.strptime(record['date'], '%d-%m-%Y')
        if start_date <= record_date <= end_date:
            active_days += 1
            for name, amount in record['details'].items():
                total_price += amount * details_prices[name]
    
    print(f'The workshop worked {active_days} days out of 7')
    print(f'Total price: {total_price}$')
    

    

def main():
    FILENAME = 'details.json'
    DETAILS_PRICES = {
        'Engine Pistons': 50,
        'Gear Shafts': 45,
        'Steering Knuckles': 75,
        'Brake Discs': 40,
        'Valve Bodies': 70,
    }

    while True:
        try:
            print('\n', '-' * 20, sep='')
            print('Choose the action: ')
            print('1 - Display JSON')
            print('2 - Add record to JSON')
            print('3 - Remove record from JSON')
            print('4 - Find record in JSON')
            print('5 - Display total price amount for details (1 week)')
            print('quit - Exit')

            action = input('\nACTION (1-5, quit): ')

            if action == '1':
                display_json(FILENAME)
            elif action == '2':
                add_to_json(FILENAME)
            elif action == '3':
                remove_from_json(FILENAME)
            elif action == '4':
                find_by_field(FILENAME)
            elif action == '5':
                display_total_week_price(FILENAME, DETAILS_PRICES)
            elif action == 'quit':
                quit()
            else:
                print('Wrong action.')
        
        except Exception as e:
            print(f'Error: {type(e)} | {e}')


if __name__ == "__main__":
    main()