from .GameStrategy import GameStrategy
from .CardFactory import CardFactory


class GameEngine:
    def __init__(self) -> None:
        self.turns_stimulated: int = 0
        self.strategy_used: str = ""
        self.total_damage: int = 0
        self.cards_created: int = 0

        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.strategy_used = strategy.__class__.__name__

        if factory.__class__.__name__ == "FantasyCardFactory":
            print("Configuring Fantasy Card Game...")
        else:
            print("Configuring Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        self.turns_stimulated += 1

        if self.strategy.get_strategy_name() == "AggressiveStrategy":
            print("\nSimulating aggressive turn...")
        else:
            print("\nSimulating turn...")

        hand = self.factory.create_themed_deck(9)
        self.cards_created += 9
        print("Hand:", {card.name: n for card, n in hand.items()}, "\n")

        battlefield = [
            self.factory.create_creature("enemy1 goblin"),
            self.factory.create_spell('Fireball'),
            self.factory.create_creature("player1 dragon")
        ]
        self.cards_created += 3

        turn_res = self.strategy.execute_turn(hand, battlefield)
        self.total_damage += turn_res['damage_dealt']

        return turn_res

    def get_engine_status(self) -> dict:
        return {
            'turns_stimulated': self.turns_stimulated,
            'strategy_used': self.strategy_used,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
