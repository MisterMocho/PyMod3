import sys


def ft_score_analytics() -> None:
    """function that takes console arguments and creates a list of ints"""
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print(
            "No scores provided. Usage: python3 "
            f"{sys.argv[0].split('/')[-1]} <score1> <score2> ...\n"
        )
    else:
        scores: list[int] = []
        try:
            for arg in sys.argv[1:]:
                scores.append(int(arg))
        except ValueError:
            print(
                "In order to your quest complete "
                "a number valid, type you must\n"
            )
            return
        total: int = sum(scores)
        nb_players: int = len(scores)
        max_score: int = max(scores)
        min_score: int = min(scores)
        print(
            f"Scores processed: {scores}\n"
            f"Total players: {nb_players}\n"
            f"Total score: {total}\n"
            f"Average score: {total / nb_players}\n"
            f"High score: {max_score}\n"
            f"Low score: {min_score}\n"
            f"Score range: {max_score - min_score}\n"
        )


if __name__ == "__main__":
    ft_score_analytics()





