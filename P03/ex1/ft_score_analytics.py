
import sys


def score_analytics(scores: list):
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    n_players = len(scores)
    total_score = sum(int(score) for score in scores)
    average_score = total_score / n_players
    max_score = int(max(scores))
    min_score = int(min(scores))

    print(f"Scores processed: {[int(score) for score in scores]}")
    print(f"Total players: {n_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}\n")


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    print("=== Player Score Analytics ===")
    try:
        score_analytics(argv[1:])
    except ValueError:
        print("Error: All arguments must be valid intergers")
