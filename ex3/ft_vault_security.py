def secure_archive(file_name: str, mode: str = "r",
                   content: str | None = None) -> (True | False, str):
    success: bool = True
    try:
        with open(file_name, mode) as file:
            if content:
                file.write(content)
                content = "Content successfully written to file"
            else:
                content = file.read()
    except Exception as error:
        content = error
        success = False
    finally:
        return (success, content)


if __name__ == "__main__":
    success: bool
    content: str

    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    (success, content) = secure_archive("file")
    print((success, content))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", "w", content))
