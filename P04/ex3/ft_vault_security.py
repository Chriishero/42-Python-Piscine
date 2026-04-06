
def secure_archive(
    file_name: str,
    action: str,
    content: str
) -> tuple[bool, str]:
    try:
        with open(file_name, action) as f:
            if action == 'r':
                content = f.read()
                return (True, content)
            elif action == 'w':
                f.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, str(e))
    return (False, "")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r', ""))
    print()

    print("Using 'secure_archive' to read from a inaccessible file:")
    print(secure_archive("/etc/shadow", 'r', ""))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    archive = secure_archive("../ex0/ft_ancient_text.py", 'r', "")
    print(archive)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", 'w', archive[1]))


if __name__ == "__main__":
    main()
