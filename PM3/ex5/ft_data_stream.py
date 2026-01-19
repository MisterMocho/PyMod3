import time
import random


def game_event_gen(limit: int):
    """Small function that generates a given number of events"""
    names = ["alice", "bob", "charlie", "dave", "eve", "filips",
             "gui", "hugo", "ines", "john", "kirk", "luis", "mario",
             "nini", "otto", "paulo", "quip", "rat", "stu", "tom",
             "uni", "volt", "watt", "xilo", "yuri", "zed"]
    actions = ["killed monster", "found treasure", "found a child",
               "leveled up", "joined guild", "got married",
               "offended a dwarf", "built a house", "found a secret"]
    for _ in range(limit):
        name = random.choice(names)
        level = random.randint(1, 15)
        action = random.choice(actions)
        yield f"Player {name} (level {level}) {action}"


def fibonacci_generator(n: int):
    """Yields the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int):
    """Yields the first n Prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    """Function that deals with huge amounts of data via stream"""
    total_events: int = 1000
    highlvl_cnt: int = 0
    treasure_cnt: int = 0
    levelup_cnt: int = 0
    events_processed: int = 0
    stream_gen = game_event_gen(total_events)
    stream_iter = iter(stream_gen)
    i: int = 0
    print(
        "=== Game Data Stream Processor ===\n"
        f"\nProcessing {total_events} game events...\n"
    )
    start_time = time.perf_counter()
    while True:
        try:
            event = next(stream_iter)
            i += 1
            if (i <= 3):
                print(f"Event {i}: {event}")
            elif (i == 4):
                print("...\n")
            try:
                start_i = event.find("(level ") + 7
                end_i = event.find(")", start_i)
                level = int(event[start_i:end_i])
                if (level >= 10):
                    highlvl_cnt += 1
            except ValueError:
                pass
            if ("found treasure" in event):
                treasure_cnt += 1
            elif ("leveled up" in event):
                levelup_cnt += 1
            events_processed += 1
        except StopIteration:
            break
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(
        "=== Stream Analytics ===\n"
        f"Total events processed: {events_processed}\n"
        f"High-level players (10+): {highlvl_cnt}\n"
        f"Treasure events: {treasure_cnt}\n"
        f"Level-up events: {levelup_cnt}\n"
        "\nMemory usage: Constant (streaming)\n"
        f"Processing time: {duration:.3f} seconds\n"
    )
    fib_seq: int = 10
    fib_gen = fibonacci_generator(fib_seq)
    fib_iter = iter(fib_gen)
    fib_results: list[str] = []
    while True:
        try:
            fib_results.append(str(next(fib_iter)))
        except StopIteration:
            break
    prime_seq: int = 5
    prime_gen = prime_generator(prime_seq)
    prime_iter = iter(prime_gen)
    prime_results: list[str] = []
    while True:
        try:
            prime_results.append(str(next(prime_iter)))
        except StopIteration:
            break
    print(
        "=== Generator Demonstration ===\n"
        f"Fibonacci sequence (first {fib_seq}): {', '.join(fib_results)}\n"
        f"Prime numbers (first {prime_seq}): {', '.join(prime_results)}"
    )


if __name__ == "__main__":
    ft_data_stream()
