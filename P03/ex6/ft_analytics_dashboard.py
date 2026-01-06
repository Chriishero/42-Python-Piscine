
class Player:
    def __init__(self, name, score, achievements, region, active):
        self.name = name
        self.score = score
        self.achievements = achievements
        self.region = region
        self.active = active


class GameDashboard:
    def __init__(self, players):
        self.players = players
        self.unique_achievements = None

    def score_activity_analytics(self):
        players = self.players
        high_scorers = [player.name for player in players
                        if player.score > 2000]
        scores_doubled = [player.score * 2 for player in players]
        active_players = [player.name for player in players
                          if player.active is True]

        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {scores_doubled}")
        print(f"Active players: {active_players}")

    def mapping_analytics(self):
        players = self.players
        self.player_scores = {player.name: player.score for player in players}
        categories = ["low", "medium", "high"]
        score_categories = {categorie: i + 1
                            for i, categorie in enumerate(categories)}
        achievement_counts = {player.name: len(player.achievements)
                              for player in players}

        print(f"Player scores: {self.player_scores}")
        print(f"Score categories: {score_categories}")
        print(f"Achievement counts: {achievement_counts}")

    def unique_analytics(self):
        players = self.players
        unique_players = {player.name for player in players}
        self.unique_achievements = {player.achievements[i]
                                    for player in players
                                    for i in range(len(player.achievements))}
        active_regions = {player.region for player in players}

        print(f"Unique players: {unique_players}")
        print(f"Unique achievement: {self.unique_achievements}")
        print(f"Active regions: {active_regions}")

    def combined_analytics(self):
        players = self.players
        total_players = len(players)
        total_unique_achievements = len(self.unique_achievements)
        scores = [player.score for player in players]
        average_score = sum(scores) / total_players
        top_performers = sorted(self.players, key=lambda player: player.score,
                                reverse=True)
        top_performer = top_performers[0]

        print(f"Total players: {total_players}")
        print(f"Total unique achievements: {total_unique_achievements}")
        print(f"Average score: {average_score}")
        print(f"Top performer: {top_performer.name} "
              f"({top_performer.score} points, "
              f"{len(top_performer.achievements)} achievements)")


if __name__ == "__main__":
    dashboard = GameDashboard([
        Player("Alice", 2300,
               ['first_kill', 'level_10', 'treasure_hunter',
                'speed_demon', 'collector'],
               "north", True),
        Player("Bob", 1800,
               ['treasure_hunter', 'collector', 'boss_slayer'],
               "north", True),
        Player("Charlie", 2150,
               ['treasure_hunter', 'speed_demon', 'collector',
                'boss_slayer', 'perfectionist'],
               "central", True),
        Player("Diana", 2050,
               ['treasure_hunter', 'collector', 'perfectionist',
                'speed_demon'],
               "east", False)
        ])
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    dashboard.score_activity_analytics()
    print("\n=== Dict Comprehension Examples ===")
    dashboard.mapping_analytics()
    print("\n=== Set Comprehension Examples ===")
    dashboard.unique_analytics()
    print("\n=== Combined Analysis ===")
    dashboard.combined_analytics()
