#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:

    while True:

        try:
            user_input: str = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            coordinates: list[str] = user_input.split(",")
            if len(coordinates) != 3:
                print("Invalid syntax")
                continue
            x: float = float(coordinates[0].strip())
            y: float = float(coordinates[1].strip())
            z: float = float(coordinates[2].strip())
            return (x, y, z)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting coordinate system.")
            return (0.0, 0.0, 0.0)

        except ValueError:
            for item in coordinates:
                clean_item = item.strip()
                try:
                    float(clean_item)
                except ValueError as e:
                    print(f"Error on parameter '{clean_item}': {e}")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x1, y1, z1 = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist_to_center = math.sqrt((x1 - 0.0)**2 + (y1 - 0.0)**2 + (z1 - 0.0)**2)
    print(f"Distance to center: {round(dist_to_center, 4)}\n")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    dist_between = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")
