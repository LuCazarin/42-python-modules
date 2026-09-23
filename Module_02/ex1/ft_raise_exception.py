#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===", end=("\n\n"))
    for value_input in tests:
        print(f"Input data is '{value_input}'")
        try:
            temp = input_temperature(value_input)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
