
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coor_str = input("Enter new coordinates as floats in format "
                         "'x,y,z': ")
        try:
            x_str, y_str, z_str = coor_str.split(',')
        except ValueError:
            print("Invalid syntax")
            continue
        for coor in (x_str, y_str, z_str):
            try:
                float(coor.strip())
            except ValueError:
                print(f"Error on parameter '{coor.strip()}': "
                      f"could not convert string to float: '{coor.strip()}'")
                break
        else:
            x = float(x_str.strip())
            y = float(y_str.strip())
            z = float(z_str.strip())
            return round(x, 1), round(y, 1), round(z, 1)


def euclidian_distance(coord1: tuple[float, float, float],
                       coord2: tuple[float, float, float]) -> float:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Get a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    origin_distance = round(euclidian_distance((0.0, 0.0, 0.0), (x1, y1, z1)),
                            4)
    print(f"Distance to center: {origin_distance}\n")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    points_distance = round(euclidian_distance((x1, y1, z1), (x2, y2, z2)), 4)
    print(f"Distance between the 2 sets of coordinates: {points_distance}")


if __name__ == "__main__":
    main()
