import importlib
import sys


def check_dependencies(packages: list) -> dict:
    imported = {}

    for pkg in packages:
        try:
            imported[pkg] = importlib.import_module(pkg)
        except ImportError:
            print(f"Error: the package '{pkg}' is not installed.\n"
                  "Try,\n"
                  "pip install -r requirements.txt\n"
                  "or\n"
                  "poetry install")
            sys.exit(1)
    return imported


def process_data(min: int, max: int, n: int, modules: dict) -> None:
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = importlib.import_module("matplotlib.pyplot")
    filename = "_analysis.png"

    print("\nAnalyzing Matrix data...")
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


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")

    modules = check_dependencies(["numpy", "pandas", "matplotlib", "requests"])

    for name, module in modules.items():
        print(f"[OK] {name} ({module.__version__}) - ready")

    process_data(0, 20, 1000, modules)
