def secure_archive(
        file_name: str, mode: str = "r",
        content: str | None = None
        ) -> tuple[bool, str | None]:
    success: bool = True
    try:
        with open(file_name, mode) as file:
            if content and mode == "r":
                file.write(content)
                content = "Content successfully written to file"
            elif mode == "w":
                content = file.read()
            else:
                raise ValueError(
                    f"Invalid mode '{mode}'.\n" +
                    "Valid options are: 'r' or 'w'"
                )
    except Exception as error:
        content = str(error)
        success = False
    return (success, content)


def main() -> None:
    success: bool
    content: str | None

    print("=== Cyber Archives Security ===")

    try:
        print("\nUsing 'secure_archive' to read from a nonexistent file:")
        print(secure_archive("/not/existing/file"))

        print("\nUsing 'secure_archive' to read from an inaccessible file:")
        print(secure_archive("/etc/shadow"))

        print("\nUsing 'secure_archive' to read from a directory:")
        print(secure_archive("/etc"))

        print("\nUsing 'secure_archive' to read from a regular file:")
        (success, content) = secure_archive("file")
        print((success, content))

        print("\nUsing 'secure_archive'",
              "to write previous content to a new file:")
        print(secure_archive("new_file", "w", content))
    except ValueError as e:
        print("[Error] -", e)


if __name__ == "__main__":
    main()
