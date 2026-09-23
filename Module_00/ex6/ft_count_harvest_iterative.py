def ft_count_harvest_iterative() -> None:
    days_count = int(input("Days until harvest: "))
    for day in range(1, days_count + 1):
        print(f"Day {day}")
    print("Harvest time!")
