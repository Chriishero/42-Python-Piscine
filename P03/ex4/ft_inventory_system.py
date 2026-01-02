
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
        if self.items.get(name):
            attributes = ItemAttributes(type, rarity, value,
                                        self.items[name].quantity + quantity)
        else:
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
                print("\n")

    def transaction_to(self, to_invent, item_name, quantity):
        item = self.items[item_name]
        print(f"=== Transaction: {self.player_name} gives "
              f"{to_invent.player_name} {quantity} {item_name}s ===")
        if item.quantity < quantity:
            print("Transaction failed: "
                  f"{self.player_name} doesn't have enough {item_name}s")
        elif quantity <= 0:
            print("Transaction failed: quantity must be > 0")
        elif item.quantity >= quantity:
            to_invent.add_item(item_name, item.type, item.rarity,
                               item.value, quantity)
            self.set_item_attribute(name=item_name, quantity=True,
                                    new_value=item.quantity - quantity)
            print("Transaction successful!\n")
            print("=== Updated Inventories ===")
            print(f"{self.player_name} {item_name}: "
                  f"{self.get_item_attribute(name=item_name, quantity=True)}")
            print(f"{to_invent.player_name} {item_name}: "
                  f"{to_invent.items[item_name].quantity}\n")

    def get_item_attribute(self, name: str, type=False, rarity=False,
                           quantity=False, value=False):
        if self.items.get(name):
            item = self.items[name]
        else:
            item = ItemAttributes(0, 0, 0, 0)
        if type:
            return item.type
        elif rarity:
            return item.rarity
        elif quantity:
            return item.quantity
        elif value:
            return item.value
        return name

    def set_item_attribute(self, name=None, type=False, rarity=False,
                           quantity=False, value=False, new_value=None):
        if type:
            self.items[name].type = new_value
        elif rarity:
            self.items[name].rarity = new_value
        elif quantity:
            old_value = self.items[name].quantity
            self.items[name].quantity = new_value
            self.item_type_count[self.items[name].type] += (new_value
                                                            - old_value)
        elif value:
            self.items[name].value = new_value

    def get_items_count(self):
        count = 0
        for t, c in self.item_type_count.items():
            count += c
        return (count)

    @staticmethod
    def get_analytics(inventories):
        print("=== Inventory Analytics ===")
        most_valuable = ["", 0]
        most_items = ["", 0]
        rarest_items = {}
        for inventory in inventories:
            if inventory.value > most_valuable[1]:
                most_valuable[0] = inventory.player_name
                most_valuable[1] = inventory.value

            if inventory.get_items_count() > most_items[1]:
                most_items[0] = inventory.player_name
                most_items[1] = inventory.get_items_count()

            for name, item_att in inventory.items.items():
                if item_att.rarity == "rare":
                    rarest_items[name] = True

        print(f"Most valuable player: {most_valuable[0]} "
              f"({most_valuable[1]} gold)")
        print(f"Most items: {most_items[0]} ({most_items[1]} items)")
        print("Rarest items: ", end="")
        i = 0
        for name, _ in rarest_items.items():
            if i + 1 < len(rarest_items):
                print(f"{name}, ", end="")
            else:
                print(f"{name}")
            i += 1


if __name__ == "__main__":
    invent1 = Inventory("Alice")
    invent1.add_item("sword", "weapon", "rare", 500, 1)
    invent1.add_item("potion", "consumable", "common", 50, 5)
    invent1.add_item("shield", "armor", "uncommon", 200, 1)
    invent2 = Inventory("Bob")
    invent2.add_item("sword", "weapon", "rare", 500, 2)
    invent2.add_item("potion", "consumable", "common", 50, 2)
    invent2.add_item("magic_ring", "armor", "rare", 700, 1)
    print("")
    invent1.get_inventory_info()
    invent1.transaction_to(invent2, "potion", 1)
    Inventory.get_analytics([invent1, invent2])
