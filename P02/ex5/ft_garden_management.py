class GardenError(Exception):
    """
    Custom exception for any garden error
    """
    def __init__(self):
        super().__init__()


class WaterTankError(GardenError):
    """
    Custom exception a water error : if the tank doesn't contain enough water

    __str__ : 'WaterTankError' can return the string defined
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ("Not enough water in tank")


class PlantError(GardenError):
    """
    Custom exception a plant error : if the name is empty

    __str__ : 'PlantError' can return the string defined
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ("Plant name cannot be empty!")


class WaterLevelError(Exception):
    """
    Custom exception a water level error : water level is too low or too high

    __str__ : 'WaterLevelError' can return the string defined
    """
    def __init__(self, water_level):
        super().__init__()
        self.water_level = water_level

    def __str__(self):
        if self.water_level > 10:
            error_msg = (f"Water level {self.water_level} "
                         + "is too high (max 10)")
        elif self.water_level < 1:
            error_msg = (f"Water level {self.water_level} "
                         + "is too low (min 1)")
        else:
            error_msg = "Unknown water level error"
        return (error_msg)


class SunlightHoursError(Exception):
    """
    Custom exception a sunlight hours error : sun is too low or too high

    __str__ : 'SunlightHoursError' can return the string defined
    """
    def __init__(self, hours):
        super().__init__()
        self.hours = hours

    def __str__(self):
        if self.hours > 12:
            error_msg = (f"Sunlight hours {self.hours} "
                         + "is too high (max 12)")
        elif self.hours < 2:
            error_msg = (f"Sunlight hours {self.hours} "
                         + "is too low (min 2)")
        else:
            error_msg = "Unknown sunlight hours error"
        return (error_msg)


class Plant:
    """
    Plant class
    """
    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class Garden:
    """
    Garden class

    add_plants : Add plants in the garden
    watering_plants : Watering all plants of the garden
    check_plants_health : Check the plants health
    """
    def __init__(self, owner_name, tank_water_level):
        self.owner_name = owner_name
        self.tank_water_level = tank_water_level
        self.plants = []

    def add_plants(self, plants):
        """
        Add plants in the garden.

        :param plants: plants list
        """
        print("Adding plants to garden...")
        for plant in plants:
            try:
                if plant.name == "" or plant.name is None:
                    raise PlantError()
            except PlantError as e:
                print(f"Error adding plant: {e}\n")
            else:
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")

    def watering_plants(self):
        """
        Water all plants in the garden.
        """
        print("Watering Plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                print("Watering " + plant.name + " - success")
        except Exception:
            print(f"Error: Cannot water {plant.name} - invalid plant")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plants_health(self):
        """
        Check all plants health
        """
        print("Checking plant health...")
        for plant in self.plants:
            name = plant.name
            water_level = plant.water_level
            sunlight_hours = plant.sunlight_hours
            try:
                if name == "" or name is None:
                    raise PlantError()
                if water_level > 10 or water_level < 1:
                    raise WaterLevelError(water_level)
                if sunlight_hours > 12 or sunlight_hours < 2:
                    raise SunlightHoursError(sunlight_hours)
            except Exception as e:
                print(f"Error checking {name}: {e}\n")
            else:
                print(f"{name}: healthy "
                      f"(water: {water_level}, sun: {sunlight_hours})")


class GardenManager:
    """
    Garden Manager

    add_garden : add garden to the garden manager
    add_garden_plants : add plants to a specific garden
    watering_garden_plants : watering the plants of a specific garden
    check_garden_health : check the health of a specific garden's plants
    error_recovery : testing error recovery
    """
    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden):
        """
        Add a garden in the garden manager

        :param garden: garden
        """
        self.gardens[garden.owner_name] = garden

    def add_garden_plants(self, owner_name, plants):
        """
        Add plants in a specific garden

        :param owner_name: garden's owner name
        :param plants: list of plants
        """
        self.gardens[owner_name].add_plants(plants)

    def watering_garden_plants(self, owner_name):
        """
        Watering all plants of a specific garden

        :param owner_name: garden's owner name
        """
        self.gardens[owner_name].watering_plants()

    def check_garden_health(self, owner_name):
        """
        Check all plants health of a specific garden

        :param owner_name: garden's owner name
        """
        self.gardens[owner_name].check_plants_health()

    def error_recovery(self):
        """
        Test error recovery of the garden manager
        """
        print("Testing error recovery...")
        for name, garden in self.gardens.items():
            try:
                if garden.tank_water_level < 10:
                    raise WaterTankError()
            except GardenError as e:
                print(f"Caught {GardenError.__name__}: {e}")
        print("System recovered and continuing...")


if __name__ == "__main__":
    gm = GardenManager()
    gm.add_garden(Garden("Chris", 9))
    print("== Garden Management System ===\n")
    gm.add_garden_plants("Chris", [Plant("tomato", 3, 5),
                                   Plant("lettuce", 15, 12),
                                   Plant("", 4, 6)])
    gm.watering_garden_plants("Chris")
    gm.check_garden_health("Chris")
    gm.error_recovery()
