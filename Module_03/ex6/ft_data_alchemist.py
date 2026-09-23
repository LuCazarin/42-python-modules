#!/usr/bin/env python3
import random


def main():

    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps: list[str] = [n for n in players if n.istitle()]
    print(f"New list of capitalized names only: {only_caps}")

    scores: dict[str, int] = {
        n: random.randint(1, 1000) for n in all_caps
    }
    print(f"Score dict: {scores}")

    avg: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores: dict[str, int] = {
        k: v for k, v in scores.items() if v > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
