from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} is enchanted with {element} element at power {power}!"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: b if b < a else a
    }
    if operation not in operations:
        raise ValueError(
            f"Unknown operation '{operation}'. "
            f"Choose from {list(operations.keys())}"
        )
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "ice": partial(base_enchantment, power=50, element="ice"),
        "lightning": partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells ({', '.join(spell)})"
    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    print("Sum:", spell_reducer([100, 20, 3, 1, 5, 6, 222], "add"))
    print("Product:", spell_reducer([100, 20, 3, 1, 5, 6, 222], "multiply"))
    print("Max:", spell_reducer([100, 20, 3, 1, 5, 6, 222], "max"))
    print()

    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"](target="Player1"))
    print(enchantments["ice"](target="Player1"))
    print(enchantments["lightning"](target="Player2"))
    print()

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print("Fib(50):", memoized_fibonacci(50))
    print(memoized_fibonacci.cache_info())
    print()

    print("Testing spell dispatcher...")
    cast_spell = spell_dispatcher()
    print(cast_spell("Fireball"))
    print(cast_spell(4))
    print(cast_spell(["Fireball", "Thunder strike"]))
    print(cast_spell(3.9))


if __name__ == "__main__":
    main()
