from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def power_accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply(item_name: str) -> str:
        return ' '.join([enchantment_type, item_name])
    return apply


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}:", counter_a())
    counter_b = mage_counter()
    print("counter_b call 1:", counter_b())
    print()

    print("Testing spell accumulator...")
    base = 100
    accumulator = spell_accumulator(100)
    print(f"Base {base}, add 20:", accumulator(20))
    print(f"Base {base}, add 30:", accumulator(30))
    print()

    print("Testing enchantment factory...")
    enchantment_a = enchantment_factory("Flaming")
    enchantment_b = enchantment_factory("Frozen")
    print(enchantment_a("Sword"))
    print(enchantment_b("Shield"))
    print()

    print("Testing memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory["store"]("secret", 42)
    print("Recall 'secret':", memory["recall"]("secret"))
    print("Recall 'unknown':", memory["recall"]("unknown"))


if __name__ == "__main__":
    main()
