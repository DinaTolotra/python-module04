from typing import IO
from sys import argv


def try_get_file(file_name: str, mode: str = "r") -> IO[str] | None:
    file: IO[str] | None = None
    try:
        file = open(file_name, mode)
    except Exception as error:
        print(f"Error opening file '{file_name}':", error)
    return file


def print_file_content(file: IO[str], suffix: str = "") -> None:
    print("---\n")
    for line in file:
        print(line[:-1] + suffix)
    print("\n---")


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
            dst.close()


def recovery(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    if file:
        print(f"Accessing file '{file_name}'")
        print_file_content(file)
        file.close()
        print(f"File '{file_name}' closed.")


def preserv(file_name: str) -> None:
    file: IO[str] | None = try_get_file(file_name)
    new_file_name: str = ""
    if file:
        print("\nTransform data:")
        print_file_content(file, "#")
        new_file_name = input("Enter new file name (or empty): ")
        if new_file_name != "":
            copy_file(file_name, new_file_name)
        else:
            print("Not saving data.")
        file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(argv) == 2:
        file_name: str = argv[1]
        recovery(file_name)
        preserv(file_name)
    else:
        print("Usage: ft_ancient_text.py <file>")
