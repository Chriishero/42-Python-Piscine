from .Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_point: int, defense_point: int, mana_point: int,
                 health: int, combat_type: str) -> None:
        super().__init__(name, cost, rarity)

        self.attack_point = attack_point
        self.defense_point = defense_point
        self.mana_point = mana_point
        self.health = health
        self.combat_type = combat_type

        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1000

    def play(self, game_state: dict) -> dict:
        if 'card_played' in game_state:
            print(f"Playing {game_state['card_played']}:")
            if ('available_mana' in game_state and
                    self.is_playable(game_state['available_mana'])):
                game_state['mana_used'] = self.cost
                game_state['available_mana'] -= self.cost
                self.durability -= 1

        return game_state

    def attack(self, target) -> dict:
        target.health -= self.attack_point
        res = {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_point,
            'combat_type': self.combat_type
        }

        return res

    def defend(self, incoming_damage: int) -> dict:
        incoming_damage -= self.defense_point
        self.health -= incoming_damage
        res = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense_point,
            'still_alive': self.health > 0
        }

        return res

    def calculate_rating(self) -> int:
        self.rating += self.wins * 10 - self.losses * 5
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_combat_stats(self) -> dict:
        res = {
            'attack_point': self.attack_point,
            'defense_point': self.defense_point,
            'combat_type': self.combat_type
        }

        return res

    def get_rank_info(self) -> dict:
        return {
            'wins': self.wins,
            'losses': self.losses,
            'rank': self.rating
        }

    def get_tournament_stats(self) -> dict:
        return {
            'wins': self.wins,
            'lossses': self.losses,
            'rank': self.rating,
            'attack_point': self.attack_point,
            'defense_point': self.defense_point,
            'mana_point': self.mana_point,
            'health': self.health,
            'combat_type': self.combat_type
        }
