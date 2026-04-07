from elements import create_air
from ..elements import create_fire
from potions import healing_potion, strength_potion


def lead_to_gold() -> str:
    return ("Recipes transmuting Lead to Gold: brew "
            f"'{create_air()}' and '{strength_potion}' "
            f"mixed with '{create_fire()}'")
