from ex0.CreatureFactory import CreatureFactory
from ex1.CreatureCapabilityFactory import HealingCreatureFactory
from ex1.CreatureCapabilityFactory import TransformCreatureFactory
from ex1.Capability import HealCapability, TransformCapability


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    assert isinstance(base, HealCapability)
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    assert isinstance(evolved, HealCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    assert isinstance(base, TransformCapability)
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    assert isinstance(evolved, TransformCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(heal_factory)
    print()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
