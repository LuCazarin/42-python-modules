#!/usr/bin/env python3
import sys


def stream_management() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return

    print("\nTransform data:")
    print("---")

    lines = content.splitlines()
    transformed_lines = [f"{line}#" for line in lines]
    transformed_content = "\n".join(transformed_lines)
    if transformed_content:
        transformed_content += "\n"

    if transformed_content.endswith("\n"):
        print(transformed_content, end="")
    else:
        print(transformed_content)
    print("---")

    new_filename: str = ""
    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        line_input = sys.stdin.readline()
        if not line_input:
            print("Not saving data.")
            return

        new_filename = line_input.strip()

        if not new_filename:
            print("Not saving data.")
            return

        print(f"Saving data to '{new_filename}'")

        out_file = open(new_filename, "w")
        out_file.write(transformed_content)
        out_file.close()

        print(f"Data saved in file '{new_filename}'.")

    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_filename}': {e}\n"
        )
        print("Data not saved.")


if __name__ == "__main__":
    stream_management()
