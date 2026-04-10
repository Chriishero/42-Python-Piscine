import importlib
import sys


def check_dependencies(dependencies: list[tuple[str, str]]) -> None:
    missing: list[str] = []
    print("Checking dependencies:")
    for pkg, msg in dependencies:
        try:
            module = importlib.import_module(pkg)
            print(f" [OK] {pkg} ({module.__version__}) - {msg} ready")
        except ImportError:
            print(f" [MISSING] {pkg} - {msg} not ready")
            missing.append(pkg)
    if missing:
        print(f"\nMissing packages {', '.join(missing)}")
        print("Install with pip:    pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        sys.exit(1)


def process_and_save(n: int, min: int, max: int,
                     filename: str = "matrix_analysis.png") -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print(f"Processing {n} data points...")
    X = np.linspace(min, max, n)
    y = np.sin(X) + 0.5 * np.cos(2 * X)
    df = pd.DataFrame({
        "X": X,
        "y": y
    })
    print("Generating visualization...")
    plt.figure()
    plt.plot(df["X"], df["y"], color='r')
    plt.savefig(filename)
    print("\nAnalysis complete")
    print(f"Results save to: {filename}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    dependencies = [("pandas", "Data manipulation"),
                    ("numpy", "Numerical computation"),
                    ("matplotlib", "Visualization")]
    check_dependencies(dependencies)
    print()
    process_and_save(0, 100, 1000)


if __name__ == "__main__":
    main()
