from . import elements


def healing_potion():
    return ("Healing potion brewed with "
            f"{elements.create_fire()} "
            f"and {elements.create_water()}")


def strength_potion():
    return ("Strength potion brewed with "
            f"{elements.create_earth()} "
            f"and {elements.create_fire()}")


def invisibility_potion():
    return ("Invisibility potion brewed with "
            f"{elements.create_earth()} "
            f"and {elements.create_water()}")


def wisdom_potion():
    return ("Wisdom potion brewed with all elements: "
            f"{elements.create_fire()}, {elements.create_water()}, "
            f"{elements.create_earth()}, "
            f"{elements.create_earth()}")
