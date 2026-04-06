import random


class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name = name
        self._achievements = achievements

    def print_achievements(self) -> None:
        print(f"Player {self.name}: {self.achievements}")

    @property
    def achievements(self) -> set[str]:
        return (self._achievements)


def gen_player_achievements(player_name: str,
                            achievements: set[str]) -> Player:
    n_ach = random.randint(1, len(achievements))
    player = Player(player_name, set())
    shuffled_achievements = list(achievements)
    random.shuffle(shuffled_achievements)
    for ach in shuffled_achievements:
        if n_ach > 0:
            n_ach -= 1
            player.achievements.add(ach)
    return player


def union_achievements(players: list[Player]) -> set[str]:
    if not players:
        return set()
    all_distinct = players[0].achievements.copy()
    for player in players[1:]:
        all_distinct = all_distinct.union(player.achievements)
    return all_distinct


def common_achievements(players: list[Player]) -> set[str]:
    if not players:
        return set()
    common = players[0].achievements.copy()
    for player in players[1:]:
        common = common.intersection(player.achievements)
    return common


def unique_achievements(p1: Player, players: list[Player]) -> set[str]:
    if not p1 or not players:
        return set()
    unique = p1.achievements.copy()
    for player in players:
        if p1 != player:
            unique = unique.difference(player.achievements)
    return unique


def missing_achievements(p1: Player, achievements: set[str]) -> set[str]:
    if not p1 or not achievements:
        return set()
    missings = achievements.difference(p1.achievements)
    return missings


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players_name = {"Alice", "Bob", "Charlie", "Dylan"}
    achievements = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'}
    players: list[Player] = []
    for name in players_name:
        player = gen_player_achievements(name, achievements)
        players.append(player)
        player.print_achievements()
    all_distinct_achievements = union_achievements(players)
    print(f"\nAll distinct achievements: {all_distinct_achievements}")
    common_achs = common_achievements(players)
    print(f"Common achievements: {common_achs}\n")
    for player in players:
        print(f"Only {player.name} has: "
              f"{unique_achievements(player, players)}")
    print("")
    for player in players:
        print(f"{player.name} is missing: "
              f"{missing_achievements(player, achievements)}")


if __name__ == "__main__":
    main()
