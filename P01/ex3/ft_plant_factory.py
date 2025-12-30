
class Plant:
    """
    Docstring for Plant

    Attributes:
        name (str): Name of the plant.
        height (float): Current height of the plant in centimeters.
        age (int): Current age of the plant in days.
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created : {self.name} ({self.height}cm, {self.age} days)")


def ft_listlen(lst: list):
    """
    Return the len (number of elements) of a list.

    :param lst: the list whose len must be computed
    :type lst: list
    """
    i = 0
    for element in lst:
        i += 1
    return i


if __name__ == "__main__":
    names_list = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights_list = [25, 200, 5, 80, 15]
    ages_list = [30, 365, 90, 45, 120]
    n_plant = ft_listlen(names_list)
    print("=== Plant Factory Output ===")
    plants = [Plant(names_list[i], heights_list[i], ages_list[i])
              for i in range(n_plant)]
    print(f"\nTotal plants created : {n_plant}")
