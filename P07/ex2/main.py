from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .Combatable import Combatable
from .Magical import Magical
from .EliteCard import EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")
    c1 = EliteCard("Arcane Warrior", 4, "Legendary", 5, 3, 8, 10, "melee")
    print("EliteCard capabilities:")
    print(f"- Card: {[name for name, value in Card.__dict__.items()
                      if callable(value)]}")
    print(f"- Combatable: {[name for name, value in Combatable.__dict__.items()
                            if callable(value)]}")
    print(f"- Magical: {[name for name, value in Magical.__dict__.items()
                         if callable(value)]}")
    print
    game_state = c1.play({
        'attack_target': CreatureCard('Enemy', 3, 'Common', 2, 1),
        'incoming_damage': 4,
        'spell_name': 'Fireball',
        'spell_targets': [CreatureCard('Enemy1', 3, 'Rare', 3, 5),
                          CreatureCard('Enemy2', 6, 'Rare', 4, 3)],
        'amount_channeled_mana': 3
    })

    print("\nMultiple interface implementation successful!")
