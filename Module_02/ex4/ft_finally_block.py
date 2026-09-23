#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    vegetables = ["Tomato", "Lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for vegetable in vegetables:
            water_plant(vegetable)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    list2_vegetables: list[str] = ["Tomato", "lettuce"]
    try:
        print("Opening watering system")
        for vegetable in list2_vegetables:
            water_plant(vegetable)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
