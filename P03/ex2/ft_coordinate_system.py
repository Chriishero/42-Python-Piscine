
import sys
import math


def ft_len(data_struct):
    i = 0
    for _ in data_struct:
        i += 1
    return (i)


def strjoin(strs, sep):
    new_str = strs[0]
    for s in strs[1:]:
        new_str += sep + s
    return (new_str)


class Coordinates:
    def __init__(self, x: int, y: int, z: int):
        self.coordinates = (x, y, z)

    @property
    def x(self):
        return (self.coordinates[0])

    @property
    def y(self):
        return (self.coordinates[1])

    @property
    def z(self):
        return (self.coordinates[2])

    @staticmethod
    def get_distance(coords1, coords2):
        (x1, y1, z1) = coords1
        (x2, y2, z2) = coords2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Distance between {coords1} and {coords2}: {float(distance)}")
        return (distance)

    @classmethod
    def create_coordinates(cls, coords):
        try:
            coords[0] + ""
            try:
                x, y, z = coords.split(',')
                x = int(x)
                y = int(y)
                z = int(z)
            except Exception as e:
                print(f"\nParsing invalid coordinates: \"{coords}\"")
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - Type: {e.__class__.__name__}, "
                      f"Args: (\"{e}\")")
                return
            else:
                print(f"\nParsing coordinates: \"{coords}\"")
                print(f"Parsed position: {(x, y, z)}")
        except TypeError:
            x, y, z = coords
            print(f"\nPosition created: {(x, y, z)}")
        return (cls(x, y, z))


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = ft_len(argv)
    coords = None

    print("=== Game Coordinate System ===")
    if argc == 1:
        coords = Coordinates.create_coordinates(argv[0])
    elif argc > 1:
        coords = Coordinates.create_coordinates(strjoin(argv, ','))
    if coords:
        Coordinates.get_distance((0, 0, 0), coords.coordinates)
    coords = Coordinates.create_coordinates((10, 9, 0))
    Coordinates.get_distance((0, 0, 0), coords.coordinates)

    print("\nUnpacking demonstration:")
    x, y, z = xyz = coords.coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={xyz[0]}, Y={xyz[1]}, Z={xyz[2]}")
