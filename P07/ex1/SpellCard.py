from ex0.Card import Card
from ex0.Card import CardTypes
from typing import Dict


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

        self.type = CardTypes.SPELL

    def play(self, game_state: Dict) -> Dict:
        if 'card_played' in game_state:
            print(f"Playing {game_state['card_played']}:")
            if ('available_mana' in game_state and
                    self.is_playable(game_state['available_mana'])):
                game_state['mana_used'] = self.cost
                game_state['available_mana'] -= self.cost
                game_state['effect'] = (f"Deal {self.cost} {self.effect_type} "
                                        "to target")
                self.effect_type = None

        return game_state

    def resolve_effect(self) -> Dict:
        if self.effect_type is None:
            print(f"Ability of {self.name} has already been consumed")
            return {
                'card_played': self.name,
                'available_mana': 0,
                'effect': None
            }
        return {
                'card_played': self.name,
                'available_mana': self.cost,
                'effect': self.effect_type
            }
