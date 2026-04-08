import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold: "
          f"{alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()
