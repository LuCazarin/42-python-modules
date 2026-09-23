#!/usr/bin/env python3
import sys


def ft_score_analytics() -> None:
    arguments: list[str] = sys.argv[1:]
    print("=== Player Score Analytics ===")
    score_verify: list[int] = []
    for arg in arguments:
        try:
            score_verify.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(score_verify) != 0:
        len_score = len(score_verify)
        sum_score: int = sum(score_verify)
        average: float = sum_score / len_score
        max_score: int = max(score_verify)
        min_score: int = min(score_verify)
        score_range = max_score - min_score
        print(f"Scores processed: {score_verify}")
        print(f"Total players: {len_score}")
        print(f"Total score: {sum_score}")
        print(f"Average score: {average}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {score_range}")
    else:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
