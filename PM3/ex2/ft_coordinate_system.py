import sys
import math


def arg_valid() -> str:
    """Function that validates the number of arguments in the console input"""
    if (len(sys.argv) == 4):
        x = sys.argv[1]
        y = sys.argv[2]
        z = sys.argv[3]
        return (f'{x},{y},{z}')
    elif (len(sys.argv) == 2):
        parts = sys.argv[1].split(',')
        if len(parts) != 3:
            print(
                f"Use: python3 {sys.argv[0].split('/')[-1]} x y z or 'x,y,z'\n"
                "Also, it has to be 3 valid coordinates."
            )
            sys.exit(1)
        x = parts[0]
        y = parts[1]
        z = parts[2]
        return (f'{x},{y},{z}')
    else:
        print(
            f"Use: python3 {sys.argv[0].split('/')[-1]} x y z or 'x,y,z'\n"
            "Also, it has to be 3 valid coordinates."
        )
        sys.exit(1)


def position_parser(coord_string: str) -> tuple[int, int, int]:
    """Function that validates console input"""
    try:
        parts = coord_string.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(
            f'Parsing invalid coordinates: "{coord_string}"\n'
            f"Error parsing coordinates: {e}\n"
            f"Error details - Type: {type(e).__name__}, Args: {e.args}"
        )
        # 0 just to sinalyze the demo ended as i intended
        # in the real world it would be a 1 in the exit code
        sys.exit(0)


def distance_calculator(p1: tuple[int, int, int],
                        p2: tuple[int, int, int]) -> float:
    """Function that calculates the distance travelled"""
    # Formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    distance_x: int = p2[0] - p1[0]
    distance_y: int = p2[1] - p1[1]
    distance_z: int = p2[2] - p1[2]
    return (math.sqrt(distance_x**2 + distance_y**2 + distance_z**2))


def ft_coordinate_system() -> None:
    """Function that takes valid coordinates from the console"""
    print("=== Game Coordinate System ===\n")
    value_to_parse: str = arg_valid()
    player_pos: tuple[int, int, int] = position_parser(value_to_parse)
    origin: tuple[int, int, int] = (0, 0, 0)
    test_value: tuple[int, int, int] = (10, 20, 5)
    distance: float = distance_calculator(origin, player_pos)
    x, y, z = player_pos
    invalid_value: str = "abc,def,ghi"
    print(
        f"Position created: {test_value}\n"
        f"Distance between {origin} and {test_value}: "
        f"{distance_calculator(origin, test_value):.2f}\n\n"
        f'Parsing coordinates: "{x},{y},{z}"\n'
        f"Parsed position: {player_pos}\n"
        f"Distance between {origin} and {player_pos}: {distance:.1f}\n"
        "\nUnpacking demonstration:\n"
        f"Player at x={x}, y={y}, z={z}\n"
        f"Coordinates: X={x}, Y={y}, Z={z}\n"
    )
    position_parser(invalid_value)


if __name__ == "__main__":
    ft_coordinate_system()
