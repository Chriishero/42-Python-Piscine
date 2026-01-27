import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")

    print("\nTesting package-level accesss (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except Exception as e:
        print(f"alchemy.create_fire(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except Exception as e:
        print(f"alchemy.create_water(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except Exception as e:
        print(f"alchemy.create_earth(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except Exception as e:
        print(f"alchemy.create_air(): {e.__class__.__name__} - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
