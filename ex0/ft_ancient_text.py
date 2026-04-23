from typing import IO
from sys import argv


def try_get_file(file_name: str) -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name)
    except Exception as error:
        print(f"Error opening file '{file_name}':", error)
    finally:
        return file


def print_file_content(file: IO[str]) -> None:
    content: str = file.read()
    print("---\n")
    print(content)
    print("---")


def recover(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    if file:
        print(f"Accessing file '{file_name}'")
        print_file_content(file)
        file.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(argv) == 2:
        recover(argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
