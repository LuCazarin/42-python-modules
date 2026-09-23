#!/usr/bin/env python3
import random
import typing


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "use", "release"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Gerador infinito que produz eventos de jogo aleatórios sob demanda."""
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx: int = random.randrange(len(event_list))
        item: tuple[str, str] = event_list.pop(idx)
        yield item


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    g: typing.Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")

    events_list: list[tuple[str, str]] = [next(g) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {events_list}\n")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
