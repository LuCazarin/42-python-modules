#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    value_input: str = "25"
    print(f"Input data is '{value_input}'")
    try:
        temp = input_temperature(value_input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    value_input = "abc"
    print(f"Input data is '{value_input}'")
    try:

        temp = input_temperature(value_input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
    print("")
    print("All tests completed - program didn't crash!")
