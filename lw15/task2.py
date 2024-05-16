import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Створіть датафрейм з даними використання велодоріжок за рік, заданий варіантом (8)
    # 2016 рік. Визначте, який місяць найбільш популярний у велосипедистів.

    # зчитування даних
    data = pd.read_csv('comptagevelo20162.csv')

    # перетворення стовпця 'Date' на формат дати
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

    # визначення місяця для кожної дати
    data['Month'] = data['Date'].dt.month

    races_list = data.columns[2:-1]  # усі стовпці з кількістю заїздів
    monthly_races = data[races_list].sum(axis=1)  # сума заїздів по днях
    data['Total'] = monthly_races

    # групування даних по місяцях і знаходження суми заїздів для кожного місяця
    monthly_sum = data.groupby('Month')['Total'].sum()

    # визначення місяця з найбільшою кількістю заїздів
    most_popular_month = monthly_sum.idxmax()

    # cтворення графіка
    plt.figure(figsize=(10, 6))
    monthly_sum.plot(kind='bar', color='skyblue')
    plt.title('Кількість заїздів по місяцях')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість заїздів')
    plt.xticks(rotation=0)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
    print(f'Найпопулярніший місяць: {most_popular_month}')
    print(f'Заїзди по місяцях: {monthly_sum}')


if __name__ == "__main__":
    main()