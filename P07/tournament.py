from ex2 import BattleStrategy
from ex0.CreatureFactory import CreatureFactory, FlameFactory, AquaFactory
from ex1.CreatureCapabilityFactory import HealingCreatureFactory
from ex1.CreatureCapabilityFactory import TransformCreatureFactory


def battle(opponents: list[tuple[CreatureFactory,
                                 BattleStrategy.BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatures = [(creature.create_base(), strategy)
                 for creature, strategy in opponents]
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature_a, strategy_a = creatures[i]
            creature_b, strategy_b = creatures[j]
            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except BattleStrategy.InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = BattleStrategy.NormalStrategy()
    aggressive = BattleStrategy.AggressiveStrategy()
    defensive = BattleStrategy.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_factory, normal), (heal_factory, defensive)])
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_factory, aggressive), (heal_factory, defensive)])
    print()

    print("Tournament 2 (multiple)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(aqua_factory, normal), (heal_factory, defensive),
            (transform_factory, aggressive)])
    print()


if __name__ == "__main__":
    main()
