class PlantError(ValueError):
    """
    Custom exception a plant error : if the name is empty

    __str__ : 'PlantError' can return the string defined
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ("Error: Plant name cannot be empty!")


class WaterError(ValueError):
    """
    Custom exception a water level error : water level is too low or too high

    __str__ : 'WaterError' can return the string defined
    """
    def __init__(self, water_level):
        super().__init__()
        self.water_level = water_level

    def __str__(self):
        if self.water_level > 10:
            error_msg = (f"Error: Water level {self.water_level} "
                         + "is too high (max 10)")
        elif self.water_level < 1:
            error_msg = (f"Error: Water level {self.water_level} "
                         + "is too low (min 1)")
        else:
            error_msg = "Unknown water level error"
        return (error_msg)


class SunlightHoursError(ValueError):
    """
    Custom exception a sunlight hours error : sun is too low or too high

    __str__ : 'SunlightHoursError' can return the string defined
    """
    def __init__(self, hours):
        super().__init__()
        self.hours = hours

    def __str__(self):
        if self.hours > 12:
            error_msg = (f"Error: Sunlight hours {self.hours} "
                         + "is too high (max 12)")
        elif self.hours < 2:
            error_msg = (f"Error: Sunlight hours {self.hours} "
                         + "is too low (min 2)")
        else:
            error_msg = "Unknown sunlight hours error"
        return (error_msg)


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check the plant health

    :param plant_name: plant name
    :param water_level: water level
    :param sunlight_hours: sunlight hours
    """
    try:
        if plant_name == "" or plant_name is None:
            raise PlantError()
        if water_level > 10 or water_level < 1:
            raise WaterError(water_level)
        if sunlight_hours > 12 or sunlight_hours < 2:
            raise SunlightHoursError(sunlight_hours)
    except ValueError as e:
        print(e, "\n")
        return
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    """
    Check the plant health for various values
    """
    print("Testing good values...")
    check_plant_health("Tomato", 3, 10)

    print("Testing empty plant name...")
    check_plant_health("", 3, 10)

    print("Testing bad water level...")
    check_plant_health("Tomato", 11, 10)

    print("Testing bad sunlight hours...")
    check_plant_health("Tomato", 3, 0)

    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
