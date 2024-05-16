import pandas as pd

def main():
    # Перетворіть словник, створений у лабораторній роботі №6, на датафрейм, 
    # у разі необхідності доповніть словник даними, виведіть його на екран. 
    # Виконайте агрегацію та групування даних із заданої предметної області.

    data = {
        'Car': ['Car 1', 'Car 2', 'Car 3', 'Car 4', 'Car 5', 'Car 6', 'Car 7', 'Car 8', 'Car 9', 'Car 10'],
        'Power': [120, 80, 95, 98, 70, 75, 90, 180, 220, 280],
        'Price': [7000, 5000, 10000, 15000, 5000, 5500, 6000, 12000, 18000, 25000]
    }
    df = pd.DataFrame(data)

    print(df)

    # інтервали
    bins = [0, 100, 200, 300]
    # мітки
    labels = ['Low Power', 'Medium Power', 'High Power']

    # новий стовбець 'Power Range': розділяємо стовбець Power за інтервалами bins з мітками labels для кожного
    df['Power Range'] = pd.cut(df['Power'], bins=bins, labels=labels)

    # групуємо (groupby) дані за стовбцем Power Range та агрегуємо (agg) за ціною
    grouped = df.groupby('Power Range', observed=False).agg({'Price': ['mean', 'min', 'max']})
    print(grouped)

if __name__ == "__main__":
    main()
