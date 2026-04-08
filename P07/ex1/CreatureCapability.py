from ex0.Creature import Creature
from ex1.Capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Wine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed is True:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.tranformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.tranformed = False
        return f"{self.name} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed is True:
            return f"{self.name} ubnleashes a devastating morph strike!"
        return f"{self.name} attacks normally!"

    def transform(self) -> str:
        self.tranformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.tranformed = False
        return f"{self.name} stabilizes its form"
