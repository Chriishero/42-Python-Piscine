
class ItemAttributes:
    def __init__(self, type, rarity, value, quantity):
        self.type = type
        self.rarity = rarity
        self.value = value
        self.quantity = quantity


class Inventory:
    def __init__(self, player_name):
        self.player_name = player_name
        self.items = {}
        self.item_type_count = {"weapon": 0, "consumable": 0, "armor": 0}
        self.value = 0

    def add_item(self, name, type, rarity, value, quantity):
        attributes = ItemAttributes(type, rarity, value, quantity)
        self.items[name] = attributes
        self.item_type_count[type] += quantity
        self.value += quantity * value
        print(f"New item in {self.player_name}'s inventory: "
              f"{name} ({type}, {rarity}): x{quantity} {value} gold")

    def get_item_info(self, name):
        item = self.items[name]
        print(f"{name} ({item.type}, {item.rarity}): "
              f"x{item.quantity} @ {item.value} gold each = "
              f"{item.quantity * item.value} gold")

    def get_inventory_info(self):
        print(f"=== {self.player_name}'s Inventory ===")
        for item_name in self.items.keys():
            self.get_item_info(item_name)
        print(f"\nInventory value: {self.value} gold")
        print(f"Item count: {len(self.items)} items")
        print("Categories: ", end="")
        for i, (type, count) in enumerate(self.item_type_count.items()):
            print(f"{type}({count})", end="")
            if i + 1 < len(self.items):
                print(", ", end="")
            else:
                print("")

    @staticmethod
    def transaction(invent1, invent2):
        pass


if __name__ == "__main__":
    invent1 = Inventory("Alice")
    invent1.add_item("sword", "weapon", "rare", 500, 1)
    invent1.add_item("potion", "consumable", "common", 50, 5)
    invent1.add_item("shield", "armor", "uncommon", 200, 1)
    print("")
    invent1.get_inventory_info()
