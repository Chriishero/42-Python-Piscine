
def ft_seed_inventory(seed_type:	str, quantity:	int, unit:	str) -> None:
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first = seed_type[0]
    for i in range(26):
        if first == lower_case[i]:
            first = upper_case[i]
            break
    seed_type = first + seed_type[1:]
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
