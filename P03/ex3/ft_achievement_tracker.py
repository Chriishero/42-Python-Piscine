
class Player:
    def __init__(self, name: str, achievements: set):
        self.name = name
        self._achievements = achievements

    def print_achievements(self):
        print(f"Player {self.name} achievements: {self.achievements}")

    @property
    def achievements(self):
        return (self._achievements)


class Achievement:
    @staticmethod
    def analytics(players: list):
        unique_achievements = set()
        for p1 in players:
            unique_achievements.update(p1.achievements)
        print(f"All unique achievements: {unique_achievements}")
        print(f"Total unique achievements: {len(unique_achievements)}\n")

        rare_achievements = set(unique_achievements)
        common_achievements = set(unique_achievements)
        for a in unique_achievements:
            for p1 in players:
                for p2 in players[:players.index(p1):]:
                    if a in p1.achievements and a in p2.achievements:
                        rare_achievements.discard(a)
                    elif a in p1.achievements and a not in p2.achievements:
                        common_achievements.discard(a)
        print(f"Common to all players: {common_achievements}")
        print(f"Rare achievements (1 player): {rare_achievements}\n")

    @staticmethod
    def players_comparaison(player1, player2):
        print(f"{player1.name} vs {player2.name} common: "
              f"{player1.achievements.intersection(player2.achievements)}")
        print(f"{player1.name} unique: "
              f"{player1.achievements.difference(player2.achievements)}")
        print(f"{player2.name} unique: "
              f"{player2.achievements.difference(player1.achievements)}")


if __name__ == "__main__":
    p1 = Player("Chris",
                {'level_10', 'treasure_hunter',
                 'boss_slayer', 'speed_demon',
                 'perfectionist'})
    p2 = Player("Alice",
                {'first_kill', 'level_10',
                 'treasure_hunter', 'speed_demon'})
    p3 = Player("Bob",
                {'first_kill', 'level_10',
                 'boss_slayer', 'collector'})

    print("=== Achievement Tracker System ===\n")
    p1.print_achievements()
    p2.print_achievements()
    p3.print_achievements()

    print("\n=== Achievement Analytics ===")
    Achievement.analytics([p1, p2, p3])
    Achievement.players_comparaison(p1, p2)
