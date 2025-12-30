
class Plant:
    """
    Docstring for Plant

    Attributes:
        name (str): Name of the plant.
        height (float): Current height of the plant in centimeters.
        age (int): Current age of the plant in days.
        initial_height (float): Height of the plant at creation.
        initial_age (int): Age of the plant at creation (usually 0).
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height
        self.initial_age = age

    def grow(self, cm=1):
        """
        Grow the plant

        :param cm: how much the plant will grow in centimeter
        """
        self.height += cm

    def age_by_days(self, days=1):
        """
        Docstring for age_by_days

        :param days: how much the plant will age in day(s)
        """
        self.age += days

    def get_info(self):
        """
        Print some informations about the plant
        """
        print(f"=== Day {self.age - self.initial_age + 1} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_growth(self):
        """
        Return the total growth of the plant
        """
        return self.height - self.initial_height


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    plants = [p1, p2, p3]
    for p in plants:
        p.get_info()
        p.age_by_days(6)
        p.grow(6)
    [p.get_info() for p in plants]
