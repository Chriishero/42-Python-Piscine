from .Card import Card
from .Card import CardTypes
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

        self.type = CardTypes.CREATURE
        self.card_info = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'type': self.type,
            'attack': attack,
            'health': health
        }

    def play(self, game_state: Dict) -> Dict:
        if 'card_played' in game_state:
            print(f"Playing {game_state['card_played']}:")
            if ('available_mana' in game_state and
                    self.is_playable(game_state['available_mana'])):
                game_state['mana_used'] = self.cost
                game_state['available_mana'] -= self.cost
                if self.cost >= 5:
                    game_state['effect'] = ("Rare creature summoned "
                                            "to battlefield")
                elif self.cost >= 2:
                    game_state['effect'] = ("Common creature summoned "
                                            "to battlefield")
                else:
                    game_state['effect'] = "Nothing happened"

        return game_state

    def attack_target(self, target) -> Dict:
        combat_resolved = False
        damage_dealt = self.attack

        if self.attack > target.health:
            damage_dealt = target.health
            target.health = 0
            combat_resolved = True
        else:
            target.health -= self.attack

        print(f"{self.name} attacks {target.name}:")

        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': damage_dealt,
            'combat_resolved': combat_resolved
        }
