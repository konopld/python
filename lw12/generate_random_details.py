import json
import random
from datetime import datetime, timedelta

details_names = [
    'Engine Pistons',
    'Gear Shafts',
    'Steering Knuckles',
    'Brake Discs',
    'Valve Bodies',
]

def generate_file(filename, details_names=details_names, records=7):
    json_array = []
    start_date = datetime.now()
    
    for i in range(records + 1):
        details = {name: random.randint(50, 150) for name in details_names}
        record_date = start_date + timedelta(i)
        record = {'details': details} | {'date': record_date.strftime("%d-%m-%Y")}
        json_array.append(record)
    
    with open(filename, 'w') as file:
        json.dump(json_array, file, indent=4)


if __name__ == '__main__':
    generate_file('details.json')

