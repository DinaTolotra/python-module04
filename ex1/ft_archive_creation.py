from typing import IO
from sys import argv

# TODO: used function verification


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


def print_file_content(file: IO[str], suffix: str = "") -> None:
    print("=== BEGIN")
    for line in file:
        print(line[:-1] + suffix)
    print("=== END")


def copy_file(src_name: str, dst_name: str) -> None:
    new_content: str = ""
    dst: IO[str] | None = None
    src: IO[str] | None = try_get_file(src_name)
    if src:
        for line in src:
            new_content += line[:-1] + "#" + "\n"
        src.close()
        dst = try_get_file(dst_name, "w")
        if dst:
            dst.write(new_content)
            print(f"[LOG] - Data saved in file '{dst_name}'")
            print(f"\n[LOG] - Closing file '{dst_name}'")
            dst.close()
            print(f"[LOG] - File '{dst_name}' closed")


def recovery(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    if file:
        print(f"[LOG] - Reading file '{file_name}'")
        print_file_content(file)
        print(f"\n[LOG] - Closing file '{file_name}'")
        file.close()
        print(f"[LOG] - File '{file_name}' closed")


def preserv(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    new_file_name: str = ""
    if file:
        print("\n[LOG] - Transforming data")
        print_file_content(file, "#")
        print("\nEnter new file name (or empty): ", end="")
        try:
            new_file_name = input()
        except BaseException:
            pass
        if new_file_name != "":
            print(f"\n[LOG] - Saving data to '{new_file_name}'")
            copy_file(file_name, new_file_name)
        else:
            print("\n[LOG] - Not saving data")
        file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===\n")
    if len(argv) == 2:
        file_name: str = argv[1]
        recovery(file_name)
        preserv(file_name)
    else:
        print("Usage: python ft_archive_creation.py <file>")
