from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from typing import Dict, TypedDict


class GameState(TypedDict):
    attack_target: Card
    incoming_damage: int
    spell_name: str
    spell_targets: list
    amount_channeled_mana: int


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_point: int, defense_point: int, mana_point: int,
                 health: int, combat_type: str) -> None:
        super().__init__(name, cost, rarity)

        self.attack_point = attack_point
        self.defense_point = defense_point
        self.mana_point = mana_point
        self.health = health
        self.combat_type = combat_type

        self.total_mana_used = 0
        self.total_mana_channeled = 0

    def play(self, game_state: GameState) -> Dict:
        print(f"Playing {self.name} (Elite Card)\n")
        res = {}
        attack_res, defense_res, spell_res, channel_mana_res = (
            None, None, None, None
        )
        try:
            print("Combat phase:")
            attack_res = self.attack(game_state['attack_target'])
            print(f"Attack result: {attack_res}")
            defense_res = self.defend(game_state['incoming_damage'])
            print(f"Defense result: {defense_res}\n")

            print("Magic phase:")
            spell_res = self.cast_spell(game_state['spell_name'],
                                        game_state['spell_targets'])
            print(f"Spell cast: {spell_res}")
            channel_mana_res = self.channel_mana(
                game_state['amount_channeled_mana'])
            print(f"Mana channel: {channel_mana_res}")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            res = {
                'attack_res': attack_res,
                'defense_res': defense_res,
                'spell_res': spell_res,
                'channel_mana_res': channel_mana_res
            }

        return res

    def attack(self, target) -> Dict:
        target.health -= self.attack_point
        res = {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_point,
            'combat_type': self.combat_type
        }

        return res

    def defend(self, incoming_damage: int) -> Dict:
        incoming_damage -= self.defense_point
        self.health -= incoming_damage
        res = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense_point,
            'still_alive': self.health > 0
        }

        return res

    def get_combat_stats(self) -> Dict:
        res = {
            'attack_point': self.attack_point,
            'defense_point': self.defense_point,
            'combat_type': self.combat_type
        }

        return res

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        for target in targets:
            target.health -= 2
        mana_used = len(targets) * 2
        self.total_mana_used += mana_used
        res = {
            'caster': self.name,
            'spell': spell_name,
            'targets': [target.name for target in targets],
            'mana_used': mana_used
        }

        return res

    def channel_mana(self, amount: int) -> Dict:
        self.total_mana_channeled += amount
        self.mana_point += amount
        res = {
            'channeled': amount,
            'total_mana': self.mana_point
        }

        return res

    def get_magic_stats(self) -> Dict:
        res = {
            'total_mana': self.mana_point,
            'total_mana_used': self.total_mana_used,
            'total_mana_channeled': self.total_mana_channeled
        }

        return res
