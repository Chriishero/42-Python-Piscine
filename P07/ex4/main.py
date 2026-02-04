from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    platform = TournamentPlatform()
    print(platform.register_card(TournamentCard("Fire Dragon", 4,
                                                "Legendary", 4,
                                                4, 3,
                                                5, 'melee')))
    print(platform.register_card(TournamentCard("Ice Wizard", 5,
                                                "Legendary", 3,
                                                4, 3,
                                                4, 'distance')))
    print(platform.create_match("Fire Dragon_0", "Ice Wizard_0"))

    print("\nTournament Leaderboard:")
    leaderboard = [card for card in platform.get_leaderboard()]
    for i in range(1, len(leaderboard) + 1):
        print(f"{i}. {leaderboard[i - 1].name} - "
              f"Rating: {leaderboard[i - 1].rating} "
              f"({leaderboard[i - 1].wins}-{leaderboard[i - 1].losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
