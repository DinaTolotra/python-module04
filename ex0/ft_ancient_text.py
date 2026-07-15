from typing import IO
from sys import argv


def try_get_file(file_name: str) -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name, encoding="utf-8")
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
    success: bool = False
    try:
        content = file.read()
        print("=== BEGIN ===")
        print(content)
        print("==== END ====")
        success = True
    except UnicodeDecodeError:
        print("[Error] - invalid file encoding")
    except Exception as error:
        print("[Error] - failed to read file:", error)
    return success


def recover(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    if file is not None:
        print(f"[Log] - Accessing file '{file_name}'\n")
        if not print_file_content(file):
            print(f"[Error] - failed to read file '{file_name}'")
        print(f"\n[Log] - closing file '{file_name}'...")
        file.close()
        print(f"[Log] - File '{file_name}' closed.")


def main() -> None:
    file_name: str = ""
    print("=== Cyber Archives Recovery ===\n")
    if len(argv) == 2:
        file_name = argv[1]
        recover(file_name)
    else:
        print("Usage: python ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
