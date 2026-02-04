from .TournamentCard import TournamentCard
from typing import Dict
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.status = True
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        i = 0
        while True:
            if f"{card.name}_{i}" not in self.cards:
                break
            i += 1
        self.cards[f"{card.name}_{i}"] = card

        return (f"{card.name} (ID: {card.name}_{i}):\n"
                f"- Interfaces: {[cls.__name__
                                  for cls in card.__class__.__bases__]}\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.wins}-{card.losses}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        print("Creating tournament match...")
        self.matches_played += 1
        if random.randint(0, 1) == 1:
            winner = card1_id
            loser = card2_id
        else:
            winner = card2_id
            loser = card1_id
        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)

        return {
            'winner': winner,
            'loser': loser,
            'winner_rating': self.cards[winner].rating,
            'loser_rating': self.cards[loser].rating
        }

    def get_leaderboard(self) -> list:
        res = []
        max_rate = 0
        best_card = None

        while True:
            for _, card in self.cards.items():
                if card.rating > max_rate and card not in res:
                    max_rate = card.rating
                    best_card = card
            if best_card is None:
                break
            res.append(best_card)
            best_card = None
            max_rate = 0

        return res

    def generate_tournament_report(self) -> dict:
        rates = [card.rating for _, card in self.cards.items()]

        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': sum(rates) / len(rates),
            'platform_status': self.status
        }
