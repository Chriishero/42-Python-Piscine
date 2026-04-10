from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heals restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with a power of {power}"


def callable_condition(target: str, power: int) -> bool:
    if target in ("Dragon", "Gobelin"):
        if power > 50:
            return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon", 10)
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")
    conditional = conditional_caster(callable_condition, heal)
    print(conditional("Dragon", 89))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([heal, fireball])
    print(sequence("Gobelin", 60))


if __name__ == "__main__":
    main()
