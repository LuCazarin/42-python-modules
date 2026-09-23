#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self, grow_add: float) -> None:
        self.height += grow_add

    def age(self, age_add: int) -> None:
        self._age += age_add


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
