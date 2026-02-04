import sys


def get_base_prefix():
    return (
        getattr(sys, "base_prefix", None)
        or getattr(sys, "real_prefix", None)
        or sys.prefix
    )


def in_venv():
    return sys.prefix != get_base_prefix()


if __name__ == "__main__":
    curr_python = sys.executable

    if in_venv() is False:
        print("\nMATRIX STATUS: You're still plugged in\n\n"
              f"Current Python: {curr_python}\n"
              "VIrtual Environment: None detected\n\n"
              "WARNING: You're in the global envionment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate # On Windows\n\n"
              "Then run this program again.")
    else:
        environment_path = sys.prefix
        site_packages = curr_python[4]
        print("\nMATRIX STATUS: Welcome to the construct\n\n"
              f"Current Python: {curr_python}\n"
              "Virtual Environment: matrix_env\n"
              f"Environment Path: {environment_path}\n\n"
              "SUCCESS: You're in an isolated envionment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n\n"
              "Package installation path:\n"
              f"{site_packages}")
