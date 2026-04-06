
import sys
import typing


def main() -> None:
    argv = sys.argv[1:]
    if len(argv) != 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
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
    except Exception as e:
        print(f"Error opening file '{arg}': {e}")


if __name__ == "__main__":
    main()
