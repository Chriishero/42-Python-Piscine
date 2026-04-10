
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(m['power'] for m in mages) / len(mages), 2)
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff',  'power': 92, 'type': 'staff'},
        {'name': 'Shadow Dagger', 'power': 60, 'type': 'blade'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) comes before "
          f"{sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")
    print()

    print("Filtred artifacts (min 90 powers):", power_filter(artifacts, 90))
    print()

    print("Testing spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))
    print()

    print("Mage Stats:", mage_stats([{"name": "mage1", "power": 100},
                                     {"name": "mage2", "power": 89},
                                     {"name": "mage3", "power": 32},
                                     {"name": "mage4", "power": 73}]))


if __name__ == "__main__":
    main()
