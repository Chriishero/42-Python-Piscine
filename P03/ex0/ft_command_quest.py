
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    print("=== Command Quest ===")
    if argc == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {argv[i]}")
    print(f"Total arguments: {argc}\n")
