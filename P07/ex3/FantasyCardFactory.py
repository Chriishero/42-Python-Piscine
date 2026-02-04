from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        card_res = None

        try:
            if "dragon" in name_or_power or "Dragon" in name_or_power:
                card_res = CreatureCard(name_or_power, 6, "Legendary", 5, 6)
            elif "goblin" in name_or_power or "Goblin" in name_or_power:
                card_res = CreatureCard(name_or_power, 4, "Rare", 4, 5)
            for value in self.get_supported_types()['creatures']:
                if type(name_or_power) is int:
                    if value in name_or_power:
                        card_res = CreatureCard('Creature', name_or_power,
                                                "Common", 3, 4)
                else:
                    if value in name_or_power.lower():
                        card_res = CreatureCard(name_or_power, 3,
                                                "Common", 3, 4)
        except Exception as e:
            print(f"An error occured: {e}")

        return card_res

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        card_res = None

        try:
            if "fireball" in name_or_power or "Fireball" in name_or_power:
                card_res = SpellCard(name_or_power, 6, 'Rare', 'damage')
            for value in self.get_supported_types()['spells']:
                if type(name_or_power) is int:
                    if value in name_or_power:
                        card_res = SpellCard('Spell', name_or_power,
                                             "Common", 'damage')
                else:
                    if value in name_or_power.lower():
                        card_res = SpellCard(name_or_power, 3,
                                             "Common", 'damage')
        except Exception as e:
            print(f"An error occured: {e}")

        return card_res

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        card = None

        try:
            if name_or_power == "mana_ring":
                card = ArtifactCard(name_or_power, 6, 'Rare',
                                    9, 'Permanent: +1 mana per turn')
            for value in self.get_supported_types()['artifacts']:
                if type(name_or_power) is int:
                    if value in name_or_power:
                        card = ArtifactCard('Spell', name_or_power,
                                            "Common", 4, 'damage')
                else:
                    if value in name_or_power.lower():
                        card = ArtifactCard(name_or_power, 3,
                                            "Common", 4, 'damage')
        except Exception as e:
            print(f"An error occured: {e}")

        return card

    def create_themed_deck(self, size: int) -> dict:
        n_dragon = size // 4
        size -= size // 4
        n_goblin = size // 4
        size -= size // 4

        res = {
            self.create_creature("Fire Dragon"): n_dragon,
            self.create_creature("Goblin Warrior"): n_goblin,
            self.create_spell("Fireball"): size
        }

        return res

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
