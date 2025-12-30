
def water_plants(plant_list):
    """
    Water all plant of plant_list.

    :param plant_list: plant list
    """
    print("Open watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the watering system on many plant list.
    """
    plant_list1 = ["Tomato", "Onion", "Banana tree"]
    plant_list2 = ["Apple tree", None, 1]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list1)
    print("\nTesting with error...")
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
