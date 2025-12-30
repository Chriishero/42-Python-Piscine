
class Plant:
    """
    Plant class

    :attribute name: name of the plant
    :attribute height: height of the plant
    :attribute age: age of the plant
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    plants = [p1, p2, p3]
    print("=== Garden Plant Registry ===")
    for p in plants:
        print(f"{p.name}: {p.height}cm, {p.age} days old")
