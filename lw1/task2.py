
def main():
    distance = 10
    days = 1

    while distance < 50:
        print(f'Day {days}: {round(distance, 3)} km')
        distance += distance + distance * 0.1
        days += 1
    
    print(f'Answer: {days} days (distance: {round(distance, 3)} km)')

if __name__ == "__main__":
    main()
    