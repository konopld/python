import matplotlib.pyplot as plt
import json

def main():
    # Побудуйте кругову діаграму на основі даних з предметної області лабораторної роботи №12.  
    # Використайте бібліотеку Matplotlib. На круговій діаграмі мають відображатися значення показників у відсотках, 
    # наприклад, відсоток дівчат та хлопців, які навчаються у певному класі, 
    # сектори діаграми повинні бути розфарбовані в різний колір, на діаграмі мають бути підписи.
    # Получаем названия деталей и их количество
    filename = 'details.json'

    with open(filename, 'r') as file:
        data: list = json.load(file)

    details_sums = {}  # суми деталей за всі дні
    for i in data:
        for k, v in i['details'].items():
            if k in details_sums:
                details_sums[k] += v
            else:
                details_sums[k] = v
    
    print(details_sums)

    labels = details_sums.keys()
    sizes = details_sums.values()

    # створення кругової діаграми
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # відтворення діаграми
    plt.show()

if __name__ == '__main__':
    main()