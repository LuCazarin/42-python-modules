#!/usr/bin/env python3


def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file_obj:
                data: str = file_obj.read()
            return True, data

        elif action == "write":
            with open(filename, "w") as file_obj:
                file_obj.write(content)
            return True, "Content successfully written to file"

        else:
            return False, f"Invalid action: '{action}'"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    res1: tuple[bool, str] = secure_archive("/not/existing/file", "read")
    print(res1)

    print("Using 'secure_archive' to read from an inaccessible file:")
    res2: tuple[bool, str] = secure_archive("/etc/master.passwd", "read")
    print(res2)

    sample_file: str = "ancient_fragment.txt"
    sample_content: str = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    try:
        with open(sample_file, "w") as f:
            f.write(sample_content)
    except Exception:
        pass

    print("Using 'secure_archive' to read from a regular file:")
    res3: tuple[bool, str] = secure_archive(sample_file, "read")
    print(res3)

    new_file: str = "secure_backup.txt"
    print(
        f"Using 'secure_archive' to write previous content to '{new_file}':"
    )
    if res3:
        res4: tuple[bool, str] = secure_archive(
            new_file, "write", content=res3[1]
        )
        print(res4)


if __name__ == "__main__":
    main()
