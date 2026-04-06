
import sys
import typing


def add_archive_char(content: str, archive_char: str) -> str:
    lines = content.splitlines()
    new_lines = [line + archive_char for line in lines]
    return '\n'.join(new_lines) + ('\n' if content.endswith('\n') else '')


def main() -> None:
    argv = sys.argv[1:]
    if len(argv) != 1:
        print("Usage: ft_stream_management.py <file>")
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
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file_name = sys.stdin.readline().strip()
        if new_file_name:
            print(f"Saving data to '{new_file_name}'")
            try:
                fw: typing.IO[str] = open(new_file_name, "w")
                fw.write(new_content)
                fw.close()
                print(f"Data saved in file '{new_file_name}'.")
            except Exception as e:
                print(f"[STDERR] Error opening file '{new_file_name}': {e}",
                      file=sys.stderr)
                print("Data not saved.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{arg}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
