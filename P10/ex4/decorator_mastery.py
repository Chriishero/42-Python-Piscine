from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get('power',
                               args[1] if len(args) > 1
                               and hasattr(args[0], '__dict__')
                               else args[0])
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attemps"
        return wrapper
    return decorator


@retry_spell(max_attempts=3)
@power_validator(min_power=50)
@spell_timer
def fireball(power: int) -> str:
    time.sleep(0.1)
    if power > 100:
        raise ValueError(
            f"Failed to cast a fireball with {power} power"
        )
    return f"Fireball cast at {power} power!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(fireball(100))
    print()

    print("Testing power validator...")
    print(fireball(49))
    print()

    print("Testing retrying spell...")
    print(fireball(1000))
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Bobby oui"))
    print(guild.validate_mage_name("Bob5678f 90fpdsa"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(8, "Lightning"))


if __name__ == "__main__":
    main()
