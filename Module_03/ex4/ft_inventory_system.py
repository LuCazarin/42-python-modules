#!/usr/bin/env python3
import sys


def analyze_inventory() -> None:

    args: list[str] = sys.argv[1:]

    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    for arg in args:
        parts: list[str] = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = parts[0].strip()
        quantity_str = parts[1].strip()

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

    print(f"Got inventory: {inventory}")

    item_keys = list(inventory.keys())
    print(f"Item list: {item_keys}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant_item = ""
    most_abundant_qty = -1
    least_abundant_item = ""
    least_abundant_qty = float('inf')

    for item, qty in inventory.items():
        if qty > most_abundant_qty:
            most_abundant_qty = qty
            most_abundant_item = item
        if qty < least_abundant_qty:
            least_abundant_qty = qty
            least_abundant_item = item

    print(f"Item most abundant: {most_abundant_item} "
          f"with quantity {most_abundant_qty}")
    print(f"Item least abundant: {least_abundant_item} "
          f"with quantity {least_abundant_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    analyze_inventory()
