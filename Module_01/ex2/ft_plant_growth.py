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
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()
    growth: float = rose.height - 25.0
    print(f"Growth this week: {growth:.1f}cm")
