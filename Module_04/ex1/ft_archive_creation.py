#!/usr/bin/env python3
import sys


def archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    content: str = ""

    try:
        file_obj = open(filename, "r")
        content = file_obj.read()

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
        return

    print("\nTransform data:")
    print("---")

    lines: list[str] = content.splitlines()

    transformed_lines: list[str] = [f"{line}#" for line in lines]

    transformed_content: str = "\n".join(transformed_lines)
    if transformed_content:
        transformed_content += "\n"

    if transformed_content.endswith("\n"):
        print(transformed_content, end="")
    else:
        print(transformed_content)
    print("---")

    try:
        new_filename: str = input("Enter new file name (or empty): ").strip()

        if not new_filename:
            print("Not saving data.")
            return

        print(f"Saving data to '{new_filename}'")

        out_file = open(new_filename, "w")

        out_file.write(transformed_content)

        out_file.close()

        print(f"Data saved in file '{new_filename}'.")

    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    archive_creation()
