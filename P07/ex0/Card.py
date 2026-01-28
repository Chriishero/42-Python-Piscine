from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class CardTypes(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

        self.card_info = {
            'name': name,
            'cost': cost,
            'rarity': rarity
        }

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return self.card_info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana > self.cost:
            print(f"Testing sufficient mana ({available_mana} available):")
            print("Playing: True")
            return True
        print(f"Testing insufficient mana ({available_mana} available):")
        print("Playing: False")
        return False
