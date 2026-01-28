from ex0.Card import Card
from ex0.Card import CardTypes
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

        self.type = CardTypes.ARTIFACT

    def play(self, game_state: Dict) -> Dict:
        if 'card_played' in game_state:
            print(f"Playing {game_state['card_played']}:")
            if ('available_mana' in game_state and
                    self.is_playable(game_state['available_mana'])):
                game_state['mana_used'] = self.cost
                game_state['available_mana'] -= self.cost
                self.durability -= 1

        return game_state

    def activate_ability(self) -> Dict:
        if self.durability > 0:
            print(f"Ability of {self.name} has been destroyed")
            return {
                'card_played': self.name,
                'available_mana': 0,
                'effect': None
            }
        return {
                'card_played': self.name,
                'available_mana': self.cost,
                'effect': self.effect
            }
