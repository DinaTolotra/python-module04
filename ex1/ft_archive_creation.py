from typing import IO
from sys import argv


def try_get_file(file_name: str, mode: str = "r") -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name, mode=mode, encoding="utf-8")
    except FileNotFoundError:
        print(f"[Error] - File not found '{file_name}'")
    except PermissionError:
        print(f"[Error] - Permission denied '{file_name}'")
    except IsADirectoryError:
        print(f"[Error] - Is a directory '{file_name}'")
    except Exception as error:
        print(f"[Error] - Failed to open file '{file_name}':", error)
    return file


def add_suffix(content: str, suffix: str) -> str:
    return "\n".join(line + suffix for line in content.splitlines())


def print_content(content: str) -> None:
    print("=== BEGIN ===")
    print(content)
    print("==== END ====")


def get_user_input(prompt: str) -> str | None:
    value: str | None = None
    try:
        value = input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n[Log] - Input interrupted")
    except Exception as e:
        print(f"[Error] - Failed to get user input: {e}")
    return value


def write_to_file(file_name: str, file: IO[str], content: str) -> None:
    try:
        file.write(content)
        print(f"[Log] - Data saved in file '{file_name}'")
    except Exception as error:
        print(f"[Error] - Failed to write to file '{file_name}':",
              error)
    finally:
        print(f"\n[Log] - Closing file '{file_name}'")
        file.close()
        print(f"[Log] - File '{file_name}' closed")


def read_file(file_name: str, file: IO[str]) -> str | None:
    content: str | None = None
    print(f"[Log] - Reading file '{file_name}'")
    try:
        content = file.read()
        print_content(content)
    except Exception as error:
        print(f"[Error] - Failed to read file '{file_name}':", error)
    finally:
        print(f"\n[Log] - Closing file '{file_name}'")
        file.close()
        print(f"[Log] - File '{file_name}' closed")
    return content


def recovery(file_name: str) -> str | None:
    file: IO[str] | None = try_get_file(file_name)
    content: str | None = None
    if file is not None:
        content = read_file(file_name, file)
    else:
        print("[Log] - Aborted")
    return content


def preserve(content: str) -> None:
    new_file_name: str | None
    new_file: IO[str] | None
    new_content: str
    print("\n[Log] - Transforming data")
    new_content = add_suffix(content, "#")
    print_content(new_content)
    new_file_name = get_user_input("\nEnter new file name (or empty): ")
    if new_file_name is not None and new_file_name != "":
        print(f"\n[Log] - Saving data to '{new_file_name}'")
        new_file = try_get_file(new_file_name, "w")
        if new_file is not None:
            write_to_file(new_file_name, new_file, new_content)
        else:
            print("[Log] - Aborted")
    else:
        print("\n[Log] - Not saving data")


def main() -> None:
    content: str | None
    file_name: str
    print("=== Cyber Archives Recovery & Preservation ===\n")
    if len(argv) == 2:
        file_name = argv[1]
        content = recovery(file_name)
        if content is not None:
            preserve(content)
    else:
        print("Usage: python ft_archive_creation.py <file>")


if __name__ == "__main__":
    main()
