import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    if (len(sys.argv) == 1):
        print(
            "No Arguments provided!\n"
            f"Program name: {sys.argv[0].split('/')[-1]}\n"
            f"Total arguments: {len(sys.argv)}\n"
        )
    else:
        print(
            f"Program name: {sys.argv[0].split('/')[-1]}\n"
            f"Arguments received: {len(sys.argv) - 1}"
        )
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    ft_command_quest()
