#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, grow_add: float) -> None:
        if grow_add > 0:
            self.set_height(self._height + grow_add)

    def age(self, age_add: int) -> None:
        if age_add > 0:
            self.set_age(self._age + age_add)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    print("")
    rose.set_height(-25)
    rose.set_age(-30)
    print("")
    print("Current state: ", end="")
    rose.show()
