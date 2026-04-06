
import sys


def discard_redundant(argv: list[str]) -> list[str]:
    items = argv.copy()
    for i in range(len(argv)):
        for j in range(i + 1, len(argv)):
            if argv[i].split(':')[0] == argv[j].split(':')[0]:
                redundant = argv[i].split(':')[0]
                print(f"Redundant item '{redundant}' - discarding")
                items.remove(argv[j])
    return items


def discard_invalid(items: list[str]) -> list[str]:
    items_new = items.copy()
    for item in items:
        try:
            key, value = tuple(item.split(":"))
        except ValueError:
            print(f"Error - invalid parameter '{item}'")
            items_new.remove(item)
        else:
            try:
                int(value)
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
                items_new.remove(item)
    return items_new


def get_inventory(items: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for item in items:
        key, value = tuple(item.split(":"))
        inventory[key] = int(value)
    return inventory


def main() -> None:
    argv = sys.argv[1:]
    inventory = {}
    print("=== Inventory System Analysis ===")
    items = discard_redundant(argv)
    items = discard_invalid(items)
    inventory = get_inventory(items)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    n_items = len(inventory)
    total_items_quantity = sum(list(inventory.values()))
    print(f"Total quantity of the {n_items} items: {total_items_quantity}")
    most_abundant = None
    least_abundant = None
    for item, quantity in inventory.items():
        print(f"Item {item} represents "
              f"{round(quantity / total_items_quantity * 100, 1)}%")
        if most_abundant is None or inventory[most_abundant] < quantity:
            most_abundant = item
        if least_abundant is None or inventory[least_abundant] > quantity:
            least_abundant = item
    if most_abundant is not None and least_abundant is not None:
        print(f"Item most abundant: {most_abundant} "
              f"with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} "
              f"with quantity {inventory[least_abundant]}")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
