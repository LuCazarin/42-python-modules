#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def increment_grow(self) -> None:
            self.grow_calls += 1

        def increment_age(self) -> None:
            self.age_calls += 1

        def increment_show(self) -> None:
            self.show_calls += 1

        def display(self) -> None:
            """Exibe as estatísticas básicas de qualquer planta."""
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)
        self.stats: Plant.Stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self.stats.increment_show()

    def grow(self, grow_add: float) -> None:
        if grow_add > 0:
            self.set_height(self._height + grow_add)
            self.stats.increment_grow()

    def age(self, age_add: int) -> None:
        if age_add > 0:
            self.set_age(self._age + age_add)
            self.stats.increment_age()

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

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls: int = 0

        def increment_shade(self) -> None:
            self.shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        stats = self.stats
        if isinstance(stats, Tree.Stats):
            stats.increment_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, grow_add: float) -> None:
        if grow_add > 0:
            super().grow(grow_add)
            self.nutritional_value += 1

    def age(self, age_add: int) -> None:
        if age_add > 0:
            super().age(age_add)
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.age(20)
    sunflower.grow(30)
    sunflower.show()
    display_plant_stats(sunflower)
    print("")
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)
