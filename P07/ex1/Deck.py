from ex0.Card import Card
from ex0.Card import CardTypes
from typing import Dict, List
import random


class Deck:
    def __init__(self):
        self.deck: List[Card] = []
        self.deck_stats = {
            'total_cards': 0,
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0
        }

    def add_card(self, card: Card) -> None:
        self.deck.append(card)
        self.deck_stats['total_cards'] += 1

        if card.type == CardTypes.CREATURE:
            self.deck_stats['creatures'] += 1
        elif card.type == CardTypes.SPELL:
            self.deck_stats['spells'] += 1
        elif card.type == CardTypes.ARTIFACT:
            self.deck_stats['artifacts'] += 1

        cost_sum = 0
        n_cards = 0
        for c in self.deck:
            cost_sum += c.cost
            n_cards += 1
        self.deck_stats['avg_cost'] = f"{(cost_sum / n_cards):.1f}"

    def remove_card(self, card_name: str) -> None:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        card = self.deck[0]
        self.deck.remove(card)
        print(f"Drew: {card.name} ({card.type.value})")

        return card

    def get_deck_stats(self) -> Dict:
        return self.deck_stats
