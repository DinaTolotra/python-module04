from typing import IO
from sys import argv


def try_get_file(file_name: str) -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name)
    except FileNotFoundError:
        print(f"[Error] - file not found '{file_name}'")
    except PermissionError:
        print(f"[Error] - permission denied '{file_name}'")
    except IsADirectoryError:
        print(f"[Error] - is a directory '{file_name}'")
    except Exception as error:
        print(f"[Error] - failed to open file '{file_name}':", error)
    return file


def print_file_content(file: IO[str]) -> bool:
    content: str = ""
    try:
        content = file.read()
        print("=== BEGIN ===")
        print(content)
        print("==== END ====")
        return True
    except UnicodeDecodeError:
        print("[Error] - invalid file encoding")
        return False


def recover(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    if file:
        print(f"[LOG] - Accessing file '{file_name}'\n")
        print_file_content(file)
        print(f"\n[Log] - closing file '{file_name}'...")
        file.close()
        print(f"[LOG] - File '{file_name}' closed.")


def main() -> None:
    print("=== Cyber Archives Recovery ===\n")
    if len(argv) == 2:
        recover(argv[1])
    else:
        print("Usage: python ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
