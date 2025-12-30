
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name} (Plant): {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blowing beautifully!\n")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              "{self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = (self.age * self.trunk_diameter) / self.height**2 * 200
        print(f"{self.name} provides "
              f"{(shade_area):.0f} square meters of shade\n")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              "{self.trunk_diameter} diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              "{self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("Tulip", 20, 22, "yellow")
    t1 = Tree("Oak", 500, 1825, 50)
    t2 = Tree("Baobab", 2200, 42059, 929)
    v1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    v2 = Vegetable("Onion", 39, 67, "spring", "antioxidant")
    plants = [f1, f2, t1, t2, v1, v2]
    for p in plants:
        p.get_info()
    print("")
    f1.bloom()
    f2.bloom()
    t1.produce_shade()
    t2.produce_shade()
    v1.get_nutritional_value()
    v2.get_nutritional_value()
