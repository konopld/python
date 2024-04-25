import numpy as np
import matplotlib.pyplot as plt

# функція
def Y(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)


def main():
    """
    Побудуйте графік функції. Оберіть суцільний тип лінії, 
    задайте колір та товщину графіку та позначте осі, 
    виведіть назву графіка на екран, вставте легенду. 
    Використайте бібліотеку Matplotlib.

    Y(x)=5*sin(10*x)*sin(3*x)/(x^(1/2)), x=[1...7]
    """
    # x від 1 до 7
    x = np.linspace(1, 7, 400)

    # значення y
    y = Y(x)

    # графік
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Y(x) = 5*sin(10*x)*sin(3*x)/sqrt(x), x=[1...7]', color='green', linewidth=2, linestyle='-')

    # осі
    plt.xlabel('x')
    plt.ylabel('y(x)')

    # назва графіка
    plt.title('Y(x) = 5*sin(10*x)*sin(3*x)/sqrt(x)')

    # легенда
    plt.legend()

    # відображення графіку
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()