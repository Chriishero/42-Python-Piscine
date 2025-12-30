
def strjoin(strs, sep):
    new_str = strs[0]
    for s in strs[1:]:
        new_str += sep + s
    return (new_str)


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return ("regular")

    def grow(self, h=1):
        self.height += h
        print(f"{self.name} grew {h}cm")

    def get_info(self):
        return (f"\n- {self.name}: {self.height}cm, {self.age} days")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def __str__(self):
        return ("flowering")

    def get_info(self):
        return (f"\n- {self.name}: {self.height}cm, {self.age} days, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self):
        return ("prize flowers")

    def get_info(self):
        return (f"\n- {self.name}: {self.height}cm, {self.age} days, "
                f"{self.color} flowers (blooming), "
                f"Prize points: {self.prize_points}")


class Garden:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all_plants(self, h=1):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(h)
            self.total_growth += h


class GardenManager:
    class GardenStats:
        @staticmethod
        def calculate(garden):
            stats = {
                "Plants in garden": "",
                "Plants added": 0,
                "Total growth": 0,
                "regular": 0,
                "flowering": 0,
                "prize flowers": 0
                }
            for plant in garden.plants:
                stats["Plants in garden"] += plant.get_info()
                stats["Plants added"] += 1
                stats[str(plant)] += 1
            stats["Total growth"] = garden.total_growth
            return (stats)

    def __init__(self):
        self.gardens = {}
        self.gardens_scores = {}
        self.total_garden_managed = 0

    def update_garden_score(self, owner_name):
        garden = self.gardens[owner_name]
        self.gardens_scores[owner_name] += garden.total_growth * 5

    def add_garden(self, garden):
        self.gardens[garden.owner_name] = garden
        self.gardens_scores[garden.owner_name] = 0
        self.total_garden_managed += 1
        self.update_garden_score(garden.owner_name)

    def height_validation_test(self, owner_name):
        garden = self.gardens[owner_name]
        for plant in garden.plants:
            if plant.height <= 0:
                return (False)
        return (True)

    def garden_report(self, owner_name):
        garden = self.gardens[owner_name]
        stats = self.GardenStats().calculate(garden)
        print(f"=== {owner_name}'s Garden Report ===")
        print(f"Plants in garden: {stats['Plants in garden']}")
        print(f"\nPlants added: {stats['Plants added']}, "
              f"Total growth: {stats['Total growth']}")
        print(f"Plants type: {stats['regular']} regular, "
              f"{stats['flowering']} flowering, "
              f"{stats['prize flowers']} prize flowers")
        print("Height validation test: "
              f"{self.height_validation_test(owner_name)}\n")

    def garden_scores(self):
        for name in self.gardens:
            self.update_garden_score(name)
        scores_items = self.gardens_scores.items()
        print("Garden scores - "
              f"{strjoin([f'{n}: {s}' for n, s in scores_items], ', ')}")

    @classmethod
    def create_garden_network(cls, names):
        manager = cls()
        for name in names:
            manager.add_garden(Garden(name))
        return (manager)


if __name__ == "__main__":
    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    print("=== Garden Management System ===\n")
    manager.gardens["Alice"].add_plant(Plant("Oak Tree", 101, 176))
    manager.gardens["Alice"].add_plant(FloweringPlant("Rose", 26, 10, "Red"))
    manager.gardens["Alice"].add_plant(PrizeFlower("Sunflower", 51,
                                                   17, "Yellow", 10))
    manager.gardens["Alice"].grow_all_plants(1)
    manager.garden_report("Alice")
    manager.garden_report("Bob")
    manager.garden_scores()
    print(f"Total gardens managed: {manager.total_garden_managed}")
