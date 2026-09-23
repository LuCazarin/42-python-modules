#!/usr/bin/env python3
import random


ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist',
    'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer',
    'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme',
    'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    nbr_achiv: int = random.randint(3, 9)
    sampled = random.sample(ACHIEVEMENTS, nbr_achiv)
    return set(sampled)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice | bob | charlie | dylan
    print(f"\nAll distinct achievements: {all_distinct}")

    common = alice & bob & charlie & dylan
    print(f"\nCommon achievements: {common}\n")

    only_alice = alice - (bob | charlie | dylan)
    only_bob = bob - (alice | charlie | dylan)
    only_charlie = charlie - (alice | bob | dylan)
    only_dylan = dylan - (alice | bob | charlie)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    pool_set = set(ACHIEVEMENTS)
    print(f"Alice is missing: {pool_set - alice}")
    print(f"Bob is missing: {pool_set - bob}")
    print(f"Charlie is missing: {pool_set - charlie}")
    print(f"Dylan is missing: {pool_set - dylan}")
