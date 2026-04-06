
import sys
import typing


def add_archive_char(content: str, archive_char: str) -> str:
    lines = content.splitlines()
    new_lines = [line + archive_char for line in lines]
    return '\n'.join(new_lines) + ('\n' if content.endswith('\n') else '')


def main() -> None:
    argv = sys.argv[1:]
    if len(argv) != 1:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    arg = argv[0]
    print(f"Accessing file '{arg}'")
    try:
        f: typing.IO[str] = open(arg, "r")
        content = f.read()
        print("---")
        print(content, end="")
        print("---")
        f.close()
        print(f"File '{arg}' closed.")
        print("Transform data:")
        new_content = add_archive_char(content, '#')
        print("---")
        print(new_content, end="")
        print("---")
        new_file_name = input("Enter new file name (or empty): ")
        if new_file_name.strip():
            print(f"Saving data to '{new_file_name}'")
            f = open(new_file_name, "w")
            f.write(new_content)
            f.close()
            print(f"Data saved in file '{new_file_name}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"Error opening file '{arg}': {e}")


if __name__ == "__main__":
    main()
