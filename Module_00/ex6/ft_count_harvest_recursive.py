def ft_count_harvest_recursive() -> None:
    days_count = int(input("Days until harvest: "))
    helper_function(days_count)
    print("Harvest time!")


def helper_function(current: int) -> None:
    if current > 0:
        helper_function(current - 1)
        print(f"Day {current}")
