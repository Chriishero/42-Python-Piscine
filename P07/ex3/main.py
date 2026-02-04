from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")
    g_e = GameEngine()
    g_e.configure_engine(FantasyCardFactory(), AggressiveStrategy())
    g_e.simulate_turn()
    print(f"Game Report: {g_e.get_engine_status()}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
