from .CreatureCard import CreatureCard

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    c1 = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    c2 = CreatureCard('Goblin Warrior', 2, 'Rare', 3, 4)
    print("CreatureCard Info:")
    print(c1.get_card_info())
    print("")
    game_state = c1.play({'card_played': c1.name, 'available_mana': 9})
    print(game_state)
    print("")
    attack_result = c1.attack_target(c2)
    print(attack_result)
    c2.is_playable(1)
    print("\nAbstract pattern successfully demonstrated!")
