
import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                    'Gregory', 'john', 'kevin', 'Liam']
    all_capitalizes = [name.capitalize() for name in initial_list]
    only_capitalizes = [name for name in initial_list
                        if name == name.capitalize()]
    score_dict = {key: value for key,
                  value in zip(all_capitalizes,
                               random.sample(range(1, 1000),
                                             len(all_capitalizes)))}
    score_average = round(sum(list(score_dict.values())) / len(score_dict), 2)
    high_scores = {key: value for key, value in score_dict.items()
                   if value > score_average}
    print(f"Initial list of players: {initial_list}")
    print(f"New list with all names capitalized: {all_capitalizes}")
    print(f"New list of capitalized names only: {only_capitalizes}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {score_average}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
