#!/usr/bin/env python3
import sys


def recover_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file_obj = open(filename, "r")

        content: str = file_obj.read()

        print("---")
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)

        file_obj.close()
        print("---")
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    recover_ancient_text()
