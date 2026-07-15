from typing import IO
from sys import argv


def try_get_file(file_name: str, mode: str = "r") -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name, mode=mode)
    except FileNotFoundError:
        print(f"[Error] - file not found '{file_name}'")
    except PermissionError:
        print(f"[Error] - permission denied '{file_name}'")
    except IsADirectoryError:
        print(f"[Error] - is a directory '{file_name}'")
    except Exception as error:
        print(f"[Error] - failed to open file '{file_name}':", error)
    return file


def add_suffix(content: str, suffix: str) -> str:
    return f"{suffix}\n".join(content.split("\n")) + suffix


def print_content(content: str) -> None:
    print("=== BEGIN ===")
    print(content)
    print("==== END ====")


def recovery(file_name: str) -> str | None:
    file: IO[str] | None = try_get_file(file_name)
    content: str | None = None
    if file:
        print(f"[LOG] - Reading file '{file_name}'")
        content = file.read()
        print_content(content)
        print(f"\n[LOG] - Closing file '{file_name}'")
        file.close()
        print(f"[LOG] - File '{file_name}' closed")
    else:
        print("[LOG] - Aborted")

    return content


def preserv(content: str) -> None:
    new_file_name: str | None
    new_file: IO[str] | None
    new_content: str
    print("\n[LOG] - Transforming data")
    new_content = add_suffix(content, "#")
    print_content(new_content)
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
            print("[LOG] - Aborted")
    else:
        print("\n[LOG] - Not saving data")


def main() -> None:
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


if __name__ == "__main__":
    main()
