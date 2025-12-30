
def garden_operations():
    """
    Function that intentionally causes some errors
    """
    def op1(): int("abc"),
    def op2(): 10 / 0,
    def op3(): open("missing.txt"),
    def op4(): {"a": 1, "b": 2}["c"]
    return [op1, op2, op3, op4]


def test_error_types():
    """
    Test all types of errors on the function 'garden_operations()'
    """
    print("=== Garden Error Types ===\n")
    err_tuple = (ValueError, ZeroDivisionError, FileNotFoundError, KeyError)
    ops = garden_operations()
    for err, op in zip(err_tuple, ops):
        try:
            print(f"Testing {err.__name__}...")
            op()
        except err as e:
            print(f"Caught {type(e).__name__}: {e}\n")
    try:
        print("Testing multiple errors together...")
        for op in ops:
            op()
    except err_tuple:
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
