
class SecurePlant:
    """
    Simulates a plant, with setter and getter to secure access to attributes

    Attributes:
        name (str): Name of the plant.
        height (float): Current height of the plant in centimeters.
        age (int): Current age of the plant in days.
    """
    def __init__(self, name, height, age):
        print("=== Garden Security System ===")
        self.__name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)
        print("")

    def set_height(self, height):
        """
        Setter for the height attribute : it must be >= 0

        :param height: new height
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return

    def set_age(self, age):
        """
        Setter for the age attribute : it must be >= 0

        :param age: new age
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted: ",
                  f"age {age} days old [REJECTED]")
            print("Security: Negative age rejected\n")
            return

    def get_height(self):
        """
        Getter for the height attribute
        """
        return self._height

    def get_age(self):
        """
        Getter for the age attribute
        """
        return self._age

    height = property(get_height, set_height)
    age = property(get_age, set_age)


if __name__ == "__main__":
    sp1 = SecurePlant("Rose", 25, 32)
    sp1.age = -1
    sp1.height = -1
    print(f"age : {sp1.age}")
    print(f"height : {sp1.height}")
