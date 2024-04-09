def open_file(filename, mode='r'):
    """
    Відкриває файл і обробляє помилки
    """
    try:
        file = open(filename, mode, encoding='utf-8')
        return file
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except IOError:
        print(f"Помилка вводу/виводу при роботі з файлом '{filename}'.")
    except Exception as e:
        print(f"Несподівана помилка при відкритті файлу '{filename}': {e}")
    return None

def create_file(filename, lines: list[str], length):
    """
    Створює файл з заданими рядками однакової довжини
    """
    file = open_file(filename, 'w')
    if file:
        for line in lines:
            file.write(line.ljust(length, ' ') + '\n')
        file.close()

def process_file(input_filename, output_filename, length):
    """
    Читає вміст вхідного файла, обробляє кожен рядок і записує результат у вихідний файл
    """
    input_file = open_file(input_filename, 'r')
    output_file = open_file(output_filename, 'w')
    if input_file and output_file:
        for line in input_file:
            # Видаляємо всі символи крім цифр
            processed_line = ''.join(filter(str.isdigit, line))

            output_file.write(processed_line.ljust(length, ' ') + '\n')
        input_file.close()
        output_file.close()


def print_file(filename):
    """
    Друкує вміст файла по рядках
    """
    file = open_file(filename, 'r')
    if file:
        for line in file:
            print(line, end='')
        file.close()

def main():
    lines = ['abc123', '456def', '789ghi']
    create_file('TF11_1.txt', lines, 10)
    process_file('TF11_1.txt', 'TF11_2.txt', 10)
    print_file('TF11_2.txt')


if __name__ == "__main__":
    main()
