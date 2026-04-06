
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    name_list = ["alice", "bob", "charlie", "dylan"]
    action_list = ["run", "eat", "sleep", "grab", "move", "swim", "climb"]
    while True:
        yield (random.choice(name_list), random.choice(action_list))


def build_list(n: int) -> list[tuple[str, str]]:
    gen = gen_event()
    event_list: list[tuple[str, str]] = []
    for _ in range(n):
        event_list.append(next(gen))
    return event_list


def consume_event(event_list:
                  list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while event_list:
        index = random.randrange(len(event_list))
        yield event_list.pop(index)


def main() -> None:
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    event_list = build_list(10)
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
