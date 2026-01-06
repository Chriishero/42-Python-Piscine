
def lcg_pseudogen(modulus, a, c, seed, bounds):
    while True:
        seed = (a * seed + c) % modulus
        norm = seed / modulus
        res = bounds[0] + norm * (bounds[1] - bounds[0])
        for i in range(bounds[0], bounds[1]):
            if i > res:
                yield i - 1
                break


class Stream:
    def __init__(self):
        self.total_event = 0
        self.high_level = 0
        self.treasure_events = 0
        self.levelup_events = 0

    def update_analytics(self, event):
        self.total_event += 1
        if event["level"] >= 10:
            self.high_level += 1
        if event["type"] == "found treasure":
            self.treasure_events += 1
        if event["type"] == "leveled up":
            self.levelup_events += 1

    def get_analytics(self):
        print("=== Stream Analytics ===")
        print(f"Total events processed: {self.total_event}")
        print(f"High-level players (10+): {self.high_level}")
        print(f"Treasure events: {self.treasure_events}")
        print(f"Level-up events: {self.levelup_events}\n")
        print("Memory usage: Constant (streaming)")


class GameData:
    @staticmethod
    def generator():
        players = ["alice", "bob", "charlie", "chris", "donald", "eve"]
        event_types = ["killed monster", "found treasure",
                       "leveled up", "death"]
        p_gen = lcg_pseudogen(2**31 - 1, 48271, 0, 1, [0, len(players)])
        type_gen = lcg_pseudogen(2**31 - 1, 48271, 0, 7, [0, len(event_types)])
        lvl_gen = lcg_pseudogen(2**31 - 1, 48271, 0, 42, [1, 15])
        while True:
            player = players[next(p_gen)]
            event_type = event_types[next(type_gen)]
            level = next(lvl_gen)
            yield {"player": player, "level": level, "type": event_type}


def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number():
    n = 2
    while True:
        prime = True
        for denom in range(1, n):
            if n % denom == 0 and denom != 1 and denom != n:
                prime = False
        if prime is True:
            yield n
        n += 1


def generator(n_fibonnaci, n_prime):
    print("=== Generator Demonstration ===")
    gen = fibonacci_sequence()
    print(f"Fibonacci sequence (first {n_fibonnaci}): ", end="")
    for i in range(n_fibonnaci):
        if i + 1 < n_fibonnaci:
            print(next(gen), end=", ")
        else:
            print(next(gen))

    gen = prime_number()
    print(f"Prime numbers (first {n_prime}): ", end="")
    for i in range(n_prime):
        if i + 1 < n_prime:
            print(next(gen), end=", ")
        else:
            print(next(gen))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    n = 1000
    print(f"Processing {n} game events...\n")
    gen = GameData.generator()
    stream = Stream()
    for i in range(1, n + 1):
        event = next(gen)
        if i <= 3:
            print(f"Event {i}: Player {event['player']} "
                  f"(level {event['level']}) {event['type']}")
        stream.update_analytics(event)
    print("...\n")
    stream.get_analytics()
    print("")
    generator(10, 10)
