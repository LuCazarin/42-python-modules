#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    arguments: list[str] = sys.argv[1:]
    print(f"Program name: {sys.argv[0]}")

    i: int = 1
    if len(arguments) != 0:
        print(f"Arguments received: {len(arguments)}")
        for arg in arguments:
            print(f"Argument {i}: {arg}")
            i += 1
    else:
        print("No arguments provided!")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
