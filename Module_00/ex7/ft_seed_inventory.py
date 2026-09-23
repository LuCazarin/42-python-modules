def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_capitalize = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type_capitalize} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type_capitalize} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type_capitalize} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
