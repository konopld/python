import csv


def open_file(filename, mode='r', encoding='utf-8', newline='\n'):
    try:
        file = open(filename, mode=mode, encoding=encoding, newline=newline)

        return file
    except FileNotFoundError:
        print(f'Файл {filename} не знайдено.')
    except IOError:
        print(f'Помилка з читанням/записом файлу {filename}')
    except Exception as e:
        print(f'Невідома помилка з роботою з файлом {filename}. {type(e)}: {e}')


def write_to_csv(filename, data, delimiter=','):
    """
    Записує 
    """
    csvfile = open_file(filename, mode='w', newline='')
    if csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        # writer.writerows(data)
        writer.writerows(data)
        csvfile.close()
        print(f'Дані додано до {filename} успішно!')


def main():
    file = open_file('data.csv')
    reader = csv.DictReader(file, delimiter=',')

    export_data = [
        ['Country Name', 'Min Inflation Year', 'Min Inflation Value', 'Max Inflation Year', 'Max Inflation Value'],
    ]

    for row in reader:
        export_row = [row['Country Name']]

        min_infl = {'year': '', 'value': 10000}
        max_infl = {'year': '', 'value': -10000}

        for i in range(1991, 2019):
            key = f'{i} [YR{i}]'

            try:
                value = float(row[key])
            except (KeyError, ValueError):
                continue

            if value:
                if value < min_infl['value']:
                    min_infl['year'] = key
                    min_infl['value'] = value
                elif value > max_infl['value']:
                    max_infl['year'] = key
                    max_infl['value'] = value

                print(f'Year {i} Infation: {value}')

        export_row += [min_infl['year'], min_infl['value'], max_infl['year'], max_infl['value']]
        export_data.append(export_row)
        
    file.close()
    
    write_to_csv('export.csv', export_data)

if __name__ == "__main__":
    main()