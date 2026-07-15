from typing import IO
from sys import argv


def try_get_file(file_name: str, mode: str = "r") -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name, mode=mode)
    except FileNotFoundError:
        print(f"[Error] - file not found '{file_name}'")
    except PermissionError:
        print(f"[Error] - unreadable file '{file_name}'")
    except IsADirectoryError:
        print(f"[Error] - is a directory '{file_name}'")
    except Exception as error:
        print(f"[Error] - failed to open file '{file_name}':", error)
    return file


def print_content(content: str, suffix: str = "") -> str:
    new_content: str = content
    if suffix != "":
        new_content = content.replace("\n", suffix + "\n")
    print("=== BEGIN")
    print(new_content)
    print("=== END")
    return new_content


def recovery(file_name: str) -> str | None:
    file: IO[str] | None = try_get_file(file_name)
    content: str | None = None
    if file:
        print(f"[LOG] - Reading file '{file_name}'")
        content = print_content(file.read())
        print(f"\n[LOG] - Closing file '{file_name}'")
        file.close()
        print(f"[LOG] - File '{file_name}' closed")
    return content


def preserv(content: str) -> None:
    new_file_name: str | None
    new_file: IO[str] | None
    new_content: str
    print("\n[LOG] - Transforming data")
    new_content = print_content(content, "#")
    try:
        new_file_name = input("\nEnter new file name (or empty): ")
    except BaseException:
        new_file_name = None
    if new_file_name:
        print(f"\n[LOG] - Saving data to '{new_file_name}'")
        new_file = try_get_file(new_file_name, "w")
        if new_file:
            new_file.write(new_content)
            print(f"[LOG] - Data saved in file '{new_file_name}'")
            print(f"\n[LOG] - Closing file '{new_file_name}'")
            new_file.close()
            print(f"[LOG] - File '{new_file_name}' closed")
    else:
        print("\n[LOG] - Not saving data")


if __name__ == "__main__":
    content: str | None
    file_name: str
    print("=== Cyber Archives Recovery & Preservation ===\n")
    if len(argv) == 2:
        file_name = argv[1]
        content = recovery(file_name)
        if content:
            preserv(content)
    else:
        print("Usage: python ft_archive_creation.py <file>")
