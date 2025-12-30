
class GardenError(Exception):
    """
    Custom exception for any garden error
    """
    __name__ = "GardenError"


class PlantError(GardenError):
    """
    Custom exception a plant error : if the plant is wilting
    __str__ : 'PlantError' can return the string defined
    """
    __name__ = "PlantError"

    def __init__(self, plant_name):
        self.plant_name = plant_name

    def __str__(self):
        return (f"The {self.plant_name} plant is wilting!")


class WaterError(GardenError):
    """
    Custom exception a water error : if the tank doesn't contain enough water
    __str__ : 'WaterError' can return the string defined
    """
    __name__ = "WaterError"

    def __str__(self):
        return ("Not enough water in the tank!")


def is_plant_wilting(plant_name, last_watering):
    """
    Test if the plant is wilting.

    :param plant_name: plant name
    :param last_watering: last day from now of the last plant watering
    """
    try:
        print("Testing PlantError...")
        if last_watering > 2:
            raise PlantError(plant_name)
    except PlantError as e:
        print(e, "\n")


def is_enough_water(n_liter):
    """
    Test if the tank contains enough water.

    :param n_liter: quantity of wate (liter) in the tank
    """
    try:
        print("Testing WaterError...")
        if n_liter < 100:
            raise WaterError
    except WaterError as e:
        print(e, "\n")


def is_garden_error(plant_name, last_watering, n_liter):
    """
    Test if there are any garden error.

    :param plant_name: plant name
    :param last_watering: last day from now of the last plant watering
    :param n_liter: quantity of wate (liter) in the tank
    """
    print("Testing catching all garden errors...")
    try:
        if last_watering > 2:
            raise PlantError(plant_name)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        if n_liter < 100:
            raise WaterError
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors ===\n")
    is_plant_wilting("tomato", 3)
    is_enough_water(90)
    is_garden_error("tomato", 3, 90)
