from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


if __name__ == "__main__":
    print("\n=== DataDeck Deck Build ===\n")
    print("Building Deck with different card types...")
    c1 = CreatureCard('Fire Dragon', 5, 'Legendary',
                      7, 5)
    c2 = SpellCard('Lightning Bolt', 3, 'Rare',
                   'damage')
    c3 = ArtifactCard('Mana Crystal', 6, 'Legendary',
                      5, 'Permanent: +1 mana per turn')
    deck = Deck()
    deck.add_card(c1)
    deck.add_card(c2)
    deck.add_card(c3)
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    drew_card = deck.draw_card()
    game_state = drew_card.play({'card_played': drew_card.name,
                                 'available_mana': 9})
    print(game_state)
    print("")
    drew_card = deck.draw_card()
    game_state = drew_card.play({'card_played': drew_card.name,
                                 'available_mana': 5})
    print(game_state)
    print("")
    drew_card = deck.draw_card()
    game_state = drew_card.play({'card_played': drew_card.name,
                                 'available_mana': 7})
    print(game_state)

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")
