
class SecurePlant:
    def __init__(self, name, height, age):
        print("=== Garden Security System ===")
        self.__name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)
        print("")

    def set_height(self, height):
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return

    def set_age(self, age):
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted: ",
                  f"age {age} days old [REJECTED]")
            print("Security: Negative age rejected\n")
            return

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    height = property(get_height, set_height)
    age = property(get_age, set_age)


if __name__ == "__main__":
    sp1 = SecurePlant("Rose", 25, 32)
    sp1.age = -1
    sp1.height = -1
    print(f"age : {sp1.age}")
    print(f"height : {sp1.height}")
