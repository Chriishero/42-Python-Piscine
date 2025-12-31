
class AchievementStruct:
    def __init__(self, achievements: set):
        self.achievements = achievements

    @classmethod
    def create_achievements(cls, achievements: set):
        for ach in achievements:
            try:
                ach[0] + ""
            except TypeError as e:
                print(f"Error creating achivements struct: {e}")
                print(f"Error details - Type: {e.__class__.__name__}, "
                      f"Reason: achievements must be 'str' objects")
                return None
        return (cls(achievements))


class Player:
    def __init__(self, name: str, achievements: AchievementStruct):
        self.name = name
        self.achievements = achievements

    @classmethod
    def create_player(cls, name: str, achivement_set: set):
        try:
            name + ""
            achievements = AchievementStruct.create_achievements(achivement_set)
        except TypeError as e:
            print(f"Error creating player : {e}")
            print(f"Error details - Type: {e.__class__.__name__}, "
                  f"Args: (\"{e}\")")
            return None
        return (cls(name, achievements))


if __name__ == "__main__":
    player1 = Player.create_player("Chris",
                                   {'first_kill', 'level_10',
                                    'treasure_hunter', 1})
