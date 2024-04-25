import csv
import matplotlib.pyplot as plt


def plot_time(data, years, countries):
    # 2.1 На одній координатній осі побудуйте графіки, що показують динаміку показника для двох країн,
    # підпишіть осі – по осі Х має відображатися рік, а по осі Y має відображатися значення показника.
    
    for country in countries:
        plt.plot(years, data[country], label=country)

    plt.xlabel('Year')
    plt.ylabel('Foreign direct investment, net inflows (% of GDP)')
    plt.title('Time Series of Foreign Direct Investment by Country')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_bar_chart(data, years, country):
    # 2.2 Побудуйте стовпчасті діаграми, які відображатимуть значення показника для кожної з країн. 
    # Назву країни для побудови діаграми має вводити користувач з клавіатури.

    plt.bar(years, data[country])
    plt.xlabel('Year')
    plt.ylabel('Foreign direct investment, net inflows (% of GDP)')
    plt.title(f'Foreign Direct Investment in {country}')
    plt.xticks(rotation=90)  # вертикальні стовбці
    plt.show()

def main():
    # https://databank.worldbank.org/home.aspx
    # World Development Indicators
    # Foreign direct investment, net inflows (% of GDP)
    
    file_path = 'ukraine_usa_invest_gdp.csv'

    data = {}
    years = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row["Country Name"]

            if not years:
                years = [year.split(' ')[0] for year in row if 'YR' in year]
            data[country] = [float(row[year]) for year in row if 'YR' in year]
    
    plot_time(data, years, ['Ukraine', 'United States'])
    plot_bar_chart(data, years, input('Enter country name: '))

if __name__ == "__main__":
    main()