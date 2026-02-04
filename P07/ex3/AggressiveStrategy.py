from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        super().__init__()

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print("Turn execution:")
        print(f"Strategy: {self.get_strategy_name()}")
        targets = self.prioritize_targets({
            'player': [card for card in battlefield if 'player' in card.name],
            'enemy': [card for card in battlefield if 'enemy' in card.name],
            'spell': [card for card in battlefield if 'spell' in card.name],
            'artifact': [card for card in battlefield
                         if 'artifact' in card.name]
        })
        res = {
            'cards_played': [card.name for card, n in hand.items()],
            'mana_used': sum([card.cost for card in hand]),
            'targets_attacked': [card.name for card in targets],
            'damage_dealt': sum([card.cost for card in hand]) * 2
        }
        print(f"Actions: {res}\n")

        return res

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: dict) -> list:
        res = []

        for name, value in available_targets.items():
            if "player" in name or "creature" in name:
                for card in value:
                    res.append(card)

        return res
